def febonic_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    series = [0, 1]
    for i in range(2, n):
        next_value = series[i - 1] + series[i - 2]
        series.append(next_value)
    
    return series

# Example usage
if __name__ == "__main__":
    n = 10  # Change this value to generate a longer or shorter series
    fib_series = febonic_series(n)
    print(f"Fibonacci series of length {n}: {fib_series}")