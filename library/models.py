from django.db import models

# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length = 255)
    location = models.CharField(max_length = 255)
    contact = models.CharField(max_length = 255)


class Author(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)



class Books(models.Model):
    available = 'a'
    checkedout = 'r'
    reserved = 'o'
    book_status = [
        (available, 'available'),
        (checkedout, 'checkedout'),
        (reserved, 'reserved')
    ]

    title = models.CharField(max_length = 255)
    genre = models.CharField(max_length = 255)
    author = models.foreignkey(Author, on_delete = models.CASCADE, related_name= "author")
    Bstatus = models.CharField(max_length = 1, choice = book_status, default = available)

class Member(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    phone_number = models.CharField(max_length = 255)


class Loan(models.Model):
    active = 'a'
    returned = 'r'
    overdue = 'o'
    loan_status = [
        (active, 'active'),
        (returned, 'returned'),
        (overdue, 'overdue')
    ]
    loan_date = models.CharField(max_length = 255)
    return_date = models.CharField(max_length = 255)
    Lstatus = models.CharField(max_length = 1, choice = loan_status, default = active)

    
class Reservation(models.Model):
    active = 'a'
    completed = 'c'
    canceled = 'ca'
    reservation_status = [
        (active, 'active')
        (completed, 'completed')
        (canceled, 'canceled')
    ]
    member = models.foreignkey(Member, on_delete = models.CASCADE, related_name= "member")
    book = models.OneToOneField(Books, on_delete= models.CASCADE)
    reservation_date = models.DateField(auto_now= True)
    rstatus = models.CharField(max_length= 1, choices = reservation_status)