if __name__ == '__main__':
    for i in range(3):
        print(f'hello world {i+1}')

    names = ['Nastiya', 'Eva', 'Sasha']
    for name in names:
        print(name)

    for i in range(len(names)):  # при такой записи можно удалить или добавить значения в список
        print(names[i])

    for i, name in enumerate(names):
        print(i+1, name)

    k = 0
    while(k < 3):
        k += 1
        print(1)

    nastiya = {'name': 'nastiya', 'age': '28', 'city': 'paphos'}
    print(f'Hello I {nastiya["name"]} I {nastiya["age"]} old. I am from {nastiya["city"]}.')
    for key, value in nastiya.items():
        if key == "name":
            print(f'Hello I am  {value}')
        elif key == 'age':
            print(f'I {value} old')
        else:
            print(f'I am from {value}')
