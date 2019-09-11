from django.db import models

# 1. python manage.py makemigrations => django한테 model 작성했음을 알림
# 2. python manage.py migrate => django 한테 DB에 작성하라고 요청.


class Article(models.Model):
    # id(pk)는 기본적으로 처음 테이블 생성시 자동으로 만들어 진다. 
    # id = models.AutoField(primary_key=True)  <- 요게 자동으로 만들어짐
    # CharField 에서는 max_lenght가 필수 인자임 

    # 모든 필드는 기본적으로 NOL NULL => 비어 있으면 안된다. 
    # 속성은 필드 . 하나의 정보에 모든 필드가 기본적으로 다 채워넣어져 있어야한다.

    title = models.CharField(max_length=20) #클래스 변수 (DB의 필드)
    content = models.TextField()  # 클래스 변수 (DB의 필드)
    created_at = models.DateTimeField(auto_now_add=True) # 추가 때만 
    updated_at = models.DateTimeField(auto_now=True)  # 언제든지 
    def __str__(self):
        return f'{self.id}번 글 - {self.title}: {self.content}'

class Student(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    birthday = models.DateField()
    age = models.IntegerField()