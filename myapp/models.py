from django.db import models as m

# Create your models here.
class DreamReal(m.Model):
	website = m.CharField(max_length=100)
	mail = m.EmailField(max_length=50)
	name = m.CharField(max_length=25)
	phonenumber = m.IntegerField()

	class Meta:
		db_table = "dreamreal"