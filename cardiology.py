def cardiology():
    sleep=input("input yes or no do u have good sleep at ngt")
    tiredness=input("input yes or no if u have tiredness while climbing steps")
    Ef=int(input("enetr ef"))
    cholestrol=int(input("Eneter cholestrol"))
    if(Ef<=25 and tiredness=='yes' and sleep=='yes'):
        print("You have a Heart Failure")
        print("Consult Dr.Sreenivasa Raju an Internationl cardiologist at KIIMS Nellore")
    elif(cholestrol>160 and sleep=='no' and tiredness=='yes' and Ef>25):
        print("U have a high cholestrol")
        print("There a chance of Heart stoke....")
        print("Consult Cardiologist ASAP")

cardiology()
