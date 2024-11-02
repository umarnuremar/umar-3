def count_letters(text):
    let_count = {}

    for char in text:
        if char.isalpha():  #Является ли символ буквой
            lower_char = char.lower()
            if lower_char in let_count:
                let_count[lower_char] += 1
            else:
                let_count[lower_char] = 1
    return let_count

def calculate_frequency(let_count):
    total_letters = sum(let_count.values())  #Общее колво букв
    frequency = {}

    for letter in let_count.keys():  #Через порядок появления букв
        freq = round(let_count[letter] / total_letters, 2) if total_letters > 0 else 0.00
        frequency[letter] = f"{freq:.2f}"

    return frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

#Подсчет букв и их частоты
let_counts = count_letters(main_str)
frequencies = calculate_frequency(let_counts)

for letter, freq in frequencies.items():
    print(f"{letter}: {freq}")

