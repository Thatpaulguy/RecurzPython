running = "y"
print (" Welcome to recursion in Python ")


while running != "n":

    def factorial(reCur):
      if reCur < 1:
        return 1
      else:
        return reCur * factorial(reCur - 1)


    def fibonacci(reCur):     
       if reCur == 0:
        return 0
       elif reCur == 1: 
        return 1
       else:
           return fibonacci(reCur -1 ) + fibonacci(reCur -2)


    i = 0



    ##print ("Recursion in Python. \n Would you like to do a F(a)ctorial or F(i)bonacci")
    choice = input("\n Would you like to do a F(a)ctorial or F(i)bonacci? ")


    if choice == 'a':
     ## print ("\n Factorial")
      reCur = int(input("\n Which number would you like to factor? "))
      print (" \n Your choice is ",reCur)
      if reCur > 1:
       print (" " , factorial(reCur))
      else: print(" which is less than 2") 
      running = (input(" Would you like to try again? "))

    elif choice == 'i':

      ## print ("\n Fibonacci")
      reCur = int(input("\n How many numbers in the series? "))
      print (" \n your choice is ", reCur)
      if reCur < 1:
          print(" whuch is less then one")
      while i < reCur:
           print (" ", fibonacci(i) )
           i += 1
      running = (input(" Would you like to try again? "))

    else: 

        print ("\n Not going to happen")
        running = (input(" Would you like to try again? "))



