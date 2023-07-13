import random


def generate_random_number():
    digits = [str(i) for i in range(10)]
    random.shuffle(digits)
    return "".join(digits[:4])


def main():
    target_number = generate_random_number()
    print("４桁の数字を当ててください！")

    while True:
        guess = input("数字を入力してください: ")

        if guess == target_number:
            print("正解です！")
            break
        else:
            print("不正解です。もう一度挑戦してください。")


if __name__ == "__main__":
    main()
