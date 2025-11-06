
def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]

        seen[num] = i
    raise ValueError("No solution found")

if __name__ == "__main__":
    main()
