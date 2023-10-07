import time
import unittest

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"TACKO TIMEEE {func.__name__}: {execution_time} sec.")
        return result
    return wrapper

def some_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

measured_function = measure_time(some_function)


class TestMeasureTimeDecorator(unittest.TestCase):

    def test_measure_time_decorator(self):
        n = 10000000
        result = measured_function(n)
        self.assertIsInstance(result, int)

if __name__ == "__main__":
    unittest.main()