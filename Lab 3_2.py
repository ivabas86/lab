# TODO Напишите функцию find_common_participants
def find_common_participants(first_group,first_group_2, sep = ','):
    p1 = first_group.split(sep)
    p2 = first_group_2.split(sep)
    return sorted(set(p1).intersection(p2))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group,participants_second_group, sep= '|'))