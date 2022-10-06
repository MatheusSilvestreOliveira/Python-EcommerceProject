from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from utils.cpf_validator import cpf_validator
import re


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    cpf = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    address_number = models.CharField(max_length=5)
    address_complement = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.user} - {self.user.first_name} {self.user.last_name}'

    def clean(self):
        error_messages = {}
        if not cpf_validator(self.cpf):
            error_messages['cpf'] = 'Valid CPF is required'
        raise ValidationError(error_messages)
