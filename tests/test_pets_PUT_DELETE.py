import json
import os
from apiquery.settings import valid_email, valid_password
from apiquery.api import PetFriends
import time  # для вывода времени выполнения теста: time_test

pf = PetFriends()

def test_add_new_pet(name='King-Kong', animal_type='Monkey', age='3', pet_photo=r'../images/king-kong2.jpg'):
    """Cоздадим питомца для последующих тестов..."""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'w', encoding='utf8') as write:
        write.write('\ntest_1_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')


def test_1_update_pet_info(name='Ping-Pong', animal_type='Gorila/Monkey', age='190'):
    """Позитивный. Проверяем возможность обновления информации о питомце при валидных значениях - PASSED"""

    start = time.monotonic_ns()
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Если список не пустой, то пробуем обновить у первого питомца его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result, content, optional = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        with open("out_json.json", 'a', encoding='utf8') as write:
            write.write('\ntest_1_update_pet_info:\n')
            json.dump(result, write, ensure_ascii=False, indent=4)
        print('\nContent:', content)
        print('Optional:', optional)
        finish = time.monotonic_ns()  # засекаем таймер после выполнения теста...
        time_test = (finish - start) // 1000000
        print(f"Время выполнения теста: {time_test} млсек.")

        # Проверяем статус ответа и что тело запроса соответствует заданному
        assert status == 200
        assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
        assert time_test < 1000
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets!")


def test_2_update_pet_info(name='Ping-Pong', animal_type='Gorila/Monkey', age='190'):
    """Негативный. pet_id - пустое значение - PASSED"""
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Если список не пустой, то пробуем обновить у первого питомца его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result, content, optional = pf.update_pet_info(auth_key, "", name, animal_type, age)
        with open("out_json.json", 'a', encoding='utf8') as write:
            write.write('\ntest_2_update_pet_info:\n')
            json.dump(result, write, ensure_ascii=False, indent=4)
        print('\nContent:', content)
        print('Optional:', optional)
        # Проверяем статус ответа и что тело запроса соответствует заданному
        assert status == 404
        #assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets!")


def test_3_update_pet_info(name='Ping-Pong', animal_type='Gorila', age='107'):
    """Негативный. pet_id - несуществующее значение - PASSED"""
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = 'd0beaa62-bd71-4b20-a0e9-a743184fafaV'
    # Если список не пустой, то пробуем обновить у первого питомца его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result, content, optional = pf.update_pet_info(auth_key, pet_id, name, animal_type, age)
        with open("out_json.json", 'a', encoding='utf8') as write:
            write.write('\ntest_3_update_pet_info:\n')
            json.dump(result, write, ensure_ascii=False, indent=4)
        print('\nContent:', content)
        print('Optional:', optional)
        # Проверяем статус ответа и что тело запроса соответствует заданному
        assert status == 400
        #assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets!")


def test_4_update_pet_info(name='Ping-Pong', animal_type='Gorila', age='107'):
    """Негативный. Auth_key - пустое значение - PASSED"""
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    auth_key = {'key': ''}
    # Если список не пустой, то пробуем обновить у первого питомца его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result, content, optional = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        with open("out_json.json", 'a', encoding='utf8') as write:
            write.write('\ntest_4_update_pet_info:\n')
            json.dump(result, write, ensure_ascii=False, indent=4)
        print('\nContent:', content)
        print('Optional:', optional)
        # Проверяем статус ответа и что тело запроса соответствует заданному
        assert status == 403
        #assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets!")


def test_5_update_pet_info(name='Ping-Pong', animal_type='Gorila', age='107'):
    """Негативный. Auth_key - Валидный ключ без последнего символа - PASSED"""
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    auth_key = {'key': 'f5b1037b3374bd1e3d195bdadb6a93e2ea8c299aa89e6d4658ebf6c'}
    # Если список не пустой, то пробуем обновить у первого питомца его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result, content, optional = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        with open("out_json.json", 'a', encoding='utf8') as write:
            write.write('\ntest_5_update_pet_info:\n')
            json.dump(result, write, ensure_ascii=False, indent=4)
        print('\nContent:', content)
        print('Optional:', optional)
        # Проверяем статус ответа и что тело запроса соответствует заданному
        assert status == 403
        #assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets!")


