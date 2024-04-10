import cv2 as cv
import numpy as np
import naloga2

def test_filtriraj_z_gaussovim_jedrom():
    test_image = np.array([[[10, 20, 30], [40, 50, 60], [70, 80, 90]],
                       [[100, 110, 120], [130, 140, 150], [160, 170, 180]],
                       [[190, 200, 210], [220, 230, 240], [250, 0, 0]]], dtype=np.uint8)

    expected_result = naloga2.filtriraj_z_gaussovim_jedrom(test_image, 1)

    filtered_image = naloga2.filtriraj_z_gaussovim_jedrom(test_image, 1)

    assert np.array_equal(filtered_image, expected_result), "Test failed for filtriraj_z_gaussovim_jedrom function"
    print("Test passed.")

if __name__ == "__main__":
    test_filtriraj_z_gaussovim_jedrom()
