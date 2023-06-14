from rest_framework import serializers

from .models import Students, Score

# score 모델을 추가해주세요.
# 학생들은 총 여러번의 시험을 볼 수 있습니다.
# 컬럼을 english, math, science에 대한 점수를 기록할 수 있고, 어떤 학생이 언제 본 시험인지도 기록할 수 있도록 해주세요. 

# Serializer도 추가해주세요.

# score_view 도 GET으로 만들기



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['name', 'address', 'email']
        # fields = '__all__'

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['english', 'math', 'science', 'exam_date', 'student']