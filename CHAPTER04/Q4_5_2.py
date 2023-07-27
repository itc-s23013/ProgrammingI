def parse_coord(coord_str):
    return list(map(float, coord_str.split(",")))


# 元の文字列リスト
s_coordi_list = ["1.0,2.2,3.5", "2.1,3.2,5.5", "1.2,1.3,2.2", "2.1,3.1,4.5"]

# mapを使って数値リストのリストに変換
f_coordi_list = list(map(parse_coord, s_coordi_list))

# 結果を表示
print(f_coordi_list)
