# Django_Pagination

[referred blog](https://narito.ninja/blog/detail/89/)

![pagination](pagination.gif)

> ## models.py
``` python
from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.title
```

> ## admin.py
``` python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

> ## views.py
``` python
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post
from django.views import generic

class PostIndex(generic.ListView):
    model = Post
    paginate_by = 3
```

> ## urls.py
``` python
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.PostIndex.as_view(), name='post_list'), 
]
```

> ## post_list.html
``` python

```
