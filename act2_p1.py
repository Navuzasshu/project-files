print("This program will print student averages. Enter your scores! ")

#Initialize Variables 
prelims=float(input("Enter your prelims score: "))
midterms=float(input("Enter your midterms score: "))
semis=float(input("Enter your semifinals score: "))
finals=float(input("Enter your finals score: "))

#compute average
avg=(prelims+midterms+semis+finals)/4

print("Your average is {}!".format(avg))
if avg>=75:
    print("Congratulations! You passed!")
    if avg>=99 and <=100:
        print("Your grade is A!")
    elif avg>=90 and <=98:
        print("Your grade is B!")
    elif avg>=80 and <=89:
        print("Your grade is C!")
    elif avg>=75 and <=79:
        print("Your grade is D.")    
elif avg<75:
    print("Unfortunately, you have failed. Do better next time! ")
    if avg>=71 and <=74:
        print("Your grade is D.")
    elif avg>=61 and <=70:
        print("Your grade is E.")