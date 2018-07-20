def main():
    year = int(input())
    print(is_leap(year))


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    return False


if __name__ == '__main__':
    main()
