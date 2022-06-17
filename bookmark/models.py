from django.db import models

#해당 bookmark 폴더의 models.py로 이동하여 model을 설계한다
#bookmark 앱의 model을 구성하였다
#사이트 이름, url, contents(텍스트를 넣을 수 있는 공간들), created(생성된 날짜)
class Bookmark(models.Model):
    site_name = models.CharField(max_length=30)     #사이트 이름은 CharField를 통해 넣을 수 있게
    url = models.URLField()                         #URLField를 가져와서 적용
    contents = models.TextField(blank=True)         #TextField를 통해 공간 구성(blank도 괜찮다)
    created = models.DateTimeField(auto_now_add=True) #생성날짜와 시간까지 다 들어가는 DateTimeField
                                                      # auto_now_add를 통해 알아서 입력 가능

    def __str__(self):      #str을 써서 초기 admin사이트에서 보이는 화면을 구현 가능
        return "Site name :" +self.site_name    #리턴은 사이트 이름에 관한 것을 띄워주고 self.site_name을 띄워줌

    class Meta:     #class Meta를 통헤 ordering을 바꾼다
        ordering = ["-created"]     #ordering을 -created하면 최근에 생성된 게시물이 제일 위로 오도록 설정

