def find_common_participants(group1, group2, separator=','):

    #Разделим строки на списки участников
    group1_participants = group1.split(separator)
    group2_participants = group2.split(separator)

    #Пересечение
    common_participants = list(set(group1_participants).intersection(group2_participants))

    #Сортировка в алфавитном порядке
    common_participants.sort()

    #Список общих участников
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
participants_intersection = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(participants_intersection)
