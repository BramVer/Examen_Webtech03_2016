from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class Quote(models.Model):
	quote_author_fname = models.CharField(max_length=50)
	quote_author_lname = models.CharField(max_length=50)
	quote_text = models.CharField(max_length=300)

	def __str__(self):
		return self.quote_text