# 単一の数値を文字列に変換する場合
num = 123
str_num = str(num)
print(str_num)  # 出力: "123"
print(type(str_num))  # 出力: <class 'str'>

# 複数の数値を文字列に変換する場合（map()関数を使用）
nums = [1, 2, 3, 4, 5]
str_nums = list(map(str, nums))
print(str_nums)  # 出力: ["1", "2", "3", "4", "5"]
print(type(str_nums[0]))  # 出力: <class 'str'>

