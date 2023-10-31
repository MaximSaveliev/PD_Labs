import unittest
import numpy as np
from mathmy import Math

class TestMathFunctions(unittest.TestCase):
    def test_cross_entropy_loss(self):
        y = np.array([1, 0, 1, 0, 1])  # Actual class labels (1 or 0)
        y_hat = np.array([0.8, 0.2, 0.7, 0.3, 0.9])  # Predicted probabilities
        result = Math.cross_entropy_loss(y, y_hat)
        self.assertAlmostEqual(result, 0.5328157977291422, places=6)

    def test_sigmoid(self):
        result = Math.sigmoid(0.3)
        self.assertEqual(result, 0.574442516811659)

    def test_logistic_regression_weight_update(self):
        w = [0.1, 0.2]
        X = [[1, 2], [2, 3], [3, 4]]
        y = [0, 1, 0]
        y_hat = [0.3, 0.7, 0.2]
        result = Math.logistic_regression_weight_update(w, X, y, y_hat, learning_rate=0.1)
        self.assertEqual(result, [0.09000000000000001, 0.18333333333333335])

    def test_mean_squared_error(self):
        y = [1, 2, 3]
        y_hat = [0.9, 2.1, 3.2]
        result = Math.mean_squared_error(y, y_hat)
        self.assertAlmostEqual(result, 0.020000000000000028, places=5)

    def test_cross_entropy_loss(self):
        y = [0, 1, 0]
        y_hat = [0.1, 0.9, 0.2]
        result = Math.cross_entropy_loss(y, y_hat)
        self.assertAlmostEqual(result, 0.14462152754328741, places=5)

if __name__ == '__main__':
    unittest.main(exit=False)
