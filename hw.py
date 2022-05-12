import random
import time
from numba import jit


class Timer:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def time1(self):
        self.t1 = time.time()

    def time2(self):
        self.t2 = time.time()
        return self.t2 - self.t1


class FindEuler:

    def __init__(self):
        self.sumOfI = 0
        self.run_amount = 0

    def generate_capsules(self, n):
        (self.sumOfI, self.run_amount) = self.generate_capsules_static(n)

    @staticmethod
    @jit(nopython=True, nogil=True)
    def generate_capsules_static(n):
        sumOfI = 0
        run_amount = 0
        elements = []
        for _ in range(n):
            sumOfNumbers = 0
            i = 0
            while sumOfNumbers <= 1:
                x = random.uniform(0, 1)
                elements.append(x)
                sumOfNumbers += x
                i += 1
            run_amount += 1
            sumOfI = sumOfI + i
        return sumOfI, run_amount
