# DZ-25. Список учеников

lst = []
file = open('DZ_25.txt', encoding='utf-8')
for line in file.readlines():
    lst.append(line.split())
file.close()

# Пересавляем местами Фамилия, Имя
for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j], lst[i][j + 1] = lst[i][j + 1], list(lst[i][j])
        surname = lst[i][j]
        name = lst[i][j + 1]
        for letter in range(len(name)):
            name = name[letter] + '.'
            lst[i][j + 1] = name
            break
        break

# Изменяем оценки на средний бал ученика
sred_bal = 0
sum = 0
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if j >= 2:
            lst[i][j] = int(lst[i][j])
            sum += lst[i][j]
    sred_bal = round((sum / len(lst[i][2:])), 2)
    sum = 0
    del lst[i][2:]
    lst[i].append(sred_bal)

# Расчитываем средний бал класса
sred_bal_clas = 0
for i in range(len(lst)):
    sred_bal_clas += lst[i][2]
sred_bal_clas = ['Средний бал класса: ', round((sred_bal_clas / len(lst)), 2)]

# Оставляем только тех учеников у кого средний бал меньше 5
lst_new = []
for i in range(len(lst)):
    if lst[i][2] < 5:
        lst_new.append(lst[i])
lst_new.append(sred_bal_clas)

# Вывод
for i in range(len(lst_new)):
    for j in range(len(lst_new[i])):
        if len(lst_new[i]) == 3:
            lst_new[i][j] = lst_new[i][j] + ' ' + lst_new[i][j + 1]
            del lst_new[i][j + 1]
        break
    print('{:<25}'.format(lst_new[i][0]), lst_new[i][1])
    lst_new[i] = '{:<25}'.format(lst_new[i][0]) + str(lst_new[i][1])
print()

file = open('sred_bal.txt', 'w', encoding='utf-8')
for line in lst_new:
    file.write(line)
    file.write('\n')
file.close()