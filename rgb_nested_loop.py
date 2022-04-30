#!/usr/bin/env python3
# Created by Marc Coffi
# Created in April 2022
# This program displays rgb colors up to 50


def main():
    for counter1 in range(51):
        for counter2 in range(51):
            for counter3 in range(51):
                print("({}, {}, {})".format(counter1, counter2, counter3))


if __name__ == "__main__":
    main()
