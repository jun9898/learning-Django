from django.conf import settings  # Django 프로젝트의 설정(configuration) 파일에 접근할 수 있도록 불러옵니다.
from django.db import models      # Django ORM의 모델 클래스와 관련 기능을 사용하기 위해 불러옵니다.
from django.utils import timezone # 시간과 날짜를 다루는 유틸리티를 제공하는 Django 모듈입니다.

class Post(models.Model):  # 데이터베이스 테이블에 해당하는 Django 모델을 정의합니다. 여기서는 'Post'라는 테이블입니다.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # 사용자 모델(Django에서 기본 제공하거나 커스텀 사용자 모델)과 연결됩니다.
        on_delete=models.CASCADE  # 사용자가 삭제되면 관련된 Post도 삭제되도록 설정합니다.
    )
    title = models.CharField(max_length=200)  # 제목을 저장하는 문자열 필드입니다. 최대 길이는 200자입니다.
    text = models.TextField()  # 본문 내용을 저장하는 텍스트 필드입니다. 길이 제한이 없습니다.
    created_date = models.DateTimeField(
        default=timezone.now  # 객체 생성 시 현재 시간을 기본값으로 설정합니다.
    )
    published_date = models.DateTimeField(
        blank=True,  # 필드 값이 비어 있어도 허용합니다.
        null=True    # 데이터베이스에서 NULL 값을 허용합니다.
    )

    def publish(self):  # 게시물을 게시하는 메서드입니다.
        self.published_date = timezone.now()  # 현재 시간을 게시 시간으로 설정합니다.
        self.save()  # 변경된 내용을 데이터베이스에 저장합니다.

    def __str__(self):  # 객체를 문자열로 표현할 때 반환되는 값을 정의합니다.
        return self.title  # Post 객체가 문자열로 표현될 때 제목(title)을 반환합니다.
