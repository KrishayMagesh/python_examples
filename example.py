def sample_table(n):
    """Function to print a multiplication table for a given number."""
    print(f"Multiplication table for {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

sample_table(45)