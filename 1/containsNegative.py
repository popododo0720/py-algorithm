
def main():
    inputs = list(map(int, input().split()))
    print("OK" if all(x >= 0 for x in inputs) else "WARNING")


if __name__ == "__main__":
    main() 
