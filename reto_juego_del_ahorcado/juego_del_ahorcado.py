from random import uniform as rm
import os



def read():
    words=[]
    with open("./data/data.txt","r", encoding="utf-8") as f:
        for line in f:
            words.append(line)
    return words


def word_to_list(word):
    new_word=word.maketrans('áéíóú', 'aeiou')
    unaccent_word=word.translate(new_word)
    word_list=list(unaccent_word)
    word_list.pop()
    return word_list

def comparison(letter,word):
    word_list=word_to_list(word)
    values_compared=[letter==word_list[i] for i in range(0,len(word_list))]
    return values_compared


def listToString(s):

	str1 = ""

	for ele in s:
		str1 += ele

	return str1.upper()		


def print_interface(_list):
    os.system("clear")
    print("¡Adivina la palabra! :")
    print("\n")
    print("\n")
    for i in _list:
        print(i,end="  ")
    print("\n")
    

def start_game():
    random_index=round(rm(1,171))
    word=read()[random_index]
    return word



def run():
    word=start_game()
    word_list=word_to_list(word)
    word_to_guest=["_" for i in range(0,len(word_list))]
    answer=0
    print_interface(word_to_guest)
    while answer==0:
        user_word=input("Ingrese una letra: ")
        list_comparison=comparison(user_word,word)
        for j in range(0,len(word_list)):
            index=list_comparison[j]
            if index==True:
                word_to_guest[j]=user_word.upper()
        print_interface(word_to_guest)
        if listToString(word_list)==listToString(word_to_guest):
            answer=1
    print("¡Ganaste! la palabra era " + word.upper())

    print("\n")
    
    
    


if __name__=='__main__':
    run()