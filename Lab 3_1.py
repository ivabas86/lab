# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
def func (items_list_, item):
    for tovar in items_list_:
        if tovar == item:
            indx = items_list_.index(item)
            return indx

for find_item in ['банан', 'груша', 'персик']:
    index_item = func(items_list,find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
