
def main():
    n1 = [1, 2, 3, 0, 0, 0]
    m = 3
    n2 = [2, 5, 6]
    n = 3

    merge(n1, m, n2, n)

    print(n1)

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    pass

if __name__ == "__main__":
    main()
