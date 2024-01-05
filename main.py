
class patient_details:
    def __init__(self,name,age,gender,contactno,problem):
        self.name=name
        self.age=age
        self.gender=gender
        self.contactno=contactno
        self.problem=problem
    def details(self):
        file=open("detail_of_patient.txt","a")
        file.write("\nNAME\t")
        file.write(self.name)
        file.write("\nAGE\t")
        file.write(str(self.age))
        file.write("\nGENDER\t")
        file.write(self.gender)
        file.write("\nCONTACTNO\t")
        file.write(str(self.contactno))
        file.write("\nPROBLEM\t")
        file.write(self.problem)
        file.write("\n===========================================================================\n")
class diagnosis(patient_details):
    def refer_doctor(self):
        if(self.age<15):
           print("Referring to pediatrician")
           import pediatrician
        elif(self.age<15):
           pediatrician.pediatrician()
        elif(self.age>=15 and self.problem=="Fever"):
             print("Referring to General physician")
             import generalphysician
        elif(self.problem=="Fever"):
             generalphysician.generalphysician()
        elif(self.problem=="Heart"):
            print("Referring to Cardiology")
            import cardiology
        elif(self.problem=='Heart'):
            cardiology.cardiology()
        elif(self.problem=="Eye"):
            print("Referring to Optomologist")
            import optomologist
        elif(self.problem=="Eye"):
            optomologist.optomologist()


name=input("Enter name:")
age=int(input("Enter Age:"))
gender=input("Enter Gender:")
contactno=int(input("Enter contactno:"))
problem=input("Enter Problem:")


obj=diagnosis(name,age,gender,contactno,problem)
obj.details()
obj.refer_doctor()

