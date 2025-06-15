from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    description = models.TextField()

    def __str__(self):
        return self.email
    
class Enrollment(models.Model):
        FulName = models.CharField(max_length=50)
        Email = models.EmailField()
        Gender = models.CharField(max_length=10)
        PhoneNumber = models.CharField(max_length=12)
        DOB = models.DateField()
        selectMembershipPlan = models.CharField(max_length=200)
        SelectTrainer = models.CharField(max_length=20)
        Refrence = models.CharField(max_length=20)
        Address = models.TextField()
        PaymentStatus = models.CharField(max_length=20, default='Pending')  # e.g., "Pending", "Completed"
        Price = models.DecimalField(max_digits=10, decimal_places=2)
        DueDate = models.DateField()
        TimeStamp = models.CharField(max_length=20)
        def __str__(self):
            return self.fullname
        
class Trainer(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

class MembershipPlan(models.Model):
    plan = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)  # e.g., "1 Month", "3 Months"
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.plan          
    
    