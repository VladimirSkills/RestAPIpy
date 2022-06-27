import json
from apiquery.settings import valid_email, valid_password, None_domen, no_domen, no_domen_com, no_domen_sin_com, \
domen_no_a, domen_is_, valid_name_big, valid_domen_big, domen_space, valid_name_31, valid_pass_31, \
no_name, notvalid_name_less5, valid_password_5, name_space, equals_name, valid_password_equals, name_nul, \
valid_password_nul, name_minus, valid_pass_minus, name_cyrillic, name_numbers, valid_pass_numbers, name_dash, \
name_simbols, valid_pass_simbols, name_chinese, name_star, valid_pass_star, name_script, name_quest_mark, \
valid_pass_qumark, name_quote, valid_pass_quote, notvalid_name_32, valid_pass_32, notvalid_name_10000, valid_pass_n10s, \
pass_5s, valemail_5s, pass_less8, valemail_p8, pass_latin, valemail_platin, password_numbers, valemail_num, \
password_simbols, valemail_simb, password_cirilic, valemail_cirilic, password_chinese, valemail_chin, password_script, \
valemail_pscript, password_dash, valemail_pdash, password_self, valemail_pself, password_order, valemail_porder, \
password_nul, valemail_pnul, password_space, valemail_pspace, password_spaceend, valemail_pspaceend, password_date, \
valemail_pdate, password_SQL, valemail_pSQL, name_password, name_typeint, pass_typeint
from apiquery.api import PetFriends

pf = PetFriends()

def test_1_get_api_key_valid_NP(email=valid_email, password=valid_password):
    """ Позитивный. Проверяем на 200 valid email + valid password - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'w', encoding='utf8') as write:
        write.write('test_1_get_api_key_valid_NP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result
    assert optional.get('email') == valid_email
    assert optional.get('password') == valid_password


def test_2_get_api_key_valid_NP(email=None_domen, password=valid_password):
    """ Негативный. Проверяем на 403 valid name + несуществующий домен - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_2_get_api_key_valid_NP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_3_get_api_key_valid_NP(email=no_domen, password=valid_password):
    """ Негативный. Проверяем на 403 valid name + пустой домен - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_3_get_api_key_valid_NP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_4_get_api_key_valid_NP(email=no_domen_com, password=valid_password):
    """ Негативный. Проверяем на 403 valid name + пустой домен.com - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_4_get_api_key_valid_NP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_5_get_api_key_valid_NP(email=no_domen_sin_com, password=valid_password):
    """ Негативный. Проверяем на 403 valid name + valid domen,com - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_5_get_api_key_valid_NP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_6_get_api_key_valid_NP(email=domen_no_a, password=valid_password):
    """ Негативный. Проверяем на 403 valid name + valid domen без @ - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_6_get_api_key_valid_NP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_7_get_api_key_valid_NP(email=domen_is_, password=valid_password):
    """ Негативный. Проверяем на 403 вместо @ указать "_" - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_7_get_api_key_valid_NP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_8_get_api_key_valid_NP(email=valid_name_big, password=valid_password):
    """ Негативный. Проверяем на 200 valid name ПРОПИСЬЮ + valid domen - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_8_get_api_key_valid_NP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_9_get_api_key_valid_NP(email=valid_domen_big, password=valid_password):
    """ Негативный. Проверяем на 200 valid name + valid domen ПРОПИСЬЮ - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_9_get_api_key_valid_NP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_10_get_api_key_valid_NP(email=domen_space, password=valid_password):
    """ Негативный. Проверяем на 403 valid name + valid domen (вместо @ указать пробел) - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_10_get_api_key_valid_NP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_11_get_api_key_valid_NP(email=valid_name_31, password=valid_pass_31):
    """ Позитивный. Проверяем на 200 valid name = 31 символ + valid domen - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_11_get_api_key_valid_NP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_12_get_api_key_valid_P_notN(email=no_name, password=valid_password):
    """ Негативный. Проверяем на 403 пустое имя + valid domen - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_12_get_api_key_valid_P_notN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_13_get_api_key_valid_P_notN(email=notvalid_name_less5, password=valid_password_5):
    """ Негативный. Проверяем на 403 количество валидных символов в имени меньше 5 + valid domen - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_13_get_api_key_valid_P_notN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_14_get_api_key_valid_P_notN(email=name_space, password=valid_password):
    """ НЕГАТИВНЫЙ. Проверяем на 403 пробел в имени + valid domen - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_14_get_api_key_valid_P_notN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_15_get_api_key_valid_P_notN(email=equals_name, password=valid_password_equals):
    """ Негативный. Проверяем на 403 знак "=" в имени + valid domen - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_15_get_api_key_valid_P_notN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_16_get_api_key_valid_PN(email=name_nul, password=valid_password_nul):
    """ НЕГАТИВНЫЙ. Проверяем на 200 только нули в имени + valid domen - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_16_get_api_key_valid_PN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_17_get_api_key_valid_P_notN(email=name_minus, password=valid_pass_minus):
    """ Негативный. Проверяем на 403 знак "-" в начале + valid domen - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_17_get_api_key_valid_P_notN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_18_get_api_key_valid_P_notN(email=name_cyrillic, password=valid_password):
    """ НЕГАТИВНЫЙ. Проверяем на кириллицу в имени + valid domen - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_18_get_api_key_valid_P_notN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'UnicodeEncodeError' in result


