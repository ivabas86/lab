# TODO решите задачу
import json
from idlelib.iomenu import encoding

FILE ='input.json'
def task() -> float:
    with open(FILE, 'r', encoding = 'utf-8') as f:
        file = json.load(f)
        sum_ = sum(i['score']*i['weight'] for i in file)
    return round(sum_,3)
if __name__ == '__main__':
    print(task())
