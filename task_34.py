# Задача 34:  
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  


def check_rhythm(poem):
    words = poem.split()  # Разделяем стихотворение на отдельные слова
    syllables = []  # Список для хранения количества слогов в каждой фразе

    for word in words:
        syllable_count = word.count('-') + 1  # Количество слогов равно количеству дефисов плюс один
        syllables.append(syllable_count)

    if len(set(syllables)) == 1:
        return "Парам пам-пам"  # Все фразы имеют одинаковое количество слогов
    else:
        return "Пам парам"  # Разное количество слогов в фразах






