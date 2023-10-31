def main():
    yell("This", "is", "CS50")


def yell(*words):
    # upper_cased = map(str.upper, words)
    upper_cased = [word.upper() for word in words]
    print(*upper_cased)


if __name__ == '__main__':
    main()
