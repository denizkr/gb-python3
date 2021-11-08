import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# new_list = []

def get_jokes(arg):
    new_list = []
    count = 0
    while count < arg:
        new_list.append(random.choice(nouns))
        new_list.append(random.choice(adverbs))
        new_list.append(random.choice(adjectives))
        count += 1
        print(' '.join(new_list))


get_jokes(2)