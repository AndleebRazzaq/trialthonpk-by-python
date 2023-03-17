class triathlon:
    def __init__ (self, name, address ,contno):
        self.name=name
        self.address=address
        self.contno=contno
    def dispData(self):
        print (self.name)
        print (self.address)
        print (self.contno)
        print ("##################")
class event:
    def __init__ (self, name, venue, timing, date):
        self.name=name
        self.venue=venue
        self.timing=timing
        self.date=date
    def dispData(self):
       print (self.name)
       print (self.venue)
       print (self.timing) 
       print (self.date)
       print ("##################")
class trainees:
    def __init__ (self, name, Id, physicalparameters):
        self.name=name
        self.Id=Id
        self.physicalparameters=physicalparameters
    def dispData(self):
        print (self.name)
        print (self.Id)
        print (self.physicalparameters)
        print ("###################")
class trainers:
    def __init__ (self, name, Id, skills):
        self.name=name
        self.Id=Id
        self.skills=skills
    def dispData(self):
        print (self.name)
        print (self.Id)
        print (self.skills)
        print ("###################")
class sports:
    def __init__ (self, Gamesname, timing, participants):
        self.Gamesname=Gamesname
        self.timing=timing
        self.participants=participants 
    def dispData(self):
        print (self.Gamesname)
        print (self.timing)
        print (self.participants)
        print ("######################")
inst=triathlon ("abc","multan cantt",347125994)
inst.dispData()
event1=event("opening ceremony","mango ground","12:30","1-2-23")
event1.dispData()
event2=event("result annnouncement","mango ground","1:00","4-2-23")
event2.dispData()
std1=trainees ("ali","Aligmail.com","BP,weight")
std1.dispData()
std2=trainees("umer","umergmail.com","BP,weight")
std2.dispData()
trainer1=trainers ("alina","linagmail.com","programmer")
trainer1.dispData()
trainer2=trainers ("sania","sanigmail.com","computer engineering")
trainer2.dispData()
game1=sports ("swimming","2:00",10)
game1.dispData()
game2=sports("cycling","3:00",8)
game2.dispData()