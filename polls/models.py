import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)
    creation_date = models.DateField('date created')

    def __str__(self):
        return self.name

    def get_type(self, field_name):
        if field_name == "name":
            return "text"
        if field_name == "creation_date":
            return "date"

    def get_fields(self):
        fields = list(self._meta.get_fields(include_parents=False))
        fields.pop(0)
        result = []
        for value in fields:
            result.append(value.attname)
        return result

    def get_field(self, field_name):
        return self.__getattribute__(field_name)

    @staticmethod
    def  get_url_to_go():
        return 'polls:companyDetail'


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete= models.CASCADE)
    name = models.CharField(max_length=200)
    birthday = models.DateField('birthday')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_fields(self):
        fields = list(self._meta.get_fields())
        result = []
        for value in fields:
            result.append(value.attname)
        return result

    def get_field(self, field_name):
        return self.__getattribute__(field_name)

    def get_type(self, field_name):
        if field_name == "company":
            return "foreign_key"
        if field_name == "name":
            return "text"
        if field_name == "birthday":
            return "date"
        if field_name == "title":
            return "text"

    @staticmethod
    def get_url_to_go():
        return 'polls:employeeDetail'


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


