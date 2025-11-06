
def main():
    i = int(input().strip())

    words = []

    for j in range(i):
        words.append(input().strip())

    for word in sorted(words, key = lambda x: (len(x), x)):
        print(word)


if __name__ == "__main__":
    main() 
