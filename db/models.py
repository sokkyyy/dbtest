from django.db import models
from django.contrib.auth.models import User



class Role(models.Model):
    '''Model for Staff Role in System'''

    role_choices = [
        ('super_admin', 'Super Admin'),
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

    def __str__(self):
        return self.grade

class Department(models.Model):
    '''Model for Moringa DEpartments'''


    department_names_choices = [
        ('system_admin','System Admin'), #ONLY FOR SYSTEM ADMIN
        
        ('finance','Finance'),
        ('hr', 'Human Resource'),
        ('people','People'),
        ('classroom','Classroom'),
    ]
    name = models.CharField(max_length=30,choices=department_names_choices)
    manager = models.OneToOneField(User, on_delete=models.CASCADE,related_name='department_manager')
    line_manager = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MoringaStaff(models.Model):
    ''' Model for All Moringa Staff Members '''

    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    job_grade = models.ForeignKey(JobGrade, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    system_role = models.ForeignKey(Role,on_delete=models.CASCADE)




class Organization(models.Model):
    """Model for Organization Competency Ratings """

    planning = models.IntegerField()
    execution = models.IntegerField()
    prioritization = models.IntegerField()
    score = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)

    


class Innovation(models.Model):
    """Model for Innovation Competency Ratings """

    vision_setting = models.IntegerField()
    thinking = models.IntegerField() #thinking_out_of_the_box
    adaptability = models.IntegerField()
    score = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)




class InterpersonalCommunication(models.Model):
    """Model for Interpersonal Communication Competency Ratings """

    investment_building = models.IntegerField()
    effective_communication = models.IntegerField()
    delivery = models.IntegerField() #delivering the message(method + structure)
    score = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)


class CriticalThinking(models.Model):
    """Model for Critical Thinking Competency Ratings """


    data_compilation = models.IntegerField()
    data_analysis = models.IntegerField()
    problem_solving = models.IntegerField()
    continual_improvement= models.IntegerField()
    score = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)


class Relationships(models.Model): #Building and Managing Relationships
    """Model for Relationships Competency Ratings """


    team_work = models.IntegerField()
    stakeholder_management = models.IntegerField()
    conflict_management = models.IntegerField()
    score = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)


class CompetencyResults(models.Model):
    '''Model to Consolidate Competency Ratings'''

    evaluation_type_choices = [
        ('self', 'Self'),
        ('manager', 'Manager'),
        ('final','Final'),
    ]
    type = models.CharField(max_length=30, choices=evaluation_type_choices)
    staff = models.ForeignKey(MoringaStaff, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    innovation = models.ForeignKey(Innovation, on_delete=models.CASCADE)
    interpersonal_communication = models.ForeignKey(InterpersonalCommunication, on_delete=models.CASCADE)
    critical_thinking = models.ForeignKey(CriticalThinking, on_delete=models.CASCADE)
    relationships = models.ForeignKey(Relationships, on_delete=models.CASCADE)
    last_modified = models.DateField(auto_now=True) #changes on every update
    date_created = models.DateField(auto_now_add=True)
