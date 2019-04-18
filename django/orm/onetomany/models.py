from django.db import models

# Create your models here.
class User(models.Model):   # 진짜 회원을 뜻하는 것은 아님. 이름만 User.
    name = models.TextField()
    
# User:Post = 1:N
class Post(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
# User:Comment = 1:N
# Post:Comment = 1:N
class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    
    
# 예시
# 1. 1번 사람이 작성한 게시글은?
# user1.post_set.all()

# 2. 1번 사람이 작성한 게시글의 댓글들을 출력!
# for post in user1.post_set.all():	# 1번 사람이 작성한 모든 게시글
#     for comment in post.comment_set.all():	# 게시글에서 작성된 모든 댓글!
#         print(comment.content)	# 댓글 내용 출력!

# 3. 2번 댓글을 작성한 사람은?
# c2. user

# 4. 2번 댓글을 쓴 사람이 작성한 게시글은?
# c2.user.post_set.all()

# 5. 1번 글의 첫번째 댓글을 쓴 사람의 이름은?
# post1.comment_set.first().user.name
    
# 6. '1글'이 제목인 게시글은?
# Post.objects.filter(title='1글')

# 7. 댓글 중에 해당 게시글의 제목이 1글인 것은?
# 방법 1
# Comment.objects.filter(post__title = '1글')
# 방법 2
# post1 = post.objects.get(title='1글')     # 객체에 먼저 집어넣고 호출
# Comment.objects.filter(post=post1)

# 8. 댓글 중에 해당 게시글의 제목에 '1'이 들어가 있는 것은?
# Comment.objects.filter(post__title__contains = '1')
    
    
# 임시글 (저장 nope)   
# user1 = User.objects.create(name='Kim')
# user2 = User.objects.create(name='Lee')

# post1 = Post.objects.create(title='1글', user=user1)    # 뒤에 객체(인스턴스) 값을 넣어준다.
# post2 = Post.objects.create(title='2글', user=user1)    # user_id=(num) 도 가능하다.
# post3 = Post.objects.create(title='3글', user=user2)    # user_id = user1.id 와 같다.

# c1 = Comment.objects.create(content='1글1댓글', user=user1, post=post1)
# c2 = Comment.objects.create(content='1글2댓글', user=user2, post=post1)
# c3 = Comment.objects.create(content='1글3댓글', user=user1, post=post1)
# c4 = Comment.objects.create(content='1글4댓글', user=user2, post=post1)
# c5 = Comment.objects.create(content='2글1댓글', user=user1, post=post2)
# c6 = Comment.objects.create(content='!1글5댓글', user=user2, post=post1)
# c7 = Comment.objects.create(content='!2글2댓글', user=user2, post=post2)