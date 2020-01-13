from rest_framework import serializers
from ..models import *

class MoringaStaffSerializer(serializers.ModelSerializer):
    '''API serializer for Moringa Staff Member'''
    job_grade = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    system_role = serializers.SerializerMethodField()

    def get_job_grade(self, moringa_staff):
        return moringa_staff.job_grade.grade

    def get_department(self,moringa_staff):
        return moringa_staff.department.name

    def get_system_role(self,moringa_staff):
        return moringa_staff.system_role.role

    class Meta:
        model = MoringaStaff
        fields = ['pk','job_grade','department','system_role']
