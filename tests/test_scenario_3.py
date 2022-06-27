import json
import os
from apiquery.settings import valid_email, valid_password
from apiquery.api import PetFriends

pf = PetFriends()

"""Test-Scenario 3. Создать двух питомцев (с фото и без) и получить список своих питомцев"""

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


def test_2_add_new_pet_photo(name='King-Kong-Live', animal_type='Monkey', age='5', pet_photo=r'../images/king-kong1.jpg'):
    """Проверяем создание нового питомца с фото"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_2_add_new_pet_photo:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)

    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')


def test_3_add_pet_without_foto(name='Kong-Live', animal_type='Monkey-Gorila', age='144'):
    """Проверяем создание нового питомца без фото"""
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet_nofoto(auth_key, name, animal_type, age)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_3_add_pet_without_foto:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert result.get('pet_photo') == ''


def test_4_get_user_pet_info(name='Ping-Pong', animal_type='Gorila/Monkey', age='188'):
    """Проверяем возможность получения списка питомцев пользователя"""
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    status, my_pets, content, optional = pf.get_list_of_pets(auth_key, "my_pets")
    # Если список не пустой, то выводим на печать:
    if len(my_pets['pets']) > 0:
        with open("out_json.json", 'a', encoding='utf8') as write:
            write.write('\ntest_4_get_user_pet_info:\n')
            json.dump(my_pets, write, ensure_ascii=False, indent=4)
        print('\nContent:', content)
        print('Optional:', optional)

        # Проверяем что статус ответа = 200 и список не пустой:
        assert status == 200
        assert len(my_pets['pets']) > 0
    else:
        # Если список пустой, то выводим сообщение:
        assert len(my_pets['pets']) == 0
        raise Exception("There is no user pets!")


