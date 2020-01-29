import os, sys, time

title = """
   _____ _                 _      _____               _____            
  / ____(_)               | |    |  __ \             / ____|           
 | (___  _ _ __ ___  _ __ | | ___| |__) |_ _ ___ ___| |  __  ___ _ __  
  \___ \| | '_ ` _ \| '_ \| |/ _ \  ___/ _` / __/ __| | |_ |/ _ \ '_ \ 
  ____) | | | | | | | |_) | |  __/ |  | (_| \__ \__ \ |__| |  __/ | | |
 |_____/|_|_| |_| |_| .__/|_|\___|_|   \__,_|___/___/\_____|\___|_| |_|
                    | |                                                
                    |_|                                                
"""

options = """
 [1] Generate a wordlist
 [2] Create a random password
"""

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def checkVersion():
	version = sys.version[:1]
	if int(version) == 3:
		pass
	else:
		sys.exit(warning+" Veuillez lancer la version 3 de python.")

class ProgressBar:
    '''
    Progress bar
    '''
    def __init__ (self, valmax, maxbar, title):
        if valmax == 0:  valmax = 1
        if maxbar > 200: maxbar = 200
        self.valmax = valmax
        self.maxbar = maxbar
        self.title  = title
    
    def update(self, val):
        
        # format
        if val > self.valmax: val = self.valmax
        
        # process
        perc  = round((float(val) / float(self.valmax)) * 100)
        scale = 100.0 / float(self.maxbar)
        bar   = int(perc / scale)
  
        # render 
        out = '\r%20s [%s%s] %3d %% ' % (self.title, '=' * bar, ' ' * (self.maxbar - bar), perc)
        sys.stdout.write(out)
        #Extinction du curseur
        os.system('setterm -cursor off')
        #Rafraichissement de la barre
        sys.stdout.flush()

def BarStart():
	## Test =
	i = 1  #Variable surveillée
	#Objet barre de progression
	barre = ProgressBar(30,42, "Chargement")
	print('\n')
	for x in range(60):
	     barre.update(i) 
	     time.sleep(0.30)
	     i = i+1

def listCreating():
    name = input("Prénom de l'utilisateur : ")
    surname = input("Surnom de l'utilisateur : ")
    age = input("Age de l'utilisateur (Seulement un nombre SVP) : ")
    year = input("Année de naissance de l'utilisateur : ")

    try:
       val = int(age)
    except ValueError:
        print("\nVeuillez entrer un nombre !")
        age = input("\nAge de l'utilisateur (Seulement un nombre SVP) : ")

    try:
       val2 = int(year)
    except ValueError:
        print("\nVeuillez entrer un nombre !")
        year = input("\nAnnée de naissance de l'utilisateur : ")

    str = year # initial string
    stringlength = len(str) # calculate length of the list
    reversedYear = str[stringlength::-1] # slicing 

    one = name + year
    two = surname
    three = surname + year
    four = surname + name + age
    five = surname + reversedYear
    six = name + reversedYear
    seven = name.lower() + year
    eight = surname.lower() + year
    nine = name.lower() + reversedYear
    ten = surname.lower() + reversedYear
    eleven = year + age
    douze = age + year

    results = [one, two, three, four, five, six, seven, eight, nine, ten]

    print("\n\nResultat : \n")
    print(results)
    print("\nRésultats sauvegardé dans le fichier 'wordlist.txt' dans ce même dossier.")
    time.sleep(5)
    clear()
    print(title)
    print(options)

    f = open("wordlist.txt", "w+")

    for i in results:
        f.write(i + "\n")
    f.close()