def test_6_update_pet_info(name='', animal_type='Gorila', age='115'):
    """Негативный. name - пустое значение - PASSED"""
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Если список не пустой, то пробуем обновить у первого питомца его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result, content, optional = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        with open("out_json.json", 'a', encoding='utf8') as write:
            write.write('\ntest_6_update_pet_info:\n')
            json.dump(result, write, ensure_ascii=False, indent=4)
        print('\nContent:', content)
        print('Optional:', optional)
        # Проверяем статус ответа и что тело запроса соответствует заданному
        assert status == 200
        assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets!")


def test_7_update_pet_info(name='Kongs', animal_type='', age='115'):
    """Негативный. animal_type - пустое значение - PASSED"""
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Если список не пустой, то пробуем обновить у первого питомца его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result, content, optional = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        with open("out_json.json", 'a', encoding='utf8') as write:
            write.write('\ntest_7_update_pet_info:\n')
            json.dump(result, write, ensure_ascii=False, indent=4)
        print('\nContent:', content)
        print('Optional:', optional)
        # Проверяем статус ответа и что тело запроса соответствует заданному
        assert status == 200
        assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets!")


def test_8_update_pet_info(name='Ping', animal_type='Gorila', age='九十'):
    """Негативный. Age - Китайские иероглифы - PASSED"""
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Если список не пустой, то пробуем обновить у первого питомца его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result, content, optional = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        with open("out_json.json", 'a', encoding='utf8') as write:
            write.write('\ntest_8_update_pet_info:\n')
            json.dump(result, write, ensure_ascii=False, indent=4)
        print('\nContent:', content)
        print('Optional:', optional)
        # Проверяем статус ответа и что тело запроса соответствует заданному
        assert status == 200
        assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets!")


def test_9_update_pet_info(name='', animal_type='', age=''):
    """Негативный. Проверка без параметров - PASSED"""
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Если список не пустой, то пробуем обновить у первого питомца его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result, content, optional = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        with open("out_json.json", 'a', encoding='utf8') as write:
            write.write('\ntest_9_update_pet_info:\n')
            json.dump(result, write, ensure_ascii=False, indent=4)
        print('\nContent:', content)
        print('Optional:', optional)
        # Проверяем статус ответа и что тело запроса соответствует заданному
        assert status == 200
        #assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets!")


def test_10_update_pet_info(name='Ding', animal_type='Gorge', age='88'):
    """Негативный. Проверка без параметров - PASSED"""
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Если список не пустой, то пробуем обновить у первого питомца его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result, content, optional = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        with open("out_json.json", 'a', encoding='utf8') as write:
            write.write('\ntest_10_update_pet_info:\n')
            json.dump(result, write, ensure_ascii=False, indent=4)
        print('\nContent:', content)
        print('Optional:', optional)
        # Проверяем статус ответа и что тело запроса соответствует заданному
        assert status == 200
        assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
        assert optional.get('auth_key') == auth_key.get('key')
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets!")




"""DELETE TESTING"""

