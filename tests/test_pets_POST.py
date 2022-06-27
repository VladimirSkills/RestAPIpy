import json
import os
from apiquery.settings import valid_email, valid_password, notvalid_name_1s, bigname_photo
from apiquery.api import PetFriends
import time  # для вывода времени выполнения теста: time_test

pf = PetFriends()

def test_1_add_new_pet(name='King-Kong', animal_type='Monkey', age='3', pet_photo=r'../images/king-kong2.jpg'):
    """Позитивный. Валидный тест. Проверяем, что питомец добавлен с корректными данными"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    start = time.monotonic_ns()  # засекаем таймер начала выполнения теста...
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'w', encoding='utf8') as write:
        write.write('\ntest_1_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    finish = time.monotonic_ns()  # засекаем таймер после выполнения теста...
    time_test = (finish - start)//1000000
    print(f"Время выполнения теста: {time_test} млсек.")

    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')
    assert time_test < 1000


def test_2_add_new_pet(name='King-Kong-Live!', animal_type='Monkey/Gorila', age='525', pet_photo=r'../images/king-kong1.jpg'):
    """Негативный. Валидные параметры. Проверяем на возврат 405, так как пробуем получить ответ
    при отправлении запроса по невалидному пути - PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet_set_photo(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_2_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 405


def test_3_add_new_pet(name='King-Kong-Live!', animal_type='Monkey/Gorila', age='525', pet_photo=r'../images/king-kong2.jpg'):
    """Негативный. auth_key = пустое - PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    auth_key = {'key': ''}
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_3_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 403
    #assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    #assert 'image/jpeg' in result.get('pet_photo')


def test_4_add_new_pet(name='King-Kong-Live!', animal_type='Monkey/Gorila', age='525', pet_photo=r'../images/king-kong2.jpg'):
    """Негативный. Валидный ключ в формате int - FAILED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    auth_key = {'key': f5b1037b3374bd1e3d195bdadb6a93e2ea8c299aa89e6d4658ebf6c0}
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_4_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 403
    #assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    #assert 'image/jpeg' in result.get('pet_photo')


def test_5_add_new_pet(name='King-Kong-Live!', animal_type='Monkey/Gorila', age='525', pet_photo=r'../images/king-kong2.jpg'):
    """Негативный. Валидный ключ без последнего символа PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    auth_key = {'key': 'f5b1037b3374bd1e3d195bdadb6a93e2ea8c299aa89e6d4658ebf6c'}
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_5_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 403
    #assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    #assert 'image/jpeg' in result.get('pet_photo')


def test_6_add_new_pet(name='King-Kong-Live!', animal_type='Monkey/Gorila', age='525', pet_photo=r'../images/king-kong2.jpg'):
    """Негативный. Валидный ключ с добавлением копии последнего символа PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    auth_key = {'key': 'f5b1037b3374bd1e3d195bdadb6a93e2ea8c299aa89e6d4658ebf6c00'}
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_6_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 403
    #assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    #assert 'image/jpeg' in result.get('pet_photo')


def test_7_add_new_pet(name='King-Kong-Live!', animal_type='Monkey/Gorila', age='525', pet_photo=r'../images/king-kong2.jpg'):
    """Негативный. Скрипт вместо ключа PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    auth_key = {'key': '<script>alert(f5b1037b3374bd1e3d195bdadb6a93e2ea8c299aa89e6d4658ebf6c0)</script>'}
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_7_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 403
    #assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    #assert 'image/jpeg' in result.get('pet_photo')


def test_8_add_new_pet(name='King-Kong-Live!', animal_type='Monkey/Gorila', age='525', pet_photo=r'../images/king-kong2.jpg'):
    """Негативный. valid email + valid password вместо ключа PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    auth_key = {'key': 'zeubaoabk5@bheps.com&12sdfFG#'}
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_8_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 403
    #assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    #assert 'image/jpeg' in result.get('pet_photo')


def test_9_add_new_pet(name='King-Kong-Live!', animal_type='Monkey/Gorila', age='111', pet_photo=r'../images/king-kong2.jpg'):
    """Негативный. Валидный ключ другого пользователя PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    auth_key = {'key': '475466af18cc7523c269acefa60173e500c18f00369a7be8d50c9a1c'}
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_9_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')


def test_10_add_new_pet(name='', animal_type='Monkey/Gorila', age='111', pet_photo=r'../images/king-kong2.jpg'):
    """Негативный. Пустое имя питомца PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_10_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')


def test_11_add_new_pet(name='156165465156', animal_type='Monkey/Gorila', age='111', pet_photo=r'../images/king-kong2.jpg'):
    """Негативный. Только числа, символы, китайские иероглифы в имени PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_11_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')


def test_12_add_new_pet(name='Кинг-Конг', animal_type='Monkey/Gorila', age='111', pet_photo=r'../images/king-kong2.jpg'):
    """Негативный. Только кириллица в имени PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_12_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')


def test_13_add_new_pet(name=notvalid_name_1s, animal_type='Monkey/Gorila', age='111', pet_photo=r'../images/king-kong2.jpg'):
    """Негативный. Имя длинною в 1 тыс. символов PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_13_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')


def test_14_add_new_pet(name='King-Kong', animal_type='#*&_=?$()Х{}!@', age='111', pet_photo=r'../images/king-kong2.jpg'):
    """Негативный. В поле Тип только символы PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_14_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')


def test_15_add_new_pet(name='King-Kong', animal_type='Monkey/Gorila', age=111, pet_photo=r'../images/king-kong2.jpg'):
    """Негативный. В поле Age указываем число в форате int FAILED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_15_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')


def test_16_add_new_pet(name='King-Kong', animal_type='Monkey/Gorila', age='', pet_photo=r'../images/king-kong2.jpg'):
    """Негативный. В поле Тип пустое значение PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_16_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')


def test_17_add_new_pet(name='King-Kong', animal_type='Monkey/Gorila', age='88', pet_photo=''):
    """Негативный. В поле pet_photo пустое значение FAILED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_17_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')


def test_18_add_new_pet(name='King-Kong', animal_type='Monkey/Gorila', age='188', pet_photo=r'../images/king-kong-err.jpg'):
    """Негативный. В поле pet_photo: "Битый" файл FAILED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_18_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')


def test_19_add_new_pet(name='King-Kong', animal_type='Monkey/Gorila', age='188', pet_photo=r'../images/king-kong4.exe'):
    """Негативный. В поле pet_photo: Файл jpg с другим расширением: txt, pdf, bmp, gif, png, rar, exe PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_19_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')


def test_20_add_new_pet(name='King-Kong', animal_type='Monkey/Gorila', age='122', pet_photo=r'../images/file.exe'):
    """Негативный. В поле pet_photo: Файл exe PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_20_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')


def test_21_add_new_pet(name='King-Kong', animal_type='Monkey/Gorila', age='111', pet_photo=r'../images/king-kong5.jpg'):
    """Негативный. В поле pet_photo: объёмный файл 50Mb с большим расширением PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_21_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')


def test_22_add_new_pet(name='King-Kong', animal_type='Monkey/Gorila', age='155', pet_photo=r'../images/照片文件名.jpg'):
    """Негативный. В поле pet_photo: Название файла китайские иероглифы PASSED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_22_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 500
    #assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    #assert 'image/jpeg' in result.get('pet_photo')


def test_23_add_new_pet(name='King-Kong', animal_type='Monkey/Gorila', age='145', pet_photo=bigname_photo):
    """Негативный. В поле pet_photo: 210 символов в названии файла FAILED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_23_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 200
    assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    assert 'image/jpeg' in result.get('pet_photo')


def test_24_add_new_pet(name='King-Kong', animal_type='Monkey/Gorila', age='145', pet_photo=r'../images/фотоfoto.jpg'):
    """Негативный. В поле pet_photo: Кириллица и латиница в названии файла FAILED"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_24_add_new_pet:\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученный ответ с ожидаемым результатом:
    assert status == 500
    #assert result.get('name') == name and result.get('animal_type') == animal_type and result.get('age') == age
    #assert 'image/jpeg' in result.get('pet_photo')



