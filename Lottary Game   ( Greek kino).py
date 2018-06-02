import random


while True:
    #Select between the numbers 1 and 12
    epilogh=input("Give the amount of numbers you wish to play (1-12) or (0) for EXIT :")
#Check of selection
    if (epilogh=='1'):
        print("You wish to play with %s number"%epilogh)
        one=0
        NOUMERA=[]
#Select between the numbers 1 and 80
        while one<1:
            noumera=int(input("Give the number you wish to play (1-80) :"))
            if (noumera not in NOUMERA) and (1<= noumera <=80) and type(noumera) == type(81):
                print("You have choosen the number %d" %noumera)
                NOUMERA.append(noumera)
                one+=1
            else:
                print("You selected wrong numbers, please give again")
#Betting
        while True:
            euro=int(input("Give the amount that you wish to bet (1,2,5,10)"))
            if (euro==1 or euro==2 or euro==5 or euro==10):
                print("Your bet is :%d "%euro)
                break
            else:
                print("Wrong betting, please give again")
#Draw
        print("The winning numbers are:")
        a=sorted(random.sample(range(1,81),20))
        print (a)

        n=0
        for i in NOUMERA:
            if i in a:
                n+=1
        print("You have found %d numbers" %n)
        if n==1:
            k=euro*2.5
            print("You won %.2f €"%k)
        else:
            print("Sorry you lost")
    elif (epilogh=='2'):
        print("You wish to play with %s numbers"%epilogh)
        duo=0
        NOUMERA=[]
        while duo<2:
            noumera=int(input("Give the numbers you wish to play (1-80) :"))
            if (noumera not in NOUMERA) and (1<= noumera <=80) and type(noumera) == type(81):
                print("You have choosen the number %d" %noumera)
                NOUMERA.append(noumera)
                duo+=1
            else:
                print("You selected wrong numbers, please give again")
        while True:
            euro=int(input("Give the amount that you wish to bet (1,2,5,10)"))
            if (euro==1 or euro==2 or euro==5 or euro==10):
                print("Your bet is :%d "%euro)
                break
            else:
                print("Wrong betting, please give again")
        print("The winning numbers are:")
        a=sorted(random.sample(range(1,81),20))
        print (a)

        n=0
        for i in NOUMERA:
            if i in a:
                n+=1
        print("You have found %d numbers" %n)
        if n==1:
            k=euro*1
            print("You won %.2f €"%k)
        elif n==2:
            k=euro*5
            print("You won %.2f €"%k)
        else:
            print("Sorry you lost")
    elif (epilogh=='3'):
        print("You wish to play with %s numbers"%epilogh)
        three=0
        NOUMERA=[]
        while three<3:
            noumera=int(input("Give the numbers you wish to play (1-80) :"))
            if (noumera not in NOUMERA) and (1<= noumera <=80) and type(noumera) == type(81):
                print("You have choosen the number %d" %noumera)
                NOUMERA.append(noumera)
                three+=1
            else:
                print("You selected wrong numbers, please give again")
        while True:
            euro=int(input("Give the amount that you wish to bet (1,2,5,10)"))
            if (euro==1 or euro==2 or euro==5 or euro==10):
                print("Your bet is :%d "%euro)
                break
            else:
                print("Wrong betting, please give again")
        print("The winning numbers are:")
        a=sorted(random.sample(range(1,81),20))
        print (a)

        n=0
        for i in NOUMERA:
            if i in a:
                n+=1
        print("You have found %d numbers" %n)
        if n==2:
            k=euro*2.5
            print("You won %.2f €"%k)
        elif n==3:
            k=euro*25
            print("You won %.2f €"%k)
        else:
            print("Sorry you lost")
    elif (epilogh=='4'):
        print("You wish to play with %s numbers"%epilogh)
        four=0
        NOUMERA=[]
        while four<4:
            noumera=int(input("Give the numbers you wish to play (1-80) :"))
            if (noumera not in NOUMERA) and (1<= noumera <=80) and type(noumera) == type(81):
                print("You have choosen the number %d" %noumera)
                NOUMERA.append(noumera)
                four+=1
            else:
                print("You selected wrong numbers, please give again")
        while True:
            euro=int(input("Give the amount that you wish to bet (1,2,5,10)"))
            if (euro==1 or euro==2 or euro==5 or euro==10):
                print("Your bet is :%d "%euro)
                break
            else:
                print("Wrong betting, please give again")
        print("The winning numbers are:")
        a=sorted(random.sample(range(1,81),20))
        print (a)

        n=0
        for i in NOUMERA:
            if i in a:
                n+=1
        print("You have found %d numbers" %n)
        if n==2:
            k=euro*1
            print("You won %.2f €"%k)
        elif n==3:
            k=euro*4
            print("You won %.2f €"%k)
        else:
            print("Sorry you lost")
    elif (epilogh=='5'):
        print("You wish to play with %s numbers"%epilogh)
        five=0
        NOUMERA=[]
        while five<5:
            noumera=int(input("Give the numbers you wish to play (1-80) :"))
            if (noumera not in NOUMERA) and (1<= noumera <=80) and type(noumera) == type(81):
                print("You have choosen the number %d" %noumera)
                NOUMERA.append(noumera)
                five+=1
            else:
                print("You selected wrong numbers, please give again")
        while True:
            euro=int(input("Give the amount that you wish to bet (1,2,5,10)"))
            if (euro==1 or euro==2 or euro==5 or euro==10):
                print("Your bet is :%d "%euro)
                break
            else:
                print("Wrong betting, please give again")
        print("The winning numbers are:")
        a=sorted(random.sample(range(1,81),20))
        print (a)

        n=0
        for i in NOUMERA:
            if i in a:
                n+=1
        print("You have found %d numbers" %n)
        if n==3:
            k=euro*2
            print("You won %.2f €"%k)
        elif n==4:
            k=euro*20
            print("You won %.2f €"%k)
        elif n==5:
            k=euro*450
            print("You won %.2f €"%k)
        else:
            print("Sorry you lost")
    elif (epilogh=='6'):
        print("You wish to play with %s numbers"%epilogh)
        six=0
        NOUMERA=[]
        while six<6:
            noumera=int(input("Give the numbers you wish to play (1-80) :"))
            if (noumera not in NOUMERA) and (1<= noumera <=80) and type(noumera) == type(81):
                print("You have choosen the number %d" %noumera)
                NOUMERA.append(noumera)
                six+=1
            else:
                print("You selected wrong numbers, please give again")
        while True:
            euro=int(input("Give the amount that you wish to bet (1,2,5,10)"))
            if (euro==1 or euro==2 or euro==5 or euro==10):
                print("Your bet is :%d "%euro)
                break
            else:
                print("Wrong betting, please give again")
        print("The winning numbers are:")
        a=sorted(random.sample(range(1,81),20))
        print (a)

        n=0
        for i in NOUMERA:
            if i in a:
                n+=1
        print("You have found %d numbers" %n)
        if n==3:
            k=euro*1
            print("You won %.2f €"%k)
        elif n==4:
            k=euro*7
            print("You won %.2f €"%k)
        elif n==5:
            k=euro*50
            print("You won %.2f €"%k)
        elif n==6:
            k=euro*1600
            print("You won %.2f €"%k)
        else:
            print("Sorry you lost")
    elif (epilogh=='7'):
        print("You wish to play with %s numbers"%epilogh)
        seven=0
        NOUMERA=[]
        while seven<7:
            noumera=int(input("Give the numbers you wish to play (1-80) :"))
            if (noumera not in NOUMERA) and (1<= noumera <=80) and type(noumera) == type(81):
                print("You have choosen the number %d" %noumera)
                NOUMERA.append(noumera)
                seven+=1
            else:
                print("You selected wrong numbers, please give again")
        while True:
            euro=int(input("Give the amount that you wish to bet (1,2,5,10)"))
            if (euro==1 or euro==2 or euro==5 or euro==10):
                print("Your bet is :%d "%euro)
                break
            else:
                print("Wrong betting, please give again")
        print("The winning numbers are:")
        a=sorted(random.sample(range(1,81),20))
        print (a)

        n=0
        for i in NOUMERA:
            if i in a:
                n+=1
        print("You have found %d numbers" %n)
        if n==3:
            k=euro*1
            print("You won %.2f €"%k)
        elif n==4:
            k=euro*3
            print("You won %.2f €"%k)
        elif n==5:
            k=euro*20
            print("You won %.2f €"%k)
        elif n==6:
            k=euro*100
            print("You won %.2f €"%k)
        elif n==7:
            k=euro*5000
            print("You won %.2f €"%k)
        else:
            print("Sorry you lost")
    elif (epilogh=='8'):
        print("You wish to play with %s numbers"%epilogh)
        eight=0
        NOUMERA=[]
        while eight<8:
            noumera=int(input("Give the numbers you wish to play (1-80) :"))
            if (noumera not in NOUMERA) and (1<= noumera <=80) and type(noumera) == type(81):
                print("You have choosen the number %d" %noumera)
                NOUMERA.append(noumera)
                eight+=1
            else:
                print("You selected wrong numbers, please give again")
        while True:
            euro=int(input("Give the amount that you wish to bet (1,2,5,10)"))
            if (euro==1 or euro==2 or euro==5 or euro==10):
                print("Your bet is :%d "%euro)
                break
            else:
                print("Wrong betting, please give again")
        print("The winning numbers are:")
        a=sorted(random.sample(range(1,81),20))
        print (a)

        n=0
        for i in NOUMERA:
            if i in a:
                n+=1
        print("You have found %d numbers" %n)
        if n==4:
            k=euro*2
            print("You won %.2f €"%k)
        elif n==5:
            k=euro*10
            print("You won %.2f €"%k)
        elif n==6:
            k=euro*50
            print("You won %.2f €"%k)
        elif n==7:
            k=euro*1000
            print("You won %.2f €"%k)
        elif n==8:
            k=euro*1500
            print("You won %.2f €"%k)
        else:
            print("Sorry you lost")
    elif (epilogh=='9'):
        print("You wish to play with %s numbers"%epilogh)
        nine=0
        NOUMERA=[]
        while nine<9:
            noumera=int(input("Give the numbers you wish to play (1-80) :"))
            if (noumera not in NOUMERA) and (1<= noumera <=80) and type(noumera) == type(81):
                print("You have choosen the number %d" %noumera)
                NOUMERA.append(noumera)
                nine+=1
            else:
                print("You selected wrong numbers, please give again")
        while True:
            euro=int(input("Give the amount that you wish to bet (1,2,5,10)"))
            if (euro==1 or euro==2 or euro==5 or euro==10):
                print("Your bet is :%d "%euro)
                break
            else:
                print("Wrong betting, please give again")
        print("The winning numbers are:")
        a=sorted(random.sample(range(1,81),20))
        print (a)

        n=0
        for i in NOUMERA:
            if i in a:
                n+=1
        print("You have found %d numbers" %n)
        if n==4:
            k=euro*1
            print("You won %.2f €"%k)
        elif n==5:
            k=euro*5
            print("You won %.2f €"%k)
        elif n==6:
            k=euro*25
            print("You won %.2f €"%k)
        elif n==7:
            k=euro*200
            print("You won %.2f €"%k)
        elif n==8:
            k=euro*4000
            print("You won %.2f €"%k)
        elif n==9:
            k=euro*40000
            print("You won %.2f €"%k)
        else:
            print("Sorry you lost")
    elif (epilogh=='10'):
        print("You wish to play with %s numbers"%epilogh)
        ten=0
        NOUMERA=[]
        while ten<10:
            noumera=int(input("Give the numbers you wish to play (1-80) :"))
            if (noumera not in NOUMERA) and (1<= noumera <=80) and type(noumera) == type(81):
                print("You have choosen the number %d" %noumera)
                NOUMERA.append(noumera)
                ten+=1
            else:
                print("You selected wrong numbers, please give again")
        while True:
            euro=int(input("Give the amount that you wish to bet (1,2,5,10)"))
            if (euro==1 or euro==2 or euro==5 or euro==10):
                print("Your bet is :%d "%euro)
                break
            else:
                print("Wrong betting, please give again")
        print("The winning numbers are:")
        a=sorted(random.sample(range(1,81),20))
        print (a)

        n=0
        for i in NOUMERA:
            if i in a:
                n+=1
        print("You have found %d numbers" %n)
        if n==0:
            k=euro*2
            print("You won %.2f €"%k)
        elif n==5:
            k=euro*2
            print("You won %.2f €"%k)
        elif n==6:
            k=euro*20
            print("You won %.2f €"%k)
        elif n==7:
            k=euro*80
            print("You won %.2f €"%k)
        elif n==8:
            k=euro*500
            print("You won %.2f €"%k)
        elif n==9:
            k=euro*10000
            print("You won %.2f €"%k)
        elif n==10:
            k=euro*100000
            print("You won %.2f €"%k)
        else:
            print("Sorry you lost")
    elif (epilogh=='11'):
        print("You wish to play with %s numbers"%epilogh)
        eleven=0
        NOUMERA=[]
        while eleven<11:
            noumera=int(input("Give the numbers you wish to play (1-80) :"))
            if (noumera not in NOUMERA) and (1<= noumera <=80) and type(noumera) == type(81):
                print("You have choosen the number %d" %noumera)
                NOUMERA.append(noumera)
                eleven+=1
            else:
                print("You selected wrong numbers, please give again")
        while True:
            euro=int(input("Give the amount that you wish to bet (1,2,5,10)"))
            if (euro==1 or euro==2 or euro==5 or euro==10):
                print("Your bet is :%d "%euro)
                break
            else:
                print("Wrong betting, please give again")
        print("The winning numbers are:")
        a=sorted(random.sample(range(1,81),20))
        print (a)

        n=0
        for i in NOUMERA:
            if i in a:
                n+=1
        print("You have found %d numbers" %n)
        if n==0:
            k=euro*2
            print("You won %.2f €"%k)
        elif n==5:
            k=euro*1
            print("You won %.2f €"%k)
        elif n==6:
            k=euro*10
            print("You won %.2f €"%k)
        elif n==7:
            k=euro*50
            print("You won %.2f €"%k)
        elif n==8:
            k=euro*250
            print("You won %.2f €"%k)
        elif n==9:
            k=euro*1500
            print("You won %.2f €"%k)
        elif n==10:
            k=euro*15000
            print("You won %.2f €"%k)
        else:
            print("Sorry you lost")
    elif (epilogh=='12'):
        print("You wish to play with %s numbers"%epilogh)
        twelve=0
        NOUMERA=[]
        while twelve<12:
            noumera=int(input("Give the numbers you wish to play (1-80) :"))
            if (noumera not in NOUMERA) and (1<= noumera <=80) and type(noumera) == type(81):
                print("You have choosen the number %d" %noumera)
                NOUMERA.append(noumera)
                twelve+=1
            else:
                print("You selected wrong numbers, please give again")
        while True:
            euro=int(input("Give the amount that you wish to bet (1,2,5,10)"))
            if (euro==1 or euro==2 or euro==5 or euro==10):
                print("Your bet is :%d "%euro)
                break
            else:
                print("Wrong betting, please give again")
        print("The winning numbers are:")
        a=sorted(random.sample(range(1,81),20))
        print (a)

        n=0
        for i in NOUMERA:
            if i in a:
                n+=1
        print("You have found %d numbers" %n)
        if n==0:
            k=euro*4
            print("You won %.2f €"%k)
        elif n==6:
            k=euro*5
            print("You won %.2f €"%k)
        elif n==7:
            k=euro*25
            print("You won %.2f €"%k)
        elif n==8:
            k=euro*150
            print("You won %.2f €"%k)
        elif n==9:
            k=euro*1000
            print("You won %.2f €"%k)
        elif n==10:
            k=euro*2500
            print("You won %.2f €"%k)
        elif n==11:
            k=euro*25000
            print("You won %.2f €"%k)
        elif n==12:
            k=euro*1000000
            print("You won %.2f €"%k)
        else:
            print("Sorry you lost")
    elif (epilogh=='0'):
        break
        
    
