
def is_valid(s: str) -> bool:
    pairs = {'(':')', '[':']', '{':'}'}

    stack = []

    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return False

    return not stack

def main():
    input = "({[])"
    print(is_valid(input))

if __name__ == "__main__":
    main()
