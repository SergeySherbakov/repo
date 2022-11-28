import csv


def import_data(data, sep=','):
    print(data)
    d = open('phone.csv', 'r')
    s = d.read()
    id = 1
    if s == '':
        id = 1
    else:
        for i in s:
            if i == '\n':
                id += 1
    d.close()

    with open('phone.csv', 'a+') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(str(id) + sep + sep.join(data))
            file.write(f"\n")
