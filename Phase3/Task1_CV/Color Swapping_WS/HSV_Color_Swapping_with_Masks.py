import cv2
import numpy as np

#I chose a more challenging image—one with varying lighting—and tried to produce the best possible result.

# Load image
image = cv2.imread("colors.jpg")


# Blur
image = cv2.GaussianBlur(image, (7, 7), 0)



# Convert BGR to HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


# Mouse function to get HSV values To try to get the range of orange which has low brightness
def get_hsv(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("BGR:", image[y, x])
        print("HSV:", image_hsv[y, x])


cv2.imshow("Image", image)
cv2.setMouseCallback("Image", get_hsv)


# Red
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([4, 255, 255])

lower_red2 = np.array([175, 100, 100])
upper_red2 = np.array([179, 255, 255])


red_mask1 = cv2.inRange(image_hsv, lower_red1, upper_red1)
red_mask2 = cv2.inRange(image_hsv, lower_red2, upper_red2)

red_mask = red_mask1 | red_mask2


# Orange
lower_orange = np.array([2, 40, 80])
upper_orange = np.array([20, 255, 255])

orange_mask = cv2.inRange(
    image_hsv,
    lower_orange,
    upper_orange
)

# =========================
# Yellow
# =========================

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([34, 255, 255])

yellow_mask = cv2.inRange(
    image_hsv,
    lower_yellow,
    upper_yellow
)


# =========================
# Green
# =========================

lower_green = np.array([35, 80, 80])
upper_green = np.array([90, 255, 255])

green_mask = cv2.inRange(
    image_hsv,
    lower_green,
    upper_green
)


# =========================
# Create result
# =========================

result = image.copy()

height, width = image.shape[:2]


# =========================
# Swap colors
# =========================

for y in range(height):

    for x in range(width):

        # Orange → Red
        if orange_mask[y, x] > 0:
            result[y, x] = [0, 0, 255]

        # Red → Green
        if red_mask[y, x] > 0:
            result[y, x] = [0, 255, 0]

        # Green → Orange
        if green_mask[y, x] > 0:
            result[y, x] = [0, 165, 255]

        # Yellow → Red
        if yellow_mask[y, x] > 0:
            result[y, x] = [0, 0, 255]


# Display
cv2.imshow("Original", image)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()