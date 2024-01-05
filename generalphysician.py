def generalphysician():
    temp=int(input("Enter Temperature in fahrenheit"))
    days=int(input("Enter no of days u r suffering frm fever"))
    cold=input("input yes if u have cold and bodypain")
    if(temp>100 and days>2 and cold=='yes'):
        print("You have a viral fever")
        print("Use Dolo 650 for 3 days for 3 tyms a day")
    elif(temp>=101 and days>3):
        print("Take a blood test for typhoid and dengue at nearest laboratory")
        print("Take Dolo 650 for every 6 hrs and cefixime-for once a day.....Till u take a test blood test")
generalphysician()








