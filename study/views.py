from rest_framework.decorators import api_view
from rest_framework.views import Response

from .models import Students, Score
from .serializers import StudentSerializer, ScoreSerializer

from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework import viewsets

# ViewSet
class StudentViewSet(viewsets.ModelViewSet):
  queryset = Students.objects.all()
  serializer_class = StudentSerializer


class StudentView(APIView):
  """
  Class Based View
  
  url: /students

  - get: 학생 목록조회
  - post: 학생등록
  """
  def get(self, request):
    qs = Students.objects.filter().all() # 데이터 조회
    serializer = StudentSerializer(qs, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = StudentSerializer(data=request.data) # serializer 
      
    if serializer.is_valid(): # validation check
      serializer.save() # save data to model 
      return Response(serializer.data, status.HTTP_201_CREATED)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class ScoreView(APIView):
  """
  url: /score

  - GET: 스코어 리스트 조회
  - POST: 스코어 등록 
  """
  def get(self, request):
    """
    1. Score모델에서 데이터 조회
    2. ScoreSerializer로 묶은 후
    3. Return 
    """
    qs = Score.objects.all() # 데이터 전체 조회
    serializer = ScoreSerializer(qs, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = ScoreSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
  """
  CBV
  url: /students/<int:pk>

  - get: pk 학생 세부조회
  - put: pk 학생 수정
  - delete: pk 학생 삭제
  """

  def get_object(self, pk):
    return get_object_or_404(Students, pk=pk)

  def get(self, request, pk):
    qs = self.get_object(pk)

    serializer = StudentSerializer(qs)
    return Response(serializer.data)
  
  def put(self, request, pk):
    qs = self.get_object(pk)

    serializer = StudentSerializer(qs, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    qs = self.get_object(pk)
    qs.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def StudentDetailView(request, pk):
#   """
#   FBV
#   url: /students/<int:pk>

#   - get: pk 학생 세부조회
#   - put: pk 학생 수정
#   - delete: pk 학생 삭제
#   """
#   qs = get_object_or_404(Students, pk=pk)
  
#   if request.method == 'GET':
#     serializer = StudentSerializer(qs)
#     return Response(serializer.data)
#   elif request.method == 'PUT':
#     serializer = StudentSerializer(qs, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   elif request.method == 'DELETE':
#     qs.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


###  Function Based View
# @api_view(['GET', 'POST'])
# def StudentView(request):
#     # Students.objects.all()
#     # Students.objects.filter(address='10').all()
#     # Students.objects.get(id=1)
#     # qs: queryset: Student.objects.filter().all() -> QuerySet
#     if request.method == 'GET':
#       qs = Students.objects.filter().all() # 데이터 조회
#       serializer = StudentSerializer(qs, many=True)
#       return Response(serializer.data)
#     elif request.method == 'POST':
#       serializer = StudentSerializer(data=request.data) # serializer 
      
#       if serializer.is_valid(): # validation check
#         serializer.save() # save data to model 
#         return Response(serializer.data, status.HTTP_201_CREATED)

#       return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ScoreDetailView(APIView):
  """
  url: /score/<int:pk> (pk: score의 db pk)

  - GET:  스코어 상세조회
  - PUT:  스코어 수정
  - DELETE:  스코어 삭제
  """

  def get_object(self, pk):
    qs = get_object_or_404(Score, pk=pk)
    return qs

  def get(self, request, pk):
    qs = self.get_object(pk)
    serializer = ScoreSerializer(qs)
    return Response(serializer.data)

  def put(self, request, pk):
    qs = self.get_object(pk)
    serializer = ScoreSerializer(qs, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    qs = self.get_object(pk)
    qs.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




# score 리스트 조회 및 추가
@api_view(['GET', 'POST'])
def score_view(request):
  if request.method == 'GET':
    qs = Score.objects.all() # 데이터 전체 조회
    serializer = ScoreSerializer(qs, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = ScoreSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# score 상세조회, 수정, 삭제
@api_view(['GET' 'PUT', 'DELETE'])
def score_detail_view(request, pk):
  qs = get_object_or_404(Score, pk=pk)

  if request.method == 'GET':
    serializer = ScoreSerializer(qs)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = ScoreSerializer(qs, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    qs.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(["GET", "POST"])
def StudentScoreView(request, pk):
  qs = get_object_or_404(Students, pk=pk)

  if request.method == 'GET':
    scores = qs.score_set.all()
    serializer = ScoreSerializer(scores, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = ScoreSerializer(data={'student':qs.pk, **request.data})
    if serializer.is_valid():
      serializer.save()
      # score = Score(**serializer.data, student=qs).save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)