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
