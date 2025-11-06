
def main():
    [print(w) for w in sorted(set(map(str, input().split())), key = lambda x: (len(x), x))]


if __name__ == "__main__":
    main() 
