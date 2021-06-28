from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogForm
# Create your views here.

#READ
def home(request):
    blogs = Blog.objects.all()
    # all 메소드말고도 다른 것들이 많음 order_by('-pub_date')는 최신글 순으로 보여줌. -pub_date에서 -를 빼면 오래된 글 순
    search = request.GET.get('search')
    if search == 'true':
        author = request.GET.get('writer')
        blogs = Blog.objects.exclude(writer=author).order_by('-pub_date') #이렇게 exclude와 order_by처럼 여러개 겹쳐서 적용도 가능
                            #여기 filter 대신 exclude를 넣으면 -> writer가 author인 것 제외하고 불러옴
        return render(request,'home.html',{'blogs':blogs})

    paginator = Paginator(blogs, 2)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, 'home.html',{'blogs':blogs})

def detail(request,id):
    #blog = Blog.objects.get(id = id) 이렇게 써서 id같은 것을 하나씩 불러올 수 있음
    blog = get_object_or_404(Blog, pk = id)
    return render(request,'detail.html',{'blog':blog})

#CREATE
def new(request):
    form = BlogForm()
    return render(request,'new.html',{'form':form})

def create(request):
    form = BlogForm(request.POST,request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('detail',new_blog.id)
    return redirect('home')
#UPDATE
def edit(request,id):
    edit_blog = Blog.objects.get(id = id)
    return render(request,'edit.html',{'blog':edit_blog})

def update(request,id):
    update_blog = Blog.objects.get(id = id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('detail',update_blog.id)

#DELETE
def delete(request,id):
    delete_blog = Blog.objects.get(id = id)
    delete_blog.delete()
    return redirect('home')
