# valid email + valid password:
valid_email = ""  # name@domen
valid_password = ""
valid_name_31 = "zbk5_sdjg$f1ldf_56b5_sdfkjg$f51@bheps.com"  # valid name = 31 символ + valid domen
valid_pass_31 = "12sdf5sggn$FG#"
name_nul = "00000@bheps.com"  # только нули в имени
valid_password_nul = '12sdfFG#ds23d2'
name_numbers = "651856@bheps.com"  # только цифры в имени
valid_pass_numbers = "12sdfFGds23d21"
name_typeint = "75183456@bheps.com"  # только цифры в имени
pass_typeint = 3681547894

# valid name:
name_password = '12sdfFG#@bheps.com'
None_domen = "zeubaoabk5@bheps7.com"  # несуществующий домен
no_domen = "zeubaoabk5@"  # пустой домен
no_domen_com = "zeubaoabk5@.com"  # пустой домен.com
no_domen_sin_com = "zeubaoabk5@,com"  # пустой домен,com
domen_no_a = "zeubaoabk5bheps.com"  # valid domen без @
domen_is_ = "zeubaoabk5_bheps.com"  # valid domen_
valid_name_big = "ZEUBAOABK5@bheps.com"  # valid name ПРОПИСЬЮ + valid domen
valid_domen_big = "zeubaoabk5@BHEPS.com"  # valid domen ПРОПИСЬЮ
domen_space = "zeubaoabk5 bheps.com"  # + valid domen (вместо @ указать пробел)

# not valid name:
no_name = "@bheps.com"  # пустое имя
notvalid_name_less5 = "z$k5@bheps.com"  # количество валидных символов в имени меньше 5
valid_password_5 = "12srTdf5sggn$FG"
name_space = "zeub oabk5@bheps.com"  # пробел в имени
equals_name = "=zeubaoabk5@bheps.com"  # знак "=" в имени
valid_password_equals = '12sdfFG#ds23d'
name_minus = "-zeubaoabk5@bheps.com"  # знак "-" в начале
valid_pass_minus = "12sdfFGds23d2"
name_cyrillic = "fлд5шыs4ks@bheps.com"  # кириллица в имени
name_dash = "zeub–aoabk5@bheps.com"  # длинное тире"–" в имени
name_simbols = "$&_-#@bheps.com"  # набор символов
valid_pass_simbols = "12sdfFGds23d21d"
name_chinese = "Df站521df@bheps.com"  # китайские символы в имени
name_star = "zeubA*oaHk5@bheps.com"  # символ * в имени
valid_pass_star = "12sdfFG#sfa"
name_script = "<script>alert(123)</script>"  # скрипт: <script>alert(123)</script> вместо email
name_quest_mark = "zeuba?oabk5@bheps.com"  # только знаки ? в имени
valid_pass_qumark = "12sdfFG#sfadfD"
name_quote = "zeuba'abk5@bheps.com"  # кавычка ' в имени
valid_pass_quote = "12sdfFG#sD"
notvalid_name_32 = "fKfLjfsL_j355LjfklsJl820dol_dflj@bheps.com"  # name = 32 валидных символа
valid_pass_32 = "12sdfFGa#sD"
notvalid_name_10000 = "FdJr" + str(15 ** 8496) + "dflj@bheps.com"  # 10 тыс. валидных символов
valid_pass_n10s = "12sdf43FGa#sD"

# password:
pass_5s = "FdJr" + str(15 ** 4496) + "dfljsfsGdDg"  # 5 тыс. валидных символов
valemail_5s = "zeuba4bk5@bheps.com"
pass_less8 = "djsfsG"  # 5менее 8 валидных символов
valemail_p8 = "ze4ba4bk5@bheps.com"
pass_latin = "djssDfsfsG"  # только латинские
valemail_platin = "zeba4bk5@bheps.com"
password_numbers = "24365957256802"  # только цифры
valemail_num = "ze64bk5@bheps.com"
password_simbols = "*#&%*#%(#@&(%"  # только символы
valemail_simb = "ze64dlbk5@bheps.com"
password_cirilic = "sdfKsd*$ыжW"  # есть кириллица
valemail_cirilic = "ze655bk5@bheps.com"
password_chinese = "sdfK符號sd$W"  # есть китайские символы
valemail_chin = "ze6535bk5@bheps.com"
password_script = "<script>alert(123)</script>"  # скрипт: _alert(123)
valemail_pscript = "ze653d5bk5@bheps.com"
password_dash = "12sGd–43fFG"  # длинное тире"–"
valemail_pdash = "ze65fg3d5bk5@bheps.com"
password_self = "password"  # ввести: password
valemail_pself = "ze65fg3bk5@bheps.com"
password_order = "1234567g"  # ввести: 1234567g
valemail_porder = "ze65fgRk5@bheps.com"
password_nul = "0000000y"  # семь"0" и одна лат. буква
valemail_pnul = "zeW5fgRk5@bheps.com"
password_space = "12sGd 43fFG"  # пробел между валидными символами
valemail_pspace = "zeW5fgRkfd5@bheps.com"
password_spaceend = " 12sEGd43fFG"  # пробел в начале пароля
valemail_pspaceend = "QeW5fgERkd5@bheps.com"
password_date = "23.06.2022"  # дата вместо пароля
valemail_pdate = "QeW1gERkd5@bheps.com"
password_SQL = "(‘ or ‘a’ = ‘a’; DROP TABLE user; SELECT * FROM blog WHERE code LIKE ‘a%’;)"  # SQL запрос вместо пароля
valemail_pSQL = "QeW1gERk45d5@bheps.com"



"""тестирование POST"""
notvalid_name_1s = "Привет" + str(8 ** 1196) + "dfljs123fsGdDg"  # 1084 валидных символов
bigname_photo = r'../images/aflkjbhadsfiugvbliuagfoiuvgaiouhaflkjbhadsfiugvbliuagfoiuvgaiouhaflkjbhadsfiugvbliuagfoiuvgaiouhaflkjbhadsfiugvbliuagfoiuvgaiouhaflkjbhadsfiugvbliuagfoiuvgaiouhaflkjbhadsfiugvbliuagfoiuvgaiouhaflkjbhadsfiugvbli.jpg'
