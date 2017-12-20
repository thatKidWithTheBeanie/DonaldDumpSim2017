### copyright Donald Dump Simulator 2017, bananaPi 21/11/17 22:00
###  ___                                      ___   ___ 
### | _ )  __ _   _ _    __ _   _ _    __ _  | _ \ |_ _|
### | _ \ / _` | | ' \  / _` | | ' \  / _` | |  _/  | | 
### |___/ \__,_| |_||_| \__,_| |_||_| \__,_| |_|   |___|
###                                                     
###

### add dificulty level /// variable to starting Country.rel /// population increse

### impeachment level, ie. heath points
impeachmentlvl = 0

### all users start with a small loan
USD = 1000000

### Current day of presidency
day = 0
if day == 1460:
    GameOver()

### UI break lines
def cut():
    print("")
    print("")
    print("")
    
### Ethnicity count
### prefix (eth) suffix (personal)
ethwhite = 233000000    ### white
ethafam = 39000000      ### african america
ethnat = 2000000        ### native american/alaskan
ethasi = 16000000       ### asian
ethisland = 500000      ### islanders
ethhis = 54000000       ### hispanic
totpop = ethwhite + ethafam + ethnat + ethasi + ethisland + ethhis   ### total population
### relationships classing
class Country(object):

    
    def __init__(self, name, parent, rel, starter, hp):
        self.name = name        ### country name
        self.parent = parent    ### Area name eg. Eastern Europe, Asia
        self.rel = 50           ### realtionship level (100 > :-( )
        self.starter = neutral  ### In relation to the USA
        self.hp = 100           ### health points
        ### maybe add army attribute
        ### eventually add economic influence

        if self.rel <= 40 and self.rel >= 60:      ### if rel is between 40 and 60
            self.starter = "neutral"
        if self.rel >= 61 and self.rel <= 99:      ### if rel is more than 61 and less than 99
            self.starter = "friend"     
        if self.rel <= 39 and self.rel >= 1:       ### if rel is less than 39 more than 1
            self.starter = "enemy"
        if self.rel <= 0:                ### if rel is equal or less than 0
            self.starter = "You are at war"
        if self.rel >= 100:              ### if rel is equal or more than 100
            self.starter = "besties forever!"
        if self.hp == 0 and self.starter == "You are at war":
            conquered()
            ### Do this bit
        if self.hp == 0 and self.starter == "friend":
            allyDead()
            ### Do this bit

        ### Static countries defined
        ### --------- Asia -------------
        China = Country('China', 'CAsia', 50, '', 100)
        Japan = Country('Japan', 'EAsia', 50, '', 100)
        NKorea = Country('North Korea', 'EAsia', 50, '', 100)
        Skorea = Country('South Korea', 'EAsia', 50, '', 100)
        Thiland = Country('Thiland', 'EAsia', 50, '', 100)
        Vietnam = Country('Vietnam', 'EAsia', 50, '', 100)
        Indionesia = Country('Indionesia', 'EAsia', 50, '', 100)
        Mongolia = Country('Mongolia', 'CAsaia', 50, '', 100)
        India = Country('India', 'CAsia', 50, '', 100)
        Kazakhstan = Country('Kazakhstan', 'CAsia', 50, '', 100)
        Pakistan = Country('Pakistan', 'CAsia', 50, '', 100)
        Afghanistan = Country('Afghanistan', 'WAsia', 50, '', 100)
        Iran = Country('Iran', 'WAsia', 50, '', 100)
        Iraq = Country('Iraq', 'WAsia', 50, '', 100)
        SaudiArabia = Country('SaudiArabia', 'WAsia', 50, '', 100)
        ### -------- Europe ----------
        Russia = Country('Russia', 'EEurope', 50, '', 100)
        Turkey = Country('Turkey', 'EEurpe', 50, '', 100)
        Ukraine = Country('Ukraine', 'EEurpe', 50, '', 100)
        Belarus = Country('Belarus', 'EEurpe', 50, '', 100)
        Poland = Country('Poland', 'EEurpe', 50, '', 100)
        Romania = Country('Romania', 'EEurpe', 50, '', 100)
        Italy = Country('Italy', 'CEurpe', 50, '', 100)
        Germany = Country('Germany', 'CEurpe', 50, '', 100)
        France = Country('France', 'WEurpe', 50, '', 100)
        Spain = Country('Spain', 'WEurpe', 50, '', 100)
        Portugal = Country('Portugal', 'WEurpe', 50, '', 100)
        UK = Country('UK', 'WEurope', 50, '', 100)
        Ireland = Country('Ireland', 'WEurope', 50, '', 100)
        Netherlands = Country('Netherlands', 'WEurope', 50, '', 100)
        Finland = Country('Finland', 'NEurope', 50, '', 100)
        Sweden = Country('Sweden', 'NEurope', 50, '', 100)
        Norway = Country('Norway', 'NEurope', 50, '', 100)
        Iceland = Country('Iceland', 'NEurope', 50, '', 100)
        Greenland = Country('Greenland', 'NEurope', 50, '', 100) ### I know it's not a member anymore but wtf else is it?
        ### -------- The Americas -------------
        Canada = Country('Canada', 'NAmerica', 50, '', 100)
        Mexico = Country('Mexico', 'NAmerica', 50, '', 100)
        Cuba = Country('Cuba', 'CAmerica', 50, '', 100)
        Haiti = Country('Haiti', 'CAmerica', 50, '', 100)
        CostaRica = Country('Costa Rica', 'CAmerica', 50, '', 100)
        Venezuala = Country('Venezuala', 'SAmerica', 50, '', 100)
        Colombia = Country('Colombia', 'SAmerica', 50, '', 100)
        Ecuador = Country('Ecuador', 'SAmerica', 50, '', 100)
        Peru = Country('Peru', 'SAmerica', 50, '', 100)
        Brasil = Country('Brasil', 'SAmerica', 50, '', 100)
        Bolivia = Country('Bolivia', 'SAmerica', 50, '', 100)
        Paraguay = Country('Paraguay', 'SAmerica', 50, '', 100)
        Chile = Country('Chile', 'SAmerica', 50, '', 100)
        Argentina = Country('Argentina', 'SAmerica', 50, '', 100)
        ### -------- Africa -----------------
        
