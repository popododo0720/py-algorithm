
def main():
    i = input().strip()
    count = {}

    for a in i:
        count[a] = count.get(a, 0) + 1

    for char, counter in sorted(count.items()):
        print(f"{char}: {counter}")

if __name__ == "__main__":
    main() 
