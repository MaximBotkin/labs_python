import json


def task() -> float:
    sum = 0
    with open('input.json', 'r') as file:
        data = json.load(file)
        for values in data:
            sum += values['score'] * values['weight']
    return round(sum, 3)


print(task())
