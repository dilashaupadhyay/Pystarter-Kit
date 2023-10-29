def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence

number_of_terms = int(input("Enter the number of terms: "))
result = fibonacci(number_of_terms)
print(f"The Fibonacci sequence up to {number_of_terms} terms is: {result}")
