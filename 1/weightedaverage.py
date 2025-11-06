
def main():
    n = int(input().strip())
    scores = list(map(int, input().split()))
    weights = list(map(int, input().split()))

    print(round(sum(score * weight for score, weight in zip(scores, weights)) / sum(weights)))
    

if __name__ == "__main__":
    main() 
