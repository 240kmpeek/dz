result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a is less than b")
        if b > 100:
            raise IndexError("b is greater than 100")
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    except (ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Error: {e}")
        return None

data = {10: 2, 2: 5, "123": 4, 18: 0, "some_key": 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)