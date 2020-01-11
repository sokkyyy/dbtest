from django.db import models
from django.contrib.auth.models import User



class Role(models.Model):
    '''Model for Staff Role in System'''

    role_choices = [
        ('super_admin', 'Super Admin' )
        ('admin', 'Admin'),
        ('user', 'System User'),

    ]
    role = models.CharField(max_length=20,choices=role_choices)

    def __str__(self):
        return self.role


class JobGrade(models.Model):
    '''Model for Job Grades'''

    moringa_job_grade_choices = [
        ('12','12'), #champion

        ('11','11'), #experts
        ('10','10'),

        ('9','9'), #practitioner
        ('8','8'),
        ('7','7'),
        ('6','6'),
        ('TM-3','TM-3'),
        ('TM-2','TM-2'),

        ('TM-1','TM-1'),#beginner
        ('TM-0','TM-0'),
        ('5','5'),
        ('4','4'),
        ('1','1'),
    ]
    grade = models.CharField(max_length=10, choices=moringa_job_grade_choices,)

class Department(models.Model):
    '''Model for Moringa DEpartments'''


    department_names_choices = [
        ('finance','Finance'),
        ('hr', 'Human Resource'),
        ('people','People'),
        ('classroom','Classroom'),
    ]
    name = models.CharField(max_length=30,choices=department_names_choices)
    manager = models.OneToOneField(User, on_delete=models.CASCADE,related_name='department_manager')
    line_manager = models.OneToOneField(User, on_delete=models.CASCADE)

class MoringaStaff(models.Model):
    '''Model for All Moringa Staff Members'''

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_grade = models.ForeignKey(JobGrade, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    system_role = models.ForeignKey(Role,on_delete=models.CASCADE)


class Organization(models.Model):
    """Model for Organization Competency Ratings """

    evaluation_type_choices = [
        ('self', 'Self'),
        ('manager', 'Manager'),
        ('final','Final'),
    ]
    planning = models.IntegerField()
    execution = models.IntegerField()
    prioritization = models.IntegerField()
    average = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)
    last_modified = models.DateField(auto_now=True) #changes on every update
    date_created = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=30, choices=evaluation_type_choices)
    staff = models.ForeignKey(MoringaStaff, on_delete=models.CASCADE)

class Innovation(models.Model):
    """Model for Innovation Competency Ratings """

    evaluation_type_choices = [
        ('self', 'Self'),
        ('manager', 'Manager'),
        ('final','Final'),
    ]

    vision_setting = models.IntegerField()
    thinking = models.IntegerField() #thinking_out_of_the_box
    adaptability = models.IntegerField()
    average = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)
    date = models.DateField(auto_now=True)
    type = models.CharField(max_length=30, choices=evaluation_type_choices)
    staff = models.ForeignKey(MoringaStaff, on_delete=models.CASCADE)



class InterpersonalCommunication(models.Model):
    """Model for Interpersonal Communication Competency Ratings """

    evaluation_type_choices = [
        ('self', 'Self'),
        ('manager', 'Manager'),
        ('final','Final'),
    ]
    investment_building = models.IntegerField()
    effective_communication = models.IntegerField()
    delivery = models.IntegerField() #delivering the message(method + structure)
    average = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)
    last_modified = models.DateField(auto_now=True) #changes on every update
    date_created = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=30, choices=evaluation_type_choices)
    staff = models.ForeignKey(MoringaStaff, on_delete=models.CASCADE)

class CriticalThinking(models.Model):
    """Model for Critical Thinking Competency Ratings """

    evaluation_type_choices = [
        ('self', 'Self'),
        ('manager', 'Manager'),
        ('final','Final'),
    ]
    data_compilation = models.IntegerField()
    data_analysis = models.IntegerField()
    problem_solving = models.IntegerField()
    continual_improvement= models.IntegerField()
    average = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)
    last_modified = models.DateField(auto_now=True) #changes on every update
    date_created = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=30, choices=evaluation_type_choices)
    staff = models.ForeignKey(MoringaStaff, on_delete=models.CASCADE)

class Relationships(models.Model): #Building and Managing Relationships
    """Model for Relationships Competency Ratings """

    evaluation_type_choices = [
        ('self', 'Self'),
        ('manager', 'Manager'),
        ('final','Final'),
    ]
    team_work = models.IntegerField()
    stakeholder_management = models.IntegerField()
    conflict_management = models.IntegerField()
    average = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)
    last_modified = models.DateField(auto_now=True) #changes on every update
    date_created = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=30, choices=evaluation_type_choices)
    staff = models.ForeignKey(MoringaStaff, on_delete=models.CASCADE)
