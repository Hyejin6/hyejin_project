from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm

# Create your views here.

# def 함수형태로 구현
def post_list(request) :
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') # 역순(최신글이 위로)
    return render(request, 'blog/post_list.html', {'posts' : posts})


def post_detail(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post' : post})


def post_new(request) :
    if request.method == "POST":  # 작성 후 SAVE 버튼 눌렀을 때, POST 요청이 들어온다면, PostForm()을 통해 요청으로부터 받은 데이터와 폼을 묶어줌
        form = PostForm(request.POST) # request에는 사용자가 입력했던 데이터가 담겨있으며, request.POST에 해당 내용이 들어있음.
        if form.is_valid(): # 폼의 값들이 올바른지 확인
            post = form.save(commit=False) # 폼 저장 (commit = False) 이유: 작성자, 날짜 정보를 추가하고 저장해야 하므로, 데이터 바로 저장x
            post.author = request.user
            post.published_date = timezone.now()
            post.save() # 변경사항 저장
            return redirect('blog:post_detail', pk=post.pk) # 새 블로그 글을 작성하고, post_detail 화면으로 이동
    else: # +(플러스) 버튼을 누르면 get 요청이 옴
        form = PostForm() # get 요청이 오면, PostForm()을 통해 비어있는 폼을 사용자에게 보여줌
    return render(request, 'blog/post_edit.html', {'form' : form})


def post_edit(request, pk) : # url로부터 추가로 pk 매개변수를 받아서 처리
    post = get_object_or_404(Post, pk=pk) # get_objet_or_404를 호출하여
    # 수정하고자 하는 글의 post 모델 인스턴스를 가져오고 pk로 원하는 글 찾음
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else : # 글을 수정할때 폼에 이전에 입력했던 데이터 가져오고 폼을 저장할 때 사용
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form' : form})

# 삭제기능 추가
def post_delete(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:post_list')

# 검색기능 추가
def SearchView(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        Posts = Post.objects.filter(text__contains=searched)
        return render(request, 'blog/searched.html', {'searched': searched, 'posts': Posts})
    else:
        return render(request, 'blog/searched.html', {})