### personal realtionships
class Person(object):
    def __init__(self, name, rom, fren, hat):
        self.name = name        ### persons name
        self.rom = 0            ### romantic level
        self.fren = 0           ### Friendship level
        self.hat = 0            ### hatred level
        
### New day
def newday():
    print ("Today is day ", day, " of your term")
    print ("Your impeachment level is ", impeachmentlvl)
    print ("You have $", USD, "USD")
    print ("The population is ", totpop)
    day + 1
    print ("")

### Time skip
### wow what a shockingly inefficent way to do something so simple?
### what a lol
def skip():
    if atwar == True:     ### during war time?
        print ("You cannot time skip during war time.")
    else:
        while skipping == True:      ### while loop
            print ("How many days would you like to skip?")     ### how much time to skip?
            howmany = input ("")
            if howmany.isnumeric():                             ### did they enter a valid input?
                print ("Are you sure you would like to skip ", howmany, " days? y/n")
                yn = input ("")                                 ### are you sure?
                if yn == "Y" or yn == "y":                      ### skip
                    day + howmany
                    cut()
                    skipping = False
                if yn == "N" or yn == "n":                      ### don't skip
                    cut()
                else:                                           ### you are a doofus
                    print ("Please only enter y or n")
                    cut()
            else:                                               ### a massive doofus
                print ("Please only enter a number.")
            
    newday()                                                    ### next day

### -------------------------   INTRO   --------------------------    
print ("Welcome to the Donald Dump Simulator 2017!")
cut()
print ("The date is January 20th, 2017. You, looking particularly peachy, surrounded by your fellow white males are about to take your next step towards what could be your most profitable venture yet!")
print ("Another white man steps forward and you pout your strong, imposing, definied orange lips as you begin to utter the oath.")
cut()
print ("You are now the offical president of the United States of America.")
cut()
print ("No more sitting crosslegged on your golden bathroom floor, pretending Melania loves you and playing with your model concentration camps.")
print ("The world is yours.")
print ("You are Donald Dump.")
print ("*Eagle caws in the distance*")
cut()
cut()
cut()
### ----------------------- END ----------------------

