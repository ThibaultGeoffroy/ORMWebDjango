import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.



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


class utils():

    def create_model(name, fields=None, app_label='', module='', options=None, admin_opts=None):
        """
        Create specified model
        """
        class Meta:
            pass

        if app_label:
            setattr(Meta, 'app_label', app_label)

        # Update Meta with any options that were provided
        if options is not None:
            for key, value in options.iteritems():
                setattr(Meta, key, value)

        # Set up a dictionary to simulate declarations within a class
        attrs = {'__module__': module, 'Meta': Meta}

        # Add in any fields that were provided
        if fields:
            attrs.update(fields)

        # Create the class, which automatically triggers ModelBase processing
        model = type(name, (models.Model,), attrs)

        # Create an Admin class if admin options were provided
        if admin_opts is not None:
            class Admin(admin.ModelAdmin):
                pass
            for key, value in admin_opts:
                setattr(Admin, key, value)
            admin.site.register(model, Admin)

        return model