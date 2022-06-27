import json
import os
from apiquery.settings import valid_email, valid_password
from apiquery.api import PetFriends

pf = PetFriends()

"""Test-Scenario 4. Создать питомца с фото, изменить его данные (formData) и удалить последнего питомца из списка"""

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


def test_3_update_pet_info(name='Ping-Pong', animal_type='Gorila/Monkey', age='190'):
    """Проверяем возможность обновления информации о питомце"""
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Если список не пустой, то пробуем обновить у созданного питомца его данные:
    if len(my_pets['pets']) > 0:
        status, result, content, optional = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        with open("out_json.json", 'a', encoding='utf8') as write:
            write.write('\ntest_3_update_pet_info:\n')
            json.dump(result, write, ensure_ascii=False, indent=4)
        print('\nContent:', content)
        print('Optional:', optional)

        # Проверяем статус ответа и что тело запроса соответствует заданному:
        assert status == 200
        assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    else:
        # Если список пустой, то выводим сообщение:
        assert len(my_pets['pets']) == 0
        raise Exception("There is no user pets!")


def test_4_delete_last_user_pet():
    """Проверяем возможность удаления последнего питомца"""
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    _, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    # Берём id последнего питомца из списка и отправляем запрос на удаление:
    pet_id = my_pets['pets'][-1]['id']
    _, my_pets, content, optional = pf.delete_pet(auth_key, pet_id)
    # Ещё раз запрашиваем список питомцев:
    status, my_pets, _, _ = pf.get_list_of_pets(auth_key, "my_pets")
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_4_delete_last_user_pet:\n')
        json.dump(my_pets, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    print('\nID last pet before:', pet_id)
    print('ID last pet after del:', pet_id in my_pets.values())

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца:
    assert status == 200
    assert pet_id not in my_pets.values()


