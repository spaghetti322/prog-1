import numpy as np
from scipy.special import factorial
import matplotlib.pyplot as plt


def poisson(lambda_, N):
    if lambda_ < 0:
        raise IOError("Лямбда меньше 0")
    n = np.arange(0, N+1)
    e = np.exp(1)
    return (lambda_**n)*(e**(-lambda_))/factorial(n)


def moment(arr, k):
    if not isinstance(arr, np.ndarray) or not isinstance(k, int):
        raise IOError("Неправильные значения на вход")
    m = arr[0:k]
    m_index = np.arange(0, k)
    return np.sum(m*m_index)


def expected_value(arr):
    if not isinstance(arr, np.ndarray):
        raise IOError("Неправильные значения на вход")
    return moment(arr, (arr.size))


def dispersion(arr):
    if not isinstance(arr, np.ndarray):
        raise IOError("Неправильные значения на вход")
    mid = expected_value(arr)
    ff = (arr-mid)**2
    f = expected_value(ff)
    return f


test_k = 111
test_p = poisson(3, test_k)
# print(test_p)
print(moment(test_p, 2))
print(expected_value(test_p))
print(dispersion(test_p))
plt.plot(test_p)
plt.show()
