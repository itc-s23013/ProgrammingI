def func_square(*gurara):
    results = []
    for n in gurara:
        results.append(n * n)
    return results


numbers = [1, 2, 3, 4]
print(func_square(*list(range(100))))
