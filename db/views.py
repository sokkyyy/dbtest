from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,permissions
from .models import *
from .serializers.departments import DepartmentSerializer
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from .serializers.competencies import CompetencyResultsSerializer
from .serializers.moringa_staff import MoringaStaffSerializer

# Create your views here.
@api_view(['GET'])
def departments(request):
    '''API endpoint for Moringa Departments'''

    departments = Department.objects.all()
    serializers = DepartmentSerializer(departments, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def competency_results(request):
    '''API endpoint for staff competency results'''

    results = CompetencyResults.objects.all()
    serializers = CompetencyResultsSerializer(results, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def moringa_staff(request):
    ''' API endpoint for staff information '''

    all_staff = MoringaStaff.objects.all()
    serializers = MoringaStaffSerializer(all_staff, many=True)
    return Response(serializers.data)
