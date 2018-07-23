def main():
    n = int(input())    # This line is useless, but required by the challenge.
    scores = map(int, input().split())
    scores = set(scores)
    scores = sorted(scores)
    print(scores[-2])


if __name__ == '__main__':
    main()
