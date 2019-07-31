from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from django.core.paginator import Paginator
from .models import portfolio
from .forms import BlogPost

def home(request):
    blogs = Blog.objects
    blog_list=Blog.objects.all()
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    #단순히 new.html을 띄워주기위한 함수
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
    #redirect 함수는 위내용을 다 처리하고 이 url로 넘기세요~라는 의미를 가짐
    #redirect 와 request의 차이 : redirect는 프로젝트 외의 url까지도 연결할 수 있음 ex.google
    #request는 파이썬 함수를 사용해 처리한 인자들을 담아서 보여줄때? 여튼 어떤 인자를 가지느냐의 차이 

#입력받은 내용을 데이터베이스에 넣어주는 함수 = create함수

def myportfolio(request):
    portfolios = portfolio.objects
    return render(request, 'portfolio.html', {'portfolios' : portfolios})
# Create your views here.

def blogpost(request):
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})
