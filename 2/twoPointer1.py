

def main():
    num = int(input().strip())
    nums = list(map(int, input().split()))
    target = int(input().strip())

    l = 0
    r = num - 1

    while l < r:
        current_sum = nums[l] + nums[r]
        if current_sum == target:
            print("YES")
            return
        elif current_sum > target:
            r -= 1
        else: 
            l += 1

    print("NO")

if __name__ == "__main__":
    main()
