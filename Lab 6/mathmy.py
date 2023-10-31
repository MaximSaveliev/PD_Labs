# Модуль Math.py
import numpy as np

class Math:
    def normal_distribution(x, mu, sigma):
        """
        Вычисляет значение нормального распределения (гауссианы) в заданной точке.

        Args:
            x (float): Значение входной переменной.
            mu (float): Среднее значение (математическое ожидание) распределения.
            sigma (float): Стандартное отклонение распределения.

        Returns:
            float: Значение нормального распределения в точке `x`.
        """
        coefficient = 1 / (sigma * np.sqrt(2 * np.pi))
        exponent = -0.5 * ((x - mu) / sigma) ** 2
        return coefficient * np.exp(exponent)

    def sigmoid(x):
        """
        Вычисляет сигмоидальную (логистическую) функцию в заданной точке.

        Args:
            x (float): Значение входной переменной.

        Returns:
            float: Значение сигмоидальной функции в точке `x`.
        """
        return 1 / (1 + np.exp(-x))

    def logistic_regression_weight_update(w, X, y, y_hat, learning_rate=0.0005):
        """
        Обновляет веса логистической регрессии с использованием градиентного спуска.

        Args:
            w (numpy.ndarray): Вектор весов.
            X (numpy.ndarray): Матрица признаков.
            y (numpy.ndarray): Вектор истинных классов (0 или 1).
            y_hat (numpy.ndarray): Предсказанные значения (0-1 вероятности).
            learning_rate (float): Скорость обучения (по умолчанию 0.0005).

        Returns:
            numpy.ndarray: Обновленный вектор весов.
        """
        n = len(X)  # Количество выборок

        for j in range(len(w)):
            gradient = 0.0
            for i in range(n):
                gradient += (y_hat[i] - y[i]) * X[i][j]
            gradient /= n

            w[j] = w[j] - learning_rate * gradient

        return w

    def mean_squared_error(y, y_hat):
        """
        Вычисляет среднеквадратичную ошибку между истинными и предсказанными значениями.

        Args:
            y (numpy.ndarray): Вектор истинных значений.
            y_hat (numpy.ndarray): Вектор предсказанных значений.

        Returns:
            float: Среднеквадратичная ошибка.
        """
        n = len(y)
        squared_diff = (np.array(y) - np.array(y_hat)) ** 2
        mse = np.sum(squared_diff) / n
        return mse

    def cross_entropy_loss(y, y_hat):
        """
        Вычисляет функцию потерь перекрестной энтропии.

        Args:
            y (numpy.ndarray): Вектор истинных классов (0 или 1).
            y_hat (numpy.ndarray): Вектор предсказанных вероятностей (0-1).

        Returns:
            float: Значение функции потерь перекрестной энтропии.
        """
        output_size = len(y)
        loss = -np.sum(y * np.log(y_hat) + (1 - np.array(y)) * np.log(1 - np.array(y_hat))) / output_size
        return loss
