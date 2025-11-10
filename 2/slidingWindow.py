
def main():
    num, window = map(int, input().split())
    nums = list(map(int, input().split()))

    current_sum = sum(nums[:window])
    max_sum = current_sum
    
    for i in range(window, num):
        current_sum += nums[i] - nums[i-window] 
        if current_sum > max_sum:
            max_sum = current_sum

    print(round(max_sum / window, 2))

if __name__ == "__main__":
    main()
