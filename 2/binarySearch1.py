from bisect import bisect_left


def main():
    _ = int(input().strip())
    nums = list(map(int, input().split()))
    target = int(input().strip())
    idx = bisect_left(nums, target)
    print("FOUND" if idx < len(nums) and nums[idx] == target else "NOT FOUND")
                
if __name__ == "__main__":
    main()
