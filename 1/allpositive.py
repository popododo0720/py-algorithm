
def main():
    nums = list(map(int, input().split()))
    print("YES" if all(x>0 for x in nums) else "NO")

if __name__ == "__main__":
    main() 
