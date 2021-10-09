import numpy as np
from scipy.special import factorial
import matplotlib.pyplot as plt


def poisson(lambda_, N):
    if lambda_ < 0:
        raise IOError("Лямбда меньше 0")
    n = np.arange(0, N + 1)
    e = np.exp(1)
    p = (lambda_ ** n) * (e ** (-lambda_)) / factorial(n)
    return np.array([n, p])


def moment(arr, k):
    if not isinstance(arr, np.ndarray) or not isinstance(k, int) or k < 0:
        raise IOError("Неправильные значения на вход для момента")
    return np.sum(arr[0] ** k * arr[1])


def expected_value(arr):
    if not isinstance(arr, np.ndarray):
        raise IOError("Неправильные значения на вход для мат ожидания")
    return moment(arr, 1)


def dispersion(arr):
    if not isinstance(arr, np.ndarray):
        raise IOError("Неправильные значения на вход для дисперсии")
    arr[0] = (arr[0] - expected_value(arr)) ** 2
    return expected_value(arr)


if __name__ == '__main__':
    lambda_ = 3
    N = 333
    k = 2
    p = poisson(lambda_, N)
    average_expected_value_fan = expected_value(p)
    average_dispersion_enjoyer = dispersion(p)
    # print(moment(p, k))
    # print(average_expected_value_fan)
    # print(average_dispersion_enjoyer)
    assert np.allclose([average_expected_value_fan,
                        average_dispersion_enjoyer], [lambda_, lambda_], 1e-3)
    plt.plot(p[1])
    plt.xlim(-1,50)
