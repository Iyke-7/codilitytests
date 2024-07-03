def solution(n):
    b = bin(n)[2:]
    b = b.strip("0")
    l = b.split("1")
    print(b)
    return len(max(l, key=len))
    
def main():
    try:
        n = int(input("Enter an integer: "))
        result = solution(n)
        print(f"The maximum number of consecutive zeros surrounded by ones in the binary representation of {n} is {result}")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == '__main__':
    main()