# задача 1
recipes = []
with open(r'C:\Users\Olesya.Dzhafarova\PycharmProjects\projects2\logs\data.txt', 'rt', encoding='UTF') as file:
    for dish in file:
        dish_name = dish.strip()
        cook_book = {dish_name: []}
        quantity_ingredient_count = file.readline()
        for item in range(int(quantity_ingredient_count)):
            emp = file.readline()
            ingredient_name, quantity, measure = emp.strip().split(' | ')
            cook_book[dish_name].append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        blank_line = file.readline()
        recipes.append(cook_book)
        print(cook_book)




# задача 3
outputfile = 'output.txt'
file1 = r'C:\Users\Olesya.Dzhafarova\PycharmProjects\projects2\1.txt'
file2 = r'C:\Users\Olesya.Dzhafarova\PycharmProjects\projects2\2.txt'
file3 = r'C:\Users\Olesya.Dzhafarova\PycharmProjects\projects2\3.txt'
myfile = open(outputfile, mode='w', encoding='utf-8')
def num_of_lines(*files):
    count = {}
    for file in files:
        with open(file, mode='r', encoding='utf-8') as f:
            count.update({file[-5:] : (len(f.readlines()))})
    files2 = {}
    for i in sorted(count, key=count.get, reverse=True):
        files2[i] = count[i]
    print(files2)
    for key, value in files2.items():
        myfile.write(f'Даны файлы: {key} \n')
        myfile.write(f'Количество строк: {value}, файл номер: {key}\n')
    return
num_of_lines(file1, file2, file3)
