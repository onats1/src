from django.db import models

# PRIORITY = [("L", "Low"),
#             ("M", "Medium"),
#             ("H", "High")
#             ]
#
#
# # Create your models here.
# class Questions(models.Model):
#     title = models.CharField(max_length=60)
#     question = models.TextField(max_length=400)
#     priority = models.CharField(max_length=1, choices=PRIORITY)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = "Question"
#         verbose_name_plural = "Questions"
