class Student:
    
    #creates the students objects
    def __init__(self, name, college_id, gpa):
        self.name = name
        self.college_id = college_id
        self.gpa =gpa

    #puts the together for the printing
    def __str__(self):
        return f'Name: {self.name}, id: {self.college_id}, GPA: {self.gpa}'


def main():
    alice = Student('Alice', 'aa1234aa', 2.72)
    bob = Student('Bob', 'bb1234bb', 3.0)

    print(alice.name)
    print(bob.college_id)

    print(alice)
    print(bob)

main()