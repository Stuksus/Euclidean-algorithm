#!/usr/bin/env python
# coding: utf-8


def gcd(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    return gcd(b % a, a)


def main():
    a, b = map(int, input("Введите 2 числа через пробел: ").split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
