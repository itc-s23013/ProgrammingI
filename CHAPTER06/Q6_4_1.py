import random
random.seed(1)
msgs = ["hi", "hello", "see you",]
with open("some.txt", "w") as f:
    for i in range(100000):
        f.write("{}, {}\n".format(i, random.choice(msgs))
