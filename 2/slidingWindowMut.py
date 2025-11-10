

def main():
    num, k = map(int, input().split())
    nums = list(map(int, input().split()))

    l = 0
    current_sum = 0
    max_len = 0

    for r in range(num):
        current_sum += nums[r]

        while current_sum > k and l <= r:
            current_sum -= nums[l]
            l += 1

        if current_sum <= k:
            max_len = max(max_len, r - l + 1)

    print(max_len)

if __name__ == "__main__":
    main()

