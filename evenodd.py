def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(even_or_odd(number))
