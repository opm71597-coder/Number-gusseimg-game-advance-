from random import randint
from time import sleep

class game:
    def __init__(self):
        while True:
            print("1.one time gauuse num")
            print("2.lavel shocol")
            print("3.exit")
            x=input("enter :")
            if(x=="3"):
                break
            elif(x=="1"):
                attept=0
                try:
                 num_range=int(input("enter what range you whant a number :"))
                 print("gussing number ....")
                 sleep(3)
                 num_x=randint(1,num_range)
                 print("number gusse")
                except:
                 print("invalid input")
                try:
                 while True:
                  num=int(input("enter your number :"))
                  if(num==num_x):
                   print("you win ")
                   print("you have attept:",attept+1)
                   break
                  elif(num>num_x):
                   print("lower than ",num)
                   attept+=1
                  else:
                   print("high then")
                   attept+=1
                except:
                 print("invalid input")
                 print("clic enter ")
            elif(x=="2"):
             point=0
             attept=0
             while True:
              print("1.low")
              print("2.midium")
              print("3.high")
              print("4.exit")
              x=input("enter level diffculty :") 
              if(x=="4"):
               break
              elif(x=="1"):
               num_l_r=randnt(1,100)
              elif(x=="2"):
               num_l_r=randint(1,1000)
              elif(x=="3"):
               num_l_r=randint(1000,10000)
              else:
               print("chuse a num")
              try:
               print("if you whant to exit enter 0")
               while True:
                print(f"point:{point}")
                num=int(input("gusse the number :"))
                if(num==num_l_r):
                 print("bingoooooooooooo.....")
                 print("you win the +1")
                 print("attept:",attept)
                elif(num>num_l_r):
                 print("number in lower the ",num)
                 attept+=1
                elif(num==0):
                 break
                else:
                 print("number higher than ",num)
                 attept+=1
              except:
               print("invlid input")




game_numgu=game()
