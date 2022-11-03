
class course:
    def __init__(self, prepare, perform, reherse):
        self.prepare = prepare
        self.perform = perform
        self.reherse = reherse

    def get_prepare(self):
        total=0
        for i in self.prepare:
            total+=i
        return total/len(self.prepare)
    def get_perform(self):
        total=0
        for i in self.perform:
            total+=i
        return total/len(self.perform)
    def get_reherse(self):
        total=0
        for i in self.reherse:
            total+=i
        return total/len(self.reherse)
    def get_grade(self):
        grade=0
        grade+=self.get_perform()*.5
        grade+=self.get_prepare()*.2
        grade+=self.get_reherse()*.3
        print(grade)
        print(self.get_perform())
        print(self.get_prepare())
        print(self.get_reherse())

history=course([100,90,50,100,100,100,100,100,100],[65,50,85],[90,50,50,50,95,50,95])
# history.get_grade()

math = course([100,100,100,50,50,50,50,50,50],[86,77,75,70],[100,70,50,90,100,90,60,50,100  ])
math.get_grade()
