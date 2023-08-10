# не изменяемые типы данных
a: int = 0
b: str = 'dd'
c: float = 1.2
d: bool = True
e: None = None
f: tuple = (1, 2, b)  # не изменяемый список (типа массив)
g: set = {1, 2}  # не изменяемый список уникальных данных

# изменяемые типы данных
h: list = [1, 'ghj', 2, 1]  # типа массив изменяемый
i: dict = {1: 2, 2: 'ghg'}  # список ключ-значение

if __name__ == '__main__':
    list_to_tuple = tuple(h)
    print(list_to_tuple)

    list_to_set = set(h)
    print(list_to_set)

    list_to_set.clear()  # очистить список set

    list_to_set.add('ghjh')  # добавить в список set
    print(list_to_set)

    h.append([5, 1])  # добавить в список list данные (можно доб. еще один список)
    print(h)

    h.extend(list_to_tuple)  # доб в базовый список данные из другого списка (можно добавить только из tuple, set, list)
    print(h)

    list_pop = h.pop(2)  # возвращает значение из списка по индексу и удаляет это значение оттуда
    print(list_pop)
    print(h)

    list_get = h[3]  # получить значение из списка по индексу без удаления
    print(list_get)
    print(h)

    dict_get = i.get(3, 'нет значения')  # получение значения из словаря по ключу даже если нет ключа
    # (принимает 2 аргумента, если нет ключа можно задать возвращаемое значение)
    print(dict_get)

    dict_get_2 = i[1]  # получение значения из словаря если ключ существует (если ключа нет будет ошибка)
    print(dict_get_2)

    print(i)
    i['key'] = 6  # добавляет ключ и значение в словарь
    print(i)
    i[1] = 55  # обновится значение под ключем 1
    print(i)

    print(i)
    i.update(key2=8, key3=65)  # добавляет несколько значений в словарь (пишется без пробелов перед и после =)
    print(i)

    all_keys = i.keys()  # получить все ключи из словаря
    print(all_keys)

    all_values = i.values()  # получить все значения из словаря
    print(all_values)

    all_items = i.items()  # получить и ключи и значения из словаря
    print(all_items)



