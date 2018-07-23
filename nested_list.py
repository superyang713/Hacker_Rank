# dict could be used, but the point of this challenge is to use nested list.


def main():
    n = int(input())    # useless but required by the challenge
    data = []
    for _ in range(n):
        name = input()
        score = float(input())
        record = [name, score]
        data.append(record)

    data = sorted(data, key=lambda x: x[1])
    print(data[-1])


if __name__ == '__main__':
    main()
