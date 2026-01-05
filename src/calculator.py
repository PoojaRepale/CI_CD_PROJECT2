def add(a,b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a , b):
    if b == 0:
        raise ValueError("can't divide by zero")
    return a / b

if __name__ == "__main__":
    print("Addition:",add(10, 5))
    print("Substract:",substract(10, 5))
    print("Multiplication:",multiply(10, 5))
    print("Division:",divide(10, 5))
    
    