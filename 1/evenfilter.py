
def main():
    num = int(input().strip())
    nums = list(map(int, input().split()))
    even = [x for x in nums if x % 2 == 0]
    print(*sorted(even))

if __name__ == "__main__":
    main() 
