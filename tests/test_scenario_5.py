import json
import os
from apiquery.settings import valid_email, valid_password
from apiquery.api import PetFriends

pf = PetFriends()

"""Test-Scenario 5. Создать питомца без фото, посмотреть список своих питомцев, всех удалить
и снова запросить информацию о наличии питомцев"""

def test_1_get_api_key_user(email=valid_email, password=valid_password):
    """Проверяем получение ключа и возвращаем сведения о введённых данных"""
    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'w', encoding='utf8') as write:
        write.write('test_1_get_api_key_user:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result
    assert optional.get('email') == valid_email
    assert optional.get('password') == valid_password


def test_2_add_pet_without_foto(name='King', animal_type='Monkey-Gorila', age='135'):
    """Проверяем создание нового питомца без фото"""
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet_nofoto(auth_key, name, animal_type, age)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_2_add_pet_without_foto:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert result.get('pet_photo') == ''


def test_3_delete_all_pets():
    """Удаляем всех питомцев"""
    # Получаем ключ auth_key и запрашиваем список питомцев пользователя:
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_3_delete_all_pets//list_of_pets:\n')
        json.dump(my_pets, write, ensure_ascii=False, indent=4)

    pet_id = my_pets['pets'][0]['id']
    # Получаем в цикле id всех питомцев из списка и отправляем запрос на удаление:
    for id_pet in my_pets["pets"]:
        pf.delete_pet(auth_key, id_pet["id"])
    # Ещё раз запрашиваем список питомцев:
    status, my_pets, content, optional = pf.get_list_of_pets(auth_key, "my_pets")
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_3_delete_all_pets:\n')
        json.dump(my_pets, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)

    assert status == 200
    assert pet_id not in my_pets.values()

