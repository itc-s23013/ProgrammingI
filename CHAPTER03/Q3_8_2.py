import pickle
with open('test1.pkI', 'rb') as f:
    result = pickle.load(f)
    print(result)
