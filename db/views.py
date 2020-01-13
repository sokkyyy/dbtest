from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status,permissions
from .models import *
from django.contrib.auth.models import User
from .serializers.departments import DepartmentSerializer
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from .serializers.competencies import CompetencyResultsSerializer
from .serializers.moringa_staff import MoringaStaffSerializer,UserSerializer,UserSerializerWithToken

@permission_classes((permissions.AllowAny,))
def signin_jwt_wrapped(request, *args, **kwargs):
    request_data = request.data
    host = request.get_host()
    print(host)
    email = request_data['email']
    
    # get the username for this email by model lookup
    user = User.objects.get(email=email)
    if user.username is None:
        response_text = {"non_field_errors":["Unable to login with provided credentials."]}
        return Response(response_text, status=status.HTTP_400_BAD_REQUEST)


    data = {'username': user.username, 'password':request_data['password']}
    headers = {'content-type': 'application/json'}
    url = 'http://' + host + '/api/token_auth/'
    response = request.post(url,data=dumps(data), headers=headers)

    return Response(loads(response.text), status=response.status_code)

@api_view(['GET','POST'])
def handle_login(request):
    print(request.data)
    return Response(request.data)
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
