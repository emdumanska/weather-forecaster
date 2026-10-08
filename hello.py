import numpy as np
def greet(name):
    return f"Hello, {name}! Welcome to AI Club!"


def demonstrate_numpy():
    numbers = np.array([1, 2, 3, 4, 5])

    print(f"Array: {numbers}")
    print(f"Mean: {numbers.mean()}")
    print(f"Sum: {numbers.sum()}")
    print(f"Standard Deviation: {numbers.std():.2f}")

    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"Matrix:\n{matrix}")
    print(f"Matrix shape: {matrix.shape}")


def main():
    user_name = input("What's your name? ")
    message = greet(user_name)
    print(message)
    demonstrate_numpy()

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"{num1} + {num2} = {num1 + num2}")

if __name__ == "__main__":
    main()
