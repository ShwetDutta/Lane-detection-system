import cv2
import numpy as np

def region_of_interest(image):
    height = image.shape[0]
    width = image.shape[1]
    polygons = np.array([[
    (int(width * 0.1), height),
    (int(width * 0.9), height),
    (int(width * 0.5), int(height * 0.6))
]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return line_image

video = cv2.VideoCapture('lane_video.mp4')

while True:
    ret, frame = video.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gaussian_blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(gaussian_blur, 50, 150)
    cropped_edges = region_of_interest(canny)

    lines = cv2.HoughLinesP(
        cropped_edges,
        rho=1,
        theta=np.pi/180,
        threshold=80,
        minLineLength=50,
        maxLineGap=150
    )

    line_image = display_lines(frame, lines)

    combined = cv2.addWeighted(frame, 0.8, line_image, 1, 1)

    cv2.imshow('Lane Detection', combined)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

