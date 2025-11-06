
def main():
    n = int(input().strip())
    meetings = [tuple(map(int, input().split())) for _ in range(n)]
    meetings.sort(key=lambda x:  (x[1], x[0]))

    result = []
    last_end = 0

    for start, end in meetings:
        if start >= last_end:
            result.append((start, end))
            last_end = end
    for s, e in result:
        print(s, e)

if __name__ == "__main__":
    main()
