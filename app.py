#!/usr/bin/env python3


def fizbazz(num):
    is_divisible = lambda divisor, num: num % divisor == 0

    if num == 0:
        return num

    if is_divisible(3, num) and is_divisible(5, num):
        return "fizbazz"

    if is_divisible(3, num):
        return "fiz"

    if is_divisible(5, num):
        return "bazz"

    return num


def main():
    for i in range(0, 31):
        result = fizbazz(i)
        print(f"{i}: {result}")


if __name__ == "__main__":
    main()
