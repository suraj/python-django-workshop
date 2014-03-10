from django.db import models

# Create your models here.

class Student(models.Model):
    GENDER = ( ("male", "Male",),
                ("female", "Female", ),
                ("other", "Somewhere in between", ),
        )
    YEAR = ( ("first", "First Year",),
                ("second", "Second Year", ),
                ("third", "Third Year", ),
                ("fourth", "Fourth Year", ),
        )

    name = models.CharField(max_length=255, blank=False, null=False,)
    mobile = models.CharField(max_length=15, blank=False, null=False,)
    email = models.EmailField(max_length=50, blank=False, null=False,)
    is_graduated = models.BooleanField(blank=False, null=False, default=False,)
    dob = models.DateTimeField(blank=False, null=False,)
    gender = models.CharField(max_length=255,blank=False, null=False, choices=GENDER, default=GENDER[0],)
    year = models.CharField(max_length=255,blank=False, null=False, choices=YEAR, default=YEAR[0],)
    created_on = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    modified_on = models.DateTimeField(blank=False, null=False, auto_now=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __unicode__(self):
        return "{}".format(self.name)
