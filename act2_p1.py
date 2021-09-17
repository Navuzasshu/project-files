print("This program will print student averages. Enter your scores! ")

#Initialize Variables 
prelims=float(input("Enter your prelims score: "))
midterms=float(input("Enter your midterms score: "))
semis=float(input("Enter your semifinals score: "))
finals=float(input("Enter your finals score: "))

#compute average
avg=(prelims+midterms+semis+finals)/4

print("Your average is {}!".format(avg))