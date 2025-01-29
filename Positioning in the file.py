def custom_write(file_name, strings : list):
    name = file_name
    file = open(name, 'a', encoding = 'utf-8')
    d = {}
    for i in range(len(strings)):
        t = file.tell()
        file.write(strings[i])
        file.write('\n')
        d[(i +1, t)] =  strings[i]
    file.close()
    return d


info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

    ]



result = custom_write('test.txt', info)
#print(custom_write('test.txt', info))
for elem in result.items():
  print(elem)
