import json
import os
from apiquery.settings import valid_email, valid_password
from apiquery.api import PetFriends

pf = PetFriends()

"""Test-Scenario 1. "Создать питомца и загрузить фото"""

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


def test_3_add_foto_to_pet(pet_photo=r'../images/king-kong2.jpg'):
    """Проверяем добавление фото к id созданного питомца без фото"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']  # id изменяемого питомца

    # Добавляем фото
    status, result, content, optional = pf.add_pet_photo(auth_key, pet_photo, pet_id)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_3_add_foto_to_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    # Если данный текст содержится в полученном ответе, то Passed:
    assert 'data:image/jpeg' in result.get('pet_photo')

