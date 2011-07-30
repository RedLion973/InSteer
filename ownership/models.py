from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from InSteer.settings import YEAR_CHOICES, PROJECT_ACTOR_TYPE_CHOICES
from InSteer.crm.models import Client

class Step(models.Model):
    name = models.CharField(max_length=500, unique=True)
    
    def __unicode__(self):
        return u'%s' % (self.name)
    
    class Meta:
        verbose_name = u'General Project Step'
        verbose_name_plural = u'General Project Steps'

class DeliveredDocument(models.Model):
    name = models.CharField(max_length=500, unique=True)
    
    def __unicode__(self):
        return u'%s' % (self.name)
    
    class Meta:
        verbose_name = u'General Delivered Document'
        verbose_name_plural = u'General Delivered Documents'

class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    year = models.PositiveIntegerField(choices=YEAR_CHOICES)
    client = models.ForeignKey(Client)
    steps = models.ManyToManyField(Step, through='ProjectStep')
    
    def __unicode__(self):
        return u'%s' % (self.name)
    
    class Meta:
        verbose_name = u'Project'
        verbose_name_plural = u'Projects'

class ProjectStep(models.Model):
    step = models.ForeignKey(Step)
    project = models.ForeignKey(Project)
    description = models.TextField()
    valuation_of_time = models.PositiveIntegerField(blank=True)
    
    def __unicode__(self):
        return u'%s - %s' % (self.project, self.step)
    
    class Meta:
        verbose_name = u'Project Step'
        verbose_name_plural = u'Project Steps'

class ProjectRole(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    def __unicode__(self):
        return u'%s' % (self.name)
    
    class Meta:
        verbose_name = u'Project Role'
        verbose_name_plural = u'Project Roles'
    
class ProjectActor(models.Model):
    type = models.CharField(max_length=50, choices=PROJECT_ACTOR_TYPE_CHOICES)
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    project_roles = models.ManyToManyField(ProjectRole)

    def human_readable_name(self):
        return self.user.get_full_name()
    human_readable_name.short_description = u'Complete Name'
    
    def get_full_roles(self):
        roles_string = self.project_roles.all()[0].__unicode__()
        for i in range(1, len(self.project_roles.all())):
            roles_string += "/" + self.project_roles.all()[i].__unicode__()
        return smart_unicode(roles_string)
    get_full_roles.short_description = u'Complete Roles List'
            
    def __unicode__(self):
        return u'%s - %s' % (self.human_readable_name(), self.get_full_roles())
    
    class Meta:
        verbose_name = u'Project Actor'
        verbose_name_plural = u'Project Actors'
        unique_together = ("user", "project")

class Task(models.Model):
    project_step = models.ForeignKey(ProjectStep)
    name = models.CharField(max_length=300)
    description = models.TextField()
    resources = models.ManyToManyField(ProjectActor, limit_choices_to={'type': 'Business'})
    valuation_of_time = models.PositiveIntegerField()
    document_to_deliver = models.ManyToManyField(DeliveredDocument, through='ProjectDeliveredDocument')
    delivery = models.BooleanField(editable=False, default=0)
    
    def __unicode__(self):
        return u'%s - %s' % (self.project_step, self.name)
    
    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)
        time = 0
        for task in self.project_step.task_set.all():
            time += task.valuation_of_time
        self.project_step.valuation_of_time = time
        self.project_step.save()
    
    class Meta:
        verbose_name = u'Task'
        verbose_name_plural = u'Tasks'

class ProjectDeliveredDocument(models.Model):
    document = models.ForeignKey(DeliveredDocument)
    task = models.ForeignKey(Task)
    description = models.TextField()
    url = models.URLField(max_length=600, verify_exists=True)
    version = models.CharField(max_length=10)
    
    def __unicode__(self):
        return u'%s - %s' % (self.project, self.step)
    
    class Meta:
        verbose_name = u'Project Delivered Document'
        verbose_name_plural = u'Project Delivered Documents'
