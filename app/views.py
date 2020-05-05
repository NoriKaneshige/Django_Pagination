from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post
from django.views import generic


class PostIndex(generic.ListView):
    model = Post
    paginate_by = 3