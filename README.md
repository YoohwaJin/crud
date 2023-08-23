# CRUD

1. 프로젝트 폴더 생성
2. 프로젝트 폴더로 이동 / vscode 실행
    2-1 '.gitignore', 'REDAME.md' 생성
3. django 프로젝트 생성
```bash
django-admin startproject <pjt-name> .
```
4. 가상환경 설정
```bash
python -m venv venv
```
5. 가상환경 활성화
```bash
source venv/Scripts/activate
```

6. 가상환경에 django 설치
```bash
pip install django
```

7. 서버 실행 확인
```bash
python manage.py runserver
```

8. 앱 생성
```bash
django-admin startapp <app-name>
```

9. 앱 등록 => `setting.py`
- settings.py에 installed app 추가 (`appname`)

10. `'url.py' => 'views.py' => templates/html'` 코드 작성

# Model

1. 모델 정의(`models.py`)
    - 모델의 이름은 기본적으로 단수 형태

```python
from django.db import models

#create your model here
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```

2. 번역본 생성
```bash
python manage.py makemigrations
```

3. DB에 반영
```bash
python manage.py migrate
```

4. SQL 스키마 확인
```bash
python manage.py sqlmigrate posts 0001
```

5. 생성한 모델 admin에 등록
```bash
from django,conntrib import admin
from .models import Post
# Register your model here.

admin.site.register(Post)
```


6. 관리자 계성 생성
```bash
python manage.py createsuperuser
```

# CRUD 로직 작성

### 1. Read

- 전체 게시물 출력
```python
def index(request):
    post = Post.objects.all()
    
    context = {
        'posts': posts,
    }
    
    return render(request, 'index.html', context)
```

- 하나의 게시물 출력

```python
def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }

    return render(request, 'detail.html', context)
```


### 2. Create

- 사용자에게 입력 할 수 있는 폼을 제공
```python
def new(request):
    return render(request, 'new.html')
```

- 사용자가 입력한 데이터를 가지고 DB에 저장하는 로직
```python
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')
```


### 3. Delete
```python
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('/index/')
```


### 4. Update
- 기존의 정보를 담은 form을 제공
```python
def edit(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }

    return render(request, 'edit.html', context)
```

- 사용자가 입력한 새로운 정보를 가져와서
- 기존정보에 덮어씌우기
```python
def update(request, id):
    # 방금 수정한 데이터
    title = request.GET.get('title')
    content = request.GET.get('content')

    # post = Post() => 새로운 게시물 만들때
    # 기존데이터
    post = Post.objects.get(id=id)
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')
```

