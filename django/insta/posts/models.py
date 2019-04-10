from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

def post_image_path(instance, filename):
    return f'posts/images/{filename}'  # f 스트링 사용. filename에 확장자가 포함되어 있음.
    # 폴더이름에 들어가면 안되는 기호가 있기때문에 content 를 쓰는건 바람직하지 않다.
    # {instance.pk} 도 데이터베이스에 저장이 안되면 id가 생성되지 않기 때문에 오류가 날 수 있다.


# Create your models here.
class Post(models.Model):
    # 특정한 하나의 유저가 게시할 수 있는 게시글은 여러 개이다. (1:N 관계형성)
    # 위의 경우 N이 누구의 것인지 표시하는 게 효율적이다.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 다 삭제에 노출되는 CASCADE 라는 옵션.
    # 외래키를 담는다. 다른 모델을 들고와도 반영할 수 있는 장점이 있다.(공식문서 권유기준)
    content = models.TextField()
    # image = models.ImageField(blank=True)   # image라는 이름의 column을 추가!
    # (blank=True) 없으면 이미지가 없을 때 오류가 난다.
    image = ProcessedImageField(
                    upload_to = post_image_path, # 저장 위치
                    processors = [ResizeToFill(600,600)],   # 처리할 작업 목록
                    format = 'JPEG',    # 저장 포맷
                    options = {'quality':90},   # 옵션
        )