
import random
char = "a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9" 
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
    print("""
 __      __                     _____                                    _    _____                           _             
 \ \    / /                    |  __ \                                  | |  / ____|                         | |            
  \ \  / /__  ___ _ __   __ _  | |__) |_ _ ___ _____      _____  _ __ __| | | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
   \ \/ / _ \/ __| '_ \ / _` | |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
    \  /  __/\__ \ |_) | (_| | | |  | (_| \__ \__  \ V  V / (_) | | | (_| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
     \/ \___||___/ .__/ \__,_| |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                 | |                                                                                                        
                 |_|                                                                                                        
              """)
    print("By Kirua for Vespa Corporation")
    print("Choisi la longeur du mdp boufon:")
    user_len_password = int(input())
    final_password = gen_password(user_len_password)
    print("Voici ton mdp macaque :", final_password)
    print("Tu as fini ? o/n")
    choice = input()
if choice == "o":
        continue_prog = False
        
