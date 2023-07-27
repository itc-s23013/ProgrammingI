from datetime import datetime, timedelta


def classify_days(days=0):
    # 現在の日付を取得
    today = datetime.today().date()

    # 指定された日数だけ加算または減算して目的の日付を求める
    target_date = today + timedelta(days=days)

    # 目的の日付との差分を計算
    delta = target_date - today

    # 日付を分類
    if delta.days < 0:
        category = "昨日"
    elif delta.days == 0:
        category = "今日"
    elif delta.days == 1:
        category = "明日"
    else:
        category = "今日より1日を超えて離れた日"

    return category


# テスト
print(classify_days())  # 今日
print(classify_days(-1))  # 昨日
print(classify_days(1))  # 明日
print(classify_days(3))  # 今日より1日を超えて離れた日
