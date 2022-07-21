from django.db import models


class NewsletterUser(models.Model):
    """ simple newlesletter model """
    email = models.EmailField()
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
