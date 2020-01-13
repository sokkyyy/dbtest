from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,permissions
from .models import *
from .serializers.departments import DepartmentSerializer
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from .serializers.competencies import CompetencyResultsSerializer
from .serializers.moringa_staff import MoringaStaffSerializer
from .serializers.users import UserSerializer, UserSerializerWithToken



# Create your views here.
@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
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
