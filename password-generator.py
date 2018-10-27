
import random
char = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
char_sep = char.split(" ")
def gen_password(pass_len):
    password = "" 
    random_nbr = 0
    i = 0
    while i < pass_len: 
        random_nbr = random.randint(0, len(char_sep) - 1) 
        password = password + char_sep[random_nbr]
        i += 1 
    return password
    
continue_prog = True 
while continue_prog:
    print("Vespa Password Generator ")
    print("By Kirua for Vespa Corporation")
    print("Choisi la longeur du mdp boufon:")
    user_len_password = int(input())
    final_password = gen_password(user_len_password)
    print("Voici ton mdp macaque :", final_password)
    print("Tu as fini ? o/n")
    choice = input()
    #pour choisir de redemarer ou pas
    if choice == "o":
        continue_prog = False