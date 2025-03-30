import cv2
import numpy as np

def compare_images(image1_path, image2_path, threshold=2):
    # Load images
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    if img1 is None:
        print(f"Error loading image: {image1_path}")
        return False
    if img2 is None:
        print(f"Error loading image: {image2_path}")
        return False

    if img1.shape != img2.shape:
        print("Images have different dimensions!")
        return False

    # Convert images to RGB if they have alpha channels (transparency)
    if img1.shape[2] == 4:  # If image has alpha channel
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGRA2BGR)
    if img2.shape[2] == 4:  # If image has alpha channel
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGRA2BGR)

    # Compute absolute difference
    diff = cv2.absdiff(img1, img2)
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Count non-zero (different) pixels
    non_zero_count = np.count_nonzero(gray_diff)
    total_pixels = img1.shape[0] * img1.shape[1]

    diff_percentage = (non_zero_count / total_pixels) * 100

    print(f"Non-zero pixels: {non_zero_count}, Total pixels: {total_pixels}")
    print(f"Difference percentage: {diff_percentage:.2f}%")

    if diff_percentage > threshold:
        print(f"Images differ by {diff_percentage:.2f}% (Threshold: {threshold}%)")

        # Save the difference image instead of showing a pop-up
        diff_image_path = "difference.png"
        cv2.imwrite(diff_image_path, diff)
        print(f"Difference image saved as {diff_image_path}")

        return False
    else:
        print("Images match within the acceptable threshold!")
        return True

# usage
image1 = "current_visualization.png"
image2 = "reference_visualization.png"

if compare_images(image1, image2, threshold=5):  # Adjusted threshold for testing
    print("Images are similar.")
else:
    print("Images are different.")
