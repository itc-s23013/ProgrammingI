import random


def generate_random_number():
    digits = random.sample(range(10), 4)
    return "".join(str(d) for d in digits)


def check_matching(target_number, guess):
    if sorted(target_number) == sorted(guess):
        return guess
    else:
        return "x"


def main():
    target_number = generate_random_number()
    print("４桁の数字を当ててください！")

    while True:
        guess = input("数字を入力してください: ")

        if guess == target_number:
            print("正解です！")
            break
        else:
            matching_result = check_matching(target_number, guess)
            print(matching_result)


if __name__ == "__main__":
    main()
