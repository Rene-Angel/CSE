class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, job):
        super(Employee, self).__init__(name, age)
        self.job = job

    def get_paid(self):
        print("You got paid for working as a %s" % self.job)


class Programmer(Employee):
    def __init__(self, name, age):
        super(Programmer, self).__init__(name, age, 'Programmer')

    def get_paid(self):
        print("%s got paid for all the programs they coded." % Jeff.name)


Jeff = Programmer('Jeff', 21)
print(Jeff.name)
print(Jeff.age)
print(Jeff.job)
Jeff.work()
Jeff.get_paid()
