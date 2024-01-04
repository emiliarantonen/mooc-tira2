class CoursePlan:
    def __init__(self):
        self.vaatimukset = {}
    
    def add_course(self,course):
        self.vaatimukset[course] = []

    def add_requisite(self,course1,course2):
        self.vaatimukset[course1].append(course2)


    def find_order(self):
        jarjestely = []
        kayty_lapi = dict.fromkeys(self.vaatimukset, 0)
        self.looppi = False
        for course in self.vaatimukset.keys():
            if kayty_lapi[course] == 0:
                self.kurssin_etsinta(course, kayty_lapi, jarjestely)
            if self.looppi:
                return
        return list(reversed(jarjestely))

    def kurssin_etsinta(self, course, kayty_lapi, jarjestely):
        if kayty_lapi[course] == 2:
            return
        if kayty_lapi[course] == 1:
            self.looppi = True
            return
        kayty_lapi[course] = 1
        for requisite in self.vaatimukset[course]:
            self.kurssin_etsinta(requisite, kayty_lapi, jarjestely)
        kayty_lapi[course] = 2
        jarjestely.append(course)  

if __name__ == "__main__":
    c = CoursePlan()
    c.add_course("Ohpe")
    c.add_course("Ohja")
    c.add_course("Tira")
    c.add_course("Jym")
    c.add_requisite("Ohpe", "Ohja")
    c.add_requisite("Ohja", "Tira")
    c.add_requisite("Jym", "Tira")
    print(c.find_order()) # esim. [Ohpe, Jym, Ohja, Tira]
    c.add_requisite("Tira", "Tira")
    print(c.find_order()) # None