def find_common_participants(group1, group2, delimiter=','):

    group1_participants = group1.split(delimiter)
    group2_participants = group2.split(delimiter)

    common_participants = list(set(group1_participants).intersection(group2_participants))

    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
participants_intersection = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print(participants_intersection)
