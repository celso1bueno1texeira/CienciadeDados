def soma_n(n):
    return n * (n + 1) // 2

def main():
    n = int(input())
    result = soma_n(n)
    print(result)

if __name__ == "__main__":
    main()