from pprint import pprint

def get_shop_list_by_dishes(dishes, person_count):
    ingr = {}
    f = {}
    d = dishes
    for items in range(len(d)):
        for i in range(len(cook_book[d[items]])):
            if cook_book[d[items]][i]['ingredient_name'] in ingr.keys():
                ingr[cook_book[d[items]][i]['ingredient_name']]['quantity'] = ingr[cook_book[d[items]][i]['ingredient_name']]['quantity'] + int(cook_book[d[items]][i]['quantity']) * person_count
            else:
                list_data = {}
                list_data['quantity'] = int(cook_book[d[items]][i]['quantity']) * person_count
                list_data['measure'] = cook_book[d[items]][i]['measure']
                ingr[cook_book[d[items]][i]['ingredient_name']] = list_data
    pprint(ingr)

def calc_dishes(for_input_1, cont):
    print(f'Введите цифры через "," чтобы определить список блюд для второго задания или 0 для выхода')
    print(' '.join(str(i) for i in for_input_1.items()))
    dishes = input().split(',')

    if int(dishes[0]) == 0:
        exit('спасибо, до свидания')
        cont = 1
    d = []
    for i in range(len(dishes)):
        if int(dishes[i]) not in for_input_1:
            print(f'нет такого блюда c номером {dishes[i]}, попробуйте еще раз' + '\n')
            return cont
        d.append(for_input_1[int(dishes[i])])
    cont = 1

    print('Введите кол-во гостей')
    guests = input()
    if guests.isdigit() == True:
        guests = int(guests)
        get_shop_list_by_dishes(d, guests)
    else:
        print('Введите в следующий раз числовое значение')
        cont = 0
        return cont

    return cont

#выполнение первого задания
with open('spec.txt', 'r', encoding='utf8') as f:
    cook_book = {}
    list_1 = {}
    for line in f:
        total_list = []
        s = line.strip()
        i = int(f.readline().strip())
        for item in range(i):
            list_1['ingredient_name'], list_1['quantity'], list_1['measure'] = f.readline().strip().split('|')
            total_list.append(list_1.copy())
        f.readline()
        cook_book[s] = total_list
pprint(cook_book)

# выполнение второго задания
for_input = {}
x = 1
for data in cook_book.keys():
    for_input[x] = data
    x += 1
print('')

counter = 0
while counter == 0:
    counter = calc_dishes(for_input, counter)


