# Django ORM

## Create

### 기초 설정
- shell
  ```bash
  $ python manage.py shell
  ```

- import model
  ```bash
  >>> from articles.models import Article
  ```

- 모든 객체 확인

  ```bash
  >>> Article.objects.all()
  ```

  

#### 데이터를 저장하는 3가지 방법

1. 첫번째 방식

   - ORM을 쓰는 이유?

     -> DB를 조작하는 것을 객체지향 프로그래밍(클래스)처럼 하기 위해서 

     ```bash
     article = Article()
     article #<Article: Article object (None)>
     article.title = 'First title'
     article.content = 'hello'
     article.save()
     Article.objects.all()  #<QuerySet [<Article: Article object (1)>]>
     article #<Article: Article object (1)>
     ```



2. 두번째 방식
   -  함수에서 keyword 인자 넘기기 방식과 동일

		```bash
	article = Article(title='second article', content='hihi')
	article.save()
	article  #<Article: Article object (2)>
		```



3. 세번째 방식
   
   - create를 사용하면 쿼리셋 객체를 생성하고 저장하는 로직이 한번에 
   
     ```BASH
     Article.objects.create(title='third', content='wdqwdwqd') #<Article: Article object (3)>
     
     Article.objects.all()  #<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
     ```
     
   

- object 검증 

  - 해당 object가 저장할수 있는 상태인지 검증

  ```bash
  article.full_clean()   # django.core.exceptions.ValidationError: {'content': ['이 필드는 빈 칸으로 둘 수 없습니다.']}
  ```

  

## Read

### 모든객체

```bash
>>> Article.objects.all()
<QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
```



#### 객체 표현 변경

```python
#articles/models.py
class Article(models.Model):
    ...
    def __str__(self):
        return f'{self.id}번 글 - {self.title}: {self.content}'
```

- 모든 객체

```bash
>>> Article.objects.all()
<QuerySet [<Article: 1번 글 - First article: hello, article>, <Article: 2번 글 - second article: qweqwe>, <Article: 3번 글 - third: wdqwdwqd>]>
```

- 특정 객체(하나가 아니고 여러 개를 가지고 올수도 있음)

```bash
>>> Article.objects.filter(title='second article')
<QuerySet [<Article: 2번 글 - second article: qweqwe>]>
```
```bash
>>> Article.objects.create(title='second article', content='wdqwd')
<Article: 4번 글 - second article: wdqwd>
>>> Article.objects.filter(title='second article')
<QuerySet [<Article: 2번 글 - second article: qweqwe>, <Article: 4번 글 - second article: wdqwd>]>  
```

- DB에 저장된 객체 중에서 title이 second article인 첫번째 객체만 가져옴

```bash
>>> querySet = Article.objects.filter(title='second article')
>>> querySet
<QuerySet [<Article: 2번 글 - second article: qweqwe>, <Article: 4번 글 - second article: wdqwd>]>
>>> querySet.first()
<Article: 2번 글 - second article: qweqwe>

>>> Article.objects.filter(title='second article').first()
<Article: 2번 글 - second article: qweqwe>
```

- DB에 저장된 객체 중에서 pk가 1인 객체만 가져오기

  **pk만 get()으로 가지고 올수 있다.**

  get()은 하나 있는 것만 가지고 올수 있꼬 

  pk는 확실히 구분지어줄수 있는 수단이기 때문이다.

  여러개 or 0개 있을 경우 에러남

```bash
>>> Article.objects.get(pk=1)
<Article: 1번 글 - First article: hello, article>
```

- 하지만 filter에 경우는 둘다 에러가 안남

```bash
>>> Article.objects.filter(title='wqeq')
<QuerySet []>
```

- 오름차순

```bash
>>> articles = Article.objects.order_by('pk')
>>> articles
<QuerySet [<Article: 1번 글 - First article: hello, article>, <Article: 2번 글 - second article: qweqwe>, <Article: 3번 글 - third: wdqwdwqd>, <Article: 4번 글 - second article: wdqwd>]>
```

- 내림차순

```bash
>>> articles = Article.objects.order_by('-pk')
>>> articles
<QuerySet [<Article: 4번 글 - second article: wdqwd>, <Article: 3번 글 - third: wdqwdwqd>, <Article: 2번 글 - second article: qweqwe>, <Article: 1번 글 - First article: hello, article>]>
```

- index 접근 가능(0 부터 시작)

```bash
>>> article = articles[2]
>>> article
<Article: 2번 글 - second article: qweqwe>

>>> articles = Article.objects.all()[:2]
>>> articles
<QuerySet [<Article: 1번 글 - First article: hello, article>, <Article: 2번 글 - second article: qweqwe>]>
```

- LIKE - 문자열을 포함하고 있는 값을 가지고 옴

  쟝고 ORM은 이름과 필터를 더블 언더스코어로 구분합니다. _ _

  ```BASH
  >>> articles = Article.objects.filter(title__contains='sec')
  >>> articles
  <QuerySet [<Article: 2번 글 - second article: qweqwe>, <Article: 4번 글 - second article: wdqwd>]>
  ```

- startwith

  ```bash
  >>> articles = Article.objects.filter(title__startswith='First')
  >>> articles
  <QuerySet [<Article: 1번 글 - First article: hello, article>]>
  ```

- endswith

  ```bash
  >>> articles = Article.objects.filter(title__endswith='rd')
  >>> articles
  <QuerySet [<Article: 3번 글 - third: wdqwdwqd>]>
  ```

  

## Delete

- .delete()

  ```bash
  >>> article = Article.objects.get(pk=1)
  >>> article.delete()
  (1, {'articles.Article': 1})
  ```

  

## Update

- article 인스턴스 호출 후 값 변경하여 .save()

```bash
>>> article = Article.objects.get(pk=2)
>>> article
<Article: 2번 글 - second article: qweqwe>
>>> article.content = 'refactor content'
>>> article.save()
>>> article
<Article: 2번 글 - second article: refactor content>
```