def test_19_get_api_key_valid_PN(email=name_numbers, password=valid_pass_numbers):
    """ Позитивный. Проверяем на 200 только цифры в имени + valid domen - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_19_get_api_key_valid_PN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_20_get_api_key_valid_P_notN(email=name_dash, password=valid_password):
    """ НЕГАТИВНЫЙ. Проверяем на 403 длинное тире "–" в имени + valid domen - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_20_get_api_key_valid_P_notN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'UnicodeEncodeError' in result


def test_21_get_api_key_valid_P_notN(email=name_simbols, password=valid_pass_simbols):
    """ Позитивный. Проверяем на 403 набор символов + valid domen - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_21_get_api_key_valid_P_notN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_22_get_api_key_valid_P_notN(email=name_chinese, password=valid_password):
    """ НЕГАТИВНЫЙ. Проверяем на 403 китайские символы в имени + valid domen - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_22_get_api_key_valid_P_notN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'UnicodeEncodeError' in result


def test_23_get_api_key_valid_P_notN(email=name_star, password=valid_pass_star):
    """ Негативный. Проверяем на 403 символ * в имени + valid domen - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_23_get_api_key_valid_P_notN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_24_get_api_key_valid_P_notN(email=name_script, password=valid_password):
    """ Негативный. Проверяем на 403 скрипт: alert(123) вместо email + valid domen - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_24_get_api_key_valid_P_notN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_25_get_api_key_valid_P_notN(email=name_quest_mark, password=valid_pass_qumark):
    """ Негативный. Проверяем на 403 знак ? в имени + valid domen - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_25_get_api_key_valid_P_notN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_26_get_api_key_valid_P_notN(email=name_quote, password=valid_pass_quote):
    """ Негативный. Проверяем на 403 кавычка ' в имени + valid domen - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_26_get_api_key_valid_P_notN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_27_get_api_key_valid_P_notN(email=notvalid_name_32, password=valid_pass_32):
    """ Негативный. Проверяем на 403 name = 32 валидных символа + valid domen - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_27_get_api_key_valid_P_notN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_28_get_api_key_valid_P_notN(email=notvalid_name_10000, password=valid_pass_n10s):
    """ НЕГАТИВНЫЙ. Проверяем на 403 name ≈ 10 тыс. валидных символов + valid domen - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_28_get_api_key_valid_P_notN\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 400
    assert 'key' is not result


def test_29_get_api_key_valid_E_notP(email=valemail_5s, password=pass_5s):
    """ НЕГАТИВНЫЙ. Проверяем на 200 password ~ 5 тыс. валидных символов (valid Email) - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_29_get_api_key_valid_E_notP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' is not result


def test_30_get_api_key_valid_E_notP(email=valemail_p8, password=pass_less8):
    """ Негативный. Проверяем на 401 password менее 8 валидных символов (valid Email) - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_30_get_api_key_valid_E_notP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 401
    assert 'key' is not result


def test_31_get_api_key_valid_E_notP(email=valemail_platin, password=pass_latin):
    """ Позитивный. Проверяем на 200 password только латинские (valid Email) - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_31_get_api_key_valid_E_notP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' is not result


def test_32_get_api_key_valid_E_notP(email=valemail_num, password=password_numbers):
    """ Негативный. Проверяем на 401 password только цифры (valid Email) - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_32_get_api_key_valid_E_notP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 401
    assert 'key' is not result


def test_33_get_api_key_valid_E_notP(email=valemail_simb, password=password_simbols):
    """ Негативный. Проверяем на 401 password только символы (valid Email) - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_33_get_api_key_valid_E_notP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 401
    assert 'key' is not result


def test_34_get_api_key_valid_E_notP(email=valemail_cirilic, password=password_cirilic):
    """ НЕГАТИВНЫЙ. Проверяем на 403 password есть кириллица (valid Email) - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_34_get_api_key_valid_E_notP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'UnicodeEncodeError' in result


def test_35_get_api_key_valid_E_notP(email=valemail_chin, password=password_chinese):
    """ НЕГАТИВНЫЙ. Проверяем на 403 password есть китайские символы (valid Email) - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_35_get_api_key_valid_E_notP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'UnicodeEncodeError' in result


def test_36_get_api_key_valid_E_notP(email=valemail_pscript, password=password_script):
    """ Негативный. Проверяем на 401 password скрипт: alert(123) (valid Email) - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_36_get_api_key_valid_E_notP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 401
    assert 'key' is not result


def test_37_get_api_key_valid_E_notP(email=valemail_pdash, password=password_dash):
    """ НЕГАТИВНЫЙ. Проверяем на 401 password длинное тире "–" (valid Email) - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_37_get_api_key_valid_E_notP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 401
    assert 'UnicodeEncodeError' in result


def test_38_get_api_key_valid_E_notP(email=valemail_pself, password=password_self):
    """ Негативный. Проверяем на 401 password ввести: password (valid Email) - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_38_get_api_key_valid_E_notP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 401
    assert 'key' is not result


