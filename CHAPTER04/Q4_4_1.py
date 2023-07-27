vote_num = 0


def vote():
    global vote_num
    vote_num += 1


def reset_box():
    global vote_num
    vote_num = 0


def check_box():
    print("投票箱の中の票数：", vote_num)
