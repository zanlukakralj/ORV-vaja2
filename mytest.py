import cv2 as cv
import numpy as np
import naloga2

def test_filtriraj_z_gaussovim_jedrom():
    test_image = cv.imread('.utils/lenna.png')

    expected_result = np.array([[47, 49, 52], [50, 51, 54], [57, 58, 60]])

    filtered_image = naloga2.filtriraj_z_gaussovim_jedrom(test_image, 1)

    assert np.array_equal(filtered_image, expected_result), "Test failed for filtriraj_z_gaussovim_jedrom function"
    print("Test passed.")

if __name__ == "__main__":
    test_filtriraj_z_gaussovim_jedrom()
