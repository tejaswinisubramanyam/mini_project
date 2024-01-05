def pediatrician():
    problem=input("Enter problem")
    if(problem in ("mucus","cough")):
        days=int(input("Enter days"))
        print("Use zarbee's Natural syrup for 5 days......With dosage of 5ml per day")
    elif(problem=="stomach pain"):
        print("Use SELA syrup with the dosage of 5ml per day")
    elif(problem in ("fever","cold") ):
       temp=int(input("Enter temp:"))
       days=int(input("enter days:"))
       print("Ur child is running with high temperature")
       if(temp>100 and days<3):
           print("It's just a viral Fever")


pediatrician()
