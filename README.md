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


```

> ## urls.py
``` python

```

> ## post_list.html
``` python

```
