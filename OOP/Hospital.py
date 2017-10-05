class Patient(object):
    count = 0
    counter = 0
    def __init__(self, id, name, allergies, bed_number = None):
        self.id = Patient.count
        Patient.count += 1
        self.bed_number = Patient.counter
        Patient.counter += 1
        self.name = name
        self.allergies = allergies

    def display(self):
        print self.id, self.name, self.allergies, self.bed_number

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
    
    def display_info(self):
        print self.patients, self.name, self.capacity
        
    def admitted(self, Patient):
        if len(self.patients) >= self.capacity:
            print "Im sorry but our capacity is " + str(self.capacity)
        else:
            self.patients.append(Patient)
            print self.patients
    
    def discharged(self, Patient):
        for i in self.patients:
            if i.id == Patient.id:
                self.patients.pop(i.id)
                self.bed_number = None

Patient1 = Patient(id, "David", "Shellfish")
Patient2 = Patient(id, "Virginia", "alcohol")
Hospital1 = Hospital( "Northwestern", 50)  
Hospital1.admitted(Patient1)
Hospital1.admitted(Patient2)
# Patient1.display()
# Patient2.display()
Hospital1.discharged(Patient2)
Hospital1.display_info()