def create_adder_function():
    def adder(a, b):
        return a + b

    return adder


my_adder = create_adder_function()

result = my_adder(5, 10)
print(result)  # 出力: 15
