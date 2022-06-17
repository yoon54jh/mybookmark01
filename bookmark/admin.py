from django.contrib import admin

from .models import Bookmark                #models에서 Bookmark를 가져온다

admin.site.register(Bookmark)               #admin사이트에 Bookmark를 등록해준다. admin에서 확인이 가능해진다