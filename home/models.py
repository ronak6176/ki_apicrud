from django.db import models

# Create your models here.



# class user(models.Model):
# 	id=models.AutoField
# 	name = models.CharField(max_length=255)
# 	city = models.CharField(max_length=255)
# 	number = models.CharField(max_length=255)
# 	age = models.CharField(max_length=255)

# 	def __str__(self) -> str:
# 		return self.name

class user(models.Model):
	# id=models.AutoField
	name = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	number = models.CharField(max_length=200)
	age = models.CharField(max_length=200)
 
	def __str__(self) -> str:
		return self.name



class appointment(models.Model):
	# id=models.AutoField
	name = models.CharField(max_length=2000)
	url = models.CharField(max_length=2000)
	time = models.CharField(max_length=2000)
	day = models.CharField(max_length=2000)
 
	# def __str__(self) -> str:
	# 	return self.name


class event_benefits(models.Model):
	# id=models.AutoField
	name = models.CharField(max_length=2000)
	url = models.CharField(max_length=2000)


class history(models.Model):
	# id=models.AutoField
	type = models.CharField(max_length=2000)
	history_description = models.CharField(max_length=2000)
	creation_time	 = models.CharField(max_length=2000)
	user_name = models.CharField(max_length=2000)










