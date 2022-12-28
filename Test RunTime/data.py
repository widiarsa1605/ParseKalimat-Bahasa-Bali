import os

def kamus(cnf):
    terminal = {
        'Noun': 15,  
        'Pronoun': 16,  
        'PropNoun': 19,    
        'Prep': 20, 
        'Adv': 17, 
        'Adj': 18,  
        'Verb': 21
    }
    user = 0
    ulang = ''
    while user != 8 and ulang == '':
        os.system('cls')
        print('Kamus\n1. Noun\n2. Pronoun\n3. PropNoun\n4. Prep\n5. Adv\n6. Adj\n7. Verb\n8. Return\n')
        user = int(input("Masukkan input: "))
        if user == 1:
            os.system('cls')
            print(cnf[terminal['Noun']][0][0], end='\n\n')
            print(cnf[terminal['Noun']][1])
        elif user == 2:
            os.system('cls')
            print(cnf[terminal['Pronoun']][0][0], end='\n\n')
            print(cnf[terminal['Pronoun']][1])
        elif user == 3:
            os.system('cls')
            print(cnf[terminal['PropNoun']][0][0], end='\n\n')
            print(cnf[terminal['PropNoun']][1])
        elif user == 4:
            os.system('cls')
            print(cnf[terminal['Prep']][0][0], end='\n\n')
            print(cnf[terminal['Prep']][1])
        elif user == 5:
            os.system('cls')
            print(cnf[terminal['Adv']][0][0], end='\n\n')
            print(cnf[terminal['Adv']][1])
        elif user == 6:
            os.system('cls')
            print(cnf[terminal['Adj']][0][0], end='\n\n')
            print(cnf[terminal['Adj']][1])
        elif user == 7:
            os.system('cls')
            print(cnf[terminal['Verb']][0][0], end='\n\n')
            print(cnf[terminal['Verb']][1])
        elif user == 8:
            print("Terima Kasih!!")
        else:
            print("tidak ada dalam menu")
            user = int(input("Masukkan input: "))
        ulang = input('')
    
        
