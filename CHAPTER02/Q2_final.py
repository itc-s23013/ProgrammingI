import random


def generate_random_alphabet():
    return random.choice("abcdefghijklmnopqrstuvwxyz")


def main():
    while True:
        alphabet = generate_random_alphabet()
        print(alphabet)

        if alphabet.lower() == "e":
            break


if __name__ == "__main__":
    main()