def test_39_get_api_key_valid_E_notP(email=valemail_porder, password=password_order):
    """ Негативный. Проверяем на 401 password ввести: 1234567g (valid Email) - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_39_get_api_key_valid_E_notP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 401
    assert 'key' is not result


def test_40_get_api_key_valid_E_notP(email=valemail_pnul, password=password_nul):
    """ Негативный. Проверяем на 401 password ввести: семь"0" и одна лат. буква (valid Email) - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_40_get_api_key_valid_E_notP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 401
    assert 'key' is not result


def test_41_get_api_key_valid_E_notP(email=valemail_pspace, password=password_space):
    """ Негативный. Проверяем на 401 password пробел между валидными символами (valid Email) - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_41_get_api_key_valid_E_notP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 401
    assert 'key' is not result


def test_42_get_api_key_valid_E_notP(email=valemail_pspaceend, password=password_spaceend):
    """ Негативный. Проверяем на 403 password пробел в начале (valid Email) - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_42_get_api_key_valid_E_notP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'space in header' in result


def test_43_get_api_key_valid_E_notP(email=valemail_pdate, password=password_date):
    """ Негативный. Проверяем на 401 password дата вместо пароля (valid Email) - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_43_get_api_key_valid_E_notP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 401
    assert 'key' is not result


def test_44_get_api_key_valid_E_notP(email=valemail_pSQL, password=password_SQL):
    """ Негативный. Проверяем на 401 password SQL запрос: (‘ or ‘a’ = ‘a’; DROP TABLE user;
    SELECT * FROM blog WHERE code LIKE ‘a%’;) (valid Email) - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_44_get_api_key_valid_E_notP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 401
    assert 'UnicodeEncodeError' in result


def test_45_get_api_key_notvalid_EP(email=valid_email, password=valid_pass_31):
    """ НЕГАТИВНЫЙ. Проверяем на 403 valid email/user1 + valid password/user2 - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_45_get_api_key_notvalid_EP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_46_get_api_key_notvalid_EP(email=valid_name_31, password=valid_password):
    """ НЕГАТИВНЫЙ. Проверяем на 403 valid email/user2 + valid password/user1 - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_46_get_api_key_notvalid_EP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_47_get_api_key_notvalid_EP(email=name_simbols, password=password_space):
    """ НЕГАТИВНЫЙ. Проверяем на 403 not valid email + not valid password - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_47_get_api_key_notvalid_EP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_48_get_api_key_notvalid_EP(email=valid_password, password=valid_email):
    """ НЕГАТИВНЫЙ. Проверяем на 403 email: valid password + password: valid email - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_48_get_api_key_notvalid_EP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_49_get_api_key_notvalid_EP(email=name_password, password=valid_password):
    """ НЕГАТИВНЫЙ. Проверяем на 403 email: name = password - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_49_get_api_key_notvalid_EP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_50_get_api_key_notvalid_EP(email='', password=''):
    """ НЕГАТИВНЫЙ. Проверяем на 403 email: пустое + password: пустое - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_50_get_api_key_notvalid_EP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_51_get_api_key_notvalid_EP(email='', password=valid_password):
    """ НЕГАТИВНЫЙ. Проверяем на 403 email: пустое + valid password - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_51_get_api_key_notvalid_EP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_52_get_api_key_notvalid_EP(email=valid_email, password=''):
    """ НЕГАТИВНЫЙ. Проверяем на 403 valid email + password: пустое - PASSED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_52_get_api_key_notvalid_EP\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' is not result


def test_53_get_pets_and_email(filter=valid_email):
    """ Негативный. Получить значения valid email в Параметрах строки. FAILED"""

    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)  # статус возвращать не нужно, поэтому ставим _
    status, result, content, optional = pf.get_list_of_pets(auth_key, filter)

    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_53_get_pets_and_email\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)

    assert status == 500
    assert 'email' in optional


def test_54_add_newpet_email(name=valid_email, animal_type=valid_password, age=''):
    """Негативный. Получить значения valid email + valid password в Теле запроса. FAILED"""
    _, auth_key, _, _ = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result, content, optional = pf.post_get_add_pet_nofoto(auth_key, name, animal_type, age)

    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_54_add_newpet_email\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)

    assert status == 405
    assert 'email' in optional
    assert valid_email in result


def test_55_get_api_key_typedata(email=name_typeint, password=pass_typeint):
    """ Негативный. Проверяем на 200 изменение типа данных с str на int - FAILED """

    # Отправляем запрос
    status, result, content, optional = pf.get_api_key(email, password)
    with open("out_json.json", 'a', encoding='utf8') as write:
        write.write('\ntest_55_get_api_key_typedata\n')
        json.dump(result, write, ensure_ascii=False, indent=4)
    print('\nContent:', content)
    print('Optional:', optional)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' is not result



