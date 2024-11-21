# TODO импортировать необходимые модули
import json
import csv
import collections
from csv import DictReader
from idlelib.iomenu import encoding
from xml.etree.ElementTree import indent

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open (INPUT_FILENAME,'r', encoding = 'utf-8') as f:
        data_json = csv.DictReader(f)
        data = [i for i in data_json]
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f1:
        json.dump(data, f1, indent=4)
    ...  # TODO Сериализовать в файл с отступами равными 4



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
