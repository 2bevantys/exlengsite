from django.db import models

class Words(models.Model):
    word_id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=255)
    translate = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
    ban_word = models.BooleanField(default=False)
    # table_user = models.ForeignKey('id_user', on_delete=models.CASCADE)

    def __str__(self):
        return self.word

