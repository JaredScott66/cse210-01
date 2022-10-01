import random


def Secret_word():

    word_list = ["steel", "cheese", "pumpkin"]

    index_choice = random.randint(0, 3)
    secret_word = word_list[index_choice]

print(secret_word)
    
