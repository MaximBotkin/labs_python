def find_common_participants(first_group, second_group, delimeter=','):
    result = []
    first_group = first_group.split(delimeter)
    second_group = second_group.split(delimeter)
    for person in first_group:
        if person in second_group:
            result.append(person)
    return sorted(result)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
