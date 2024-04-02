import uuid

from django.db import models


class Memory(models.Model):
    MEMORY_TYPES = (
        ('standard', 'Standard coming outdoor'),
        ('adventure', 'Crazy trip to interested place'),
        ('travel', 'Some days travelling'),
        ('celebration', 'Birthday or something like that')
    )
    MEMORY_STATUS=(
        ('in progress', 'In progress'),
        ('planned', 'Planned'),
        ('archived', 'Archived')
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=250)
    date=models.DateTimeField(blank=False, null=False)
    latitude=models.FloatField(max_length=8, default=0)
    longitude=models.FloatField(max_length=8, default=0)
    memory_type=models.CharField(choices=MEMORY_TYPES,
                                 max_length=11, default='standard')
    status=models.CharField(choices=MEMORY_STATUS, default='planned', max_length=11)

    def __str__(self):
        return self.name


class Picture(models.Model):
    id=models.AutoField(primary_key=True)
    memory_id=models.ForeignKey(Memory, on_delete=models.PROTECT)
    author=models.CharField(max_length=50, blank=False, null=False)
    image=models.ImageField(upload_to='pictures/%Y/%m')


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    memory_id=models.ForeignKey(Memory, on_delete=models.PROTECT)
    author=models.CharField(max_length=50, blank=False, null=False)
    date=models.DateTimeField()
    text=models.TextField()
    picture=models.ForeignKey(Picture, on_delete=models.CASCADE)
    likes=models.IntegerField(default=0)
    dislikes=models.IntegerField(default=0)

