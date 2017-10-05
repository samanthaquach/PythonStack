class Call(object): 

    def __init__(self,uniqueId,callerName,callerPhone,TimeCall,ReasonCall):
        self.uniqueId = uniqueId
        self.callerName = callerName
        self.callerPhone = callerPhone
        self.TimeCall = TimeCall
        self.ReasonCall = ReasonCall

    def display_all(self):
        print('Caller ID: ' + str(self.uniqueId))
        print('Name: ' + str(self.callerName))
        print('Number: ' + str(self.callerPhone))
        print('Time: ' + str(self.TimeCall))
        print('Reason: ' + str(self.ReasonCall))
        print 
        return self

class CallCenter(object):

    def __init__(self):
        self.queue_size = 0
        self.callList = []
        # for num in self.callList:
        #         if num < 5:
        #             del self.callList[0]
        #             self.queue_size -= 1
    
    def add_num(self,uniqueId,callerName,callerPhone,TimeCall,ReasonCall):
        new_call=Call(uniqueId,callerName,callerPhone,TimeCall,ReasonCall)
        self.callList.append(new_call)
        self.queue_size=(len(self.callList))

        return self

    def info_call(self):
        for x in self.callList:
            print x.callerName, x.callerPhone, self.queue_size
            for num in self.callList:
                if num < 5:
                    del self.callList[0]
                    self.queue_size -= 1
            

        return self
        

Caller1 = Call(100,"Jane",7732278899,"8:00PM","Stomach Flu").display_all()
Caller2 = Call(101,"Bob",7738982020, "9:10PM","Broken Bones").display_all()

Clinic=CallCenter()
Clinic.add_num(102,"Karen",6320190078,"9:20PM","Hives")
Clinic.info_call()
Clinic.add_num(103,"Eric",3320190078,"9:32PM","Eye gauge")
Clinic.info_call()
Clinic.add_num(104,"Brian",2320190078,"9:33PM","Heart burn")
Clinic.info_call()
Clinic.add_num(105,"Kevin",2320190078,"9:33PM","Heart burn")
Clinic.info_call()
Clinic.add_num(106,"Brian",2320190078,"9:42PM","Heart burn")
Clinic.info_call()
Clinic.add_num(106,"Alex",2320190078,"9:42PM","Heart burn")
Clinic.info_call()

    