def test_1_delete_all_pets():
    """Позитивный. Проверяем возможность удаления питомца - PASSED"""
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "King-Kong", "Gorila", "133", r'../images/king-kong2.jpg')
        _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, my_pets, content, optional = pf.delete_pet(auth_key, pet_id)
    # Ещё раз запрашиваем список своих питомцев
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_1_update_pet_info:\n')
        json.dump(my_pets, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_2_delete_all_pets():
    """Негативный. pet_id - пустое - PASSED"""
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "King-Kong", "Gorila", "133", r'../images/king-kong2.jpg')
        _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = ""
    status, my_pets, content, optional = pf.delete_pet(auth_key, pet_id)
    # Ещё раз запрашиваем список своих питомцев
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_2_update_pet_info:\n')
        json.dump(my_pets, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 404
    assert pet_id not in my_pets.values()


def test_3_delete_all_pets():
    """Негативный. pet_id - не существует - PASSED"""
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "King-Kong", "Gorila", "133", r'../images/king-kong2.jpg')
        _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = "e0614948-3593-4fa3-a250-8b515adfab6589"
    status, my_pets, content, optional = pf.delete_pet(auth_key, pet_id)
    # Ещё раз запрашиваем список своих питомцев
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_3_update_pet_info:\n')
        json.dump(my_pets, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_4_delete_all_pets():
    """Негативный. auth_key - пустое - PASSED"""
    #_, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    auth_key = {'key': ''}
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "King-Kong", "Gorila", "133", r'../images/king-kong2.jpg')
        _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, my_pets, content, optional = pf.delete_pet(auth_key, pet_id)
    # Ещё раз запрашиваем список своих питомцев
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_4_update_pet_info:\n')
        json.dump(my_pets, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_5_delete_all_pets():
    """Негативный. auth_key - заменить одну лат букву е на кириллицу е - PASSED"""
    #_, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    auth_key = {'key': 'f5b1037b3374bd1e3d195bdadb6a93e2ea8c299aa89e6d4658еbf6c0'}
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "King-Kong", "Gorila", "133", r'../images/king-kong2.jpg')
        _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, my_pets, content, optional = pf.delete_pet(auth_key, pet_id)
    # Ещё раз запрашиваем список своих питомцев
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_5_update_pet_info:\n')
        json.dump(my_pets, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_6_delete_all_pets():
    """Негативный. пустые параметры - FAILED"""
    auth_key = {'key': ''}
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "King-Kong", "Gorila", "133", r'../images/king-kong2.jpg')
        _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = ''
    status, my_pets, content, optional = pf.delete_pet(auth_key, pet_id)
    # Ещё раз запрашиваем список своих питомцев
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_6_update_pet_info:\n')
        json.dump(my_pets, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_7_delete_all_pets():
    """Позитивный. Проверяем возможность удаления питомца с числом в ключе - PASSED"""
    auth_key = {'key': 11111111111111111111111111111111111111111111111111111111}
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "King-Kong", "Gorila", "133", r'../images/king-kong2.jpg')
        _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, my_pets, content, optional = pf.delete_pet(auth_key, pet_id)
    # Ещё раз запрашиваем список своих питомцев
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_7_update_pet_info:\n')
        json.dump(my_pets, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_8_delete_all_pets():
    """Позитивный. Проверка времени удаления макс. кол-ва питомцев в пределах 1 сек. - PASSED"""

    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Удалим всех питомцев для чистоты эксперимента и добавим 4 новых:
    for id_pet in my_pets["pets"]:
        pf.delete_pet(auth_key, id_pet["id"])
    pf.add_new_pet(auth_key, "King-Kong1", "Gorila1", "133", r'../images/king-kong1.jpg')
    pf.add_new_pet(auth_key, "King-Kong2", "Gorila2", "144", r'../images/king-kong2.jpg')
    pf.add_new_pet(auth_key, "King-Kong3", "Gorila3", "155", r'../images/king-kong3.jpg')
    pf.add_new_pet(auth_key, "King-Kong4", "Gorila4", "188", r'../images/king-kong3.jpg')
    # Засекаем время и производим операцию удаления:
    start = time.monotonic_ns()
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    for id_pet in my_pets["pets"]:
        pf.delete_pet(auth_key, id_pet["id"])
    _, my_pets, content, optional = pf.get_list_of_pets(auth_key, "my_pets")
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_8_update_pet_info:\n')
        json.dump(my_pets, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    status, my_pets, content, optional = pf.get_list_of_pets(auth_key, "my_pets")
    finish = time.monotonic_ns()
    time_test = (finish - start) // 1000000
    print(f"Время выполнения теста: {time_test} млсек.")
    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()
    assert time_test < 1000




"""ТЕХНИЧЕСКИЕ КОДЫ:"""


# def test_delete_all_pets():
#     """Удаляем всех питомцев"""
#     # Получаем ключ auth_key и запрашиваем список своих питомцев
#     _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
#     _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
#
#     pet_id = my_pets['pets'][0]['id']
#     # Получаем в цикле id всех питомцев из списка и отправляем запрос на удаление:
#     for id_pet in my_pets["pets"]:
#         pf.delete_pet(auth_key, id_pet["id"])
#     # Ещё раз запрашиваем список своих питомцев
#     status, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
#
#     assert status == 200
#     assert pet_id not in my_pets.values()