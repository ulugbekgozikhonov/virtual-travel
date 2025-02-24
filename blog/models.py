from django.db import models
from users.models import Base, User
from travel.models import City
import uuid

class Blog(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    video = models.FileField(upload_to="blog_videos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.likes.count()  # Nechta like borligini hisoblaydi


class Comment(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.blog.title}"

    @property
    def like_count(self):
        return self.likes.count()


class Like(Base):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="likes", blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "blog", "comment")  
        
    def __str__(self):
        if self.blog:
            return f"{self.user.username} liked {self.blog.title}"
        return f"{self.user.username} liked a comment"


class BlogMedia(Base):
    MEDIA_TYPE_CHOICES = [
        ("image", "Image"),
        ("video", "Video"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="media_files")
    file = models.FileField(upload_to="blog_media/")
    file_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)

    def __str__(self):
        return f"{self.file_type.capitalize()} for {self.blog.title}"
