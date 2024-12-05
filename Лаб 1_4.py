users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений длину от общего либо уникального
poseshenie = { 'Общее количество': 0, 'Уникальные посещения': 0}
poseshenie['Общее количество'] = len(users)
poseshenie['Уникальные посещения'] = len(set(users))
print(poseshenie)