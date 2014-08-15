class Student(object):
    '''An object that specifies a student's name and grade.

    Attributes/fields:
    name - the full name of the student
    grade - the student's current grade
    '''

    def __init__(self, name, grade):
        ''' Initializes both variables in Student(object) '''
        self.name=name
        self.grade=grade

    def letter_grade(self):
        ''' Returns the corresponding letter grade '''
        if self.grade== 4.0:
            return 'A+'
        if self.grade<4.0 and self.grade>3.7:
            return 'A'
        if self.grade<=3.7 and self.grade>3.3:
            return 'A-'
        if self.grade<=3.3 and self.grade>3.0:
            return 'B+'
        if self.grade<=3.0 and self.grade>2.7:
            return 'B'
        if self.grade<=2.7 and self.grade>2.3:
            return 'B-'
        if self.grade<=2.3 and self.grade>2.0:
            return 'C+'
        if self.grade<=2.0 and self.grade>1.7:
            return 'C'
        if self.grade<=1.7 and self.grade>1.3:
            return 'C-'
        if self.grade<=1.3 and self.grade>1.0:
            return 'D+'
        if self.grade<=1.0 and self.grade>0.0:
            return 'D'
        if self.grade==0.0:
            return 'F'

    def __str__(self):
        ''' Formats the variables and letter_grade into type str and is returned '''
        return '{} - {} - {}'.format(self.name, self.grade, self.letter_grade())

s1 = Student('Bob', 3.0)
s2 = Student('Marsha', 3.5)
print s1
print s2
