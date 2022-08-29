class Patient:

    patient_list = []
    total_bill = []

    def __init__(self, name, age, disease, bill):
        self.name = name 
        self.age = age
        self.disease = disease
        self.bill = bill

    def corona_patient(self):
        if self.age < 25 and self.disease == "Corona":
            self.patient_list.append(self.name)
            self.total_bill.append(self.bill)

            return f"Corona Patients are: {self.patient_list} and their average bill is {sum(self.total_bill)/len(self.patient_list)}"

p1 = Patient("p1", 20, "Corona", 18000)
p2 = Patient("p2", 26, "Fever", 6000)
p3 = Patient("p3", 29, "Corona", 8000)
p4 = Patient("p4", 23, "Corona", 12000)

p1.corona_patient()
p2.corona_patient()
p3.corona_patient()
p4.corona_patient()

a = Patient.total_bill
b = Patient.patient_list

print(f"Corona Patients are: {b} and their average bill is {sum(a)/len(b)}")