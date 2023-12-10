result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a має бути меншим за b")
        if b == 0:
            raise ZeroDivisionError("b не має = 0")
        if b > 100:
            raise IndexError("b має бути більшим за 100")

        return a / b
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    except IndexError as e:
        print(f"IndexError: {e}")


data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)


print(result)