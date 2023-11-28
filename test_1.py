import subprocess
import string

'''
Задание 1.
Условие: Написать функцию на Python, которой передаются в качестве параметров команда и текст. 
Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае. 
Передаваться должна только одна строка, разбиение вывода использовать не нужно.
'''

def test_1(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if result.returncode == 0:
        text_list = text.split()
        count = 0
        for t in text_list:
            if t in result.stdout:
                count += 1
        if count >= len(text_list):
            return 'True'
        else:
            return 'False'
    else:
        return 'False'


print(test_1('cat /etc/os-release', '22.04 jammy'))



'''
Задание 2.(повышенной сложности)
Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы, в котором вывод разбивается на слова 
с удалением всех знаков пунктуации (их можно взять из списка string.punctuation модуля string). В этом режиме должно проверяться наличие слова в выводе.
'''

def test_2(command, word):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if result.returncode == 0:
        text_list = result.stdout.split()
        text_cleaned = ''
        for words in text_list:
            for char in words:
               if char in string.punctuation:
                   text_cleaned += ' '
               else:
                  text_cleaned = text_cleaned + char
            text_cleaned += ' '
        if word in text_cleaned:
            return 'True'
        else:
            return 'False'
    else:
        return 'False'


print(test_2('cat /etc/os-release', 'debian'))


