import json
import os
from apiquery.settings import valid_email, valid_password
from apiquery.api import PetFriends

pf = PetFriends()

"""Test-Scenario 2. "Создать питомца с фото и загрузить новое фото"""

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


def test_2_add_new_pet_photo(name='King-Kong', animal_type='Monkey', age='3', pet_photo=r'../images/king-kong1.jpg'):
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


def test_3_changes_petfoto(pet_photo=r'../images/king-kong3.jpg'):
    """Проверяем изменение фото добавленного ранее питомца"""
    # # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']  # id изменяемого питомца
    value_image1 = my_pets['pets'][0]['pet_photo']  # image изменяемой фотки
    print(f"\nvalue_image1: {len(str(value_image1))} символов: {value_image1}", sep='')

    # Добавляем фото
    status, result, content, optional = pf.add_pet_photo(auth_key, pet_photo, pet_id)
    value_image2 = result.get('pet_photo')
    print(f"value_image2: {len(str(value_image2))} символов: {value_image2}")
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_3_changes_petfoto:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    # Если текст первой фотки отсутствует в полученном ответе, то Passed:
    assert value_image1 != value_image2

