from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	
	def __str__(self):
		return self.title
	
# 1. Create
# post = Post(title='hello', content='world!')
# post.save()

# 2. Read
# 2.1. All
# posts = Post.objects.all()
# 2.2. Get one
# post = Post.objects.get(pk=1)
# 2.3. filter (WHERE)
# posts = Post.objects.filter(title='Hello').all()
# post = Post.objects.filter(tile='Hello').first()
# 2. 4. LIKE

# 2. 5. order
# posts = Post.objects.filter(title__contains='He').all() 
# posts = Post.objects.oreder_by('title'). all() #오름차순 
# posts = Post.objects.oreder_by('-title'). all() #내림차순 

# 2.6 limit & offset
# [offset: offset+limit]
# posts = Post.objects.all()[1:2]

# 3. Delete
# post = Post.objects.get(pk=2)
# post.delete()

# 4. Update
# post = Post.object.get(pk=1)
# post.title = 'hi'
# post.save()




