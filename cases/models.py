from django.db import models

# Create your models here.
class TestCase(models.Model):
    PRIORITY = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low')
    )
    issue = models.IntegerField(help_text="Bug and Feature ID", default=0)
    component = models.CharField(max_length=50)
    version = models.CharField(max_length=10)
    critical = models.CharField(max_length=2, choices=PRIORITY, default='H')
    summary = models.CharField(max_length=100)
    precondition = models.CharField(max_length=100, null=True)
    steps = models.TextField()
    auto = models.CharField(max_length=2, default='N',
                            choices=(('Y', 'Yes'), ('N', 'No')))
    
    def __unicode__(self):
        return "%d, %s, %s" %(self.issue, self.version, self.summary)

