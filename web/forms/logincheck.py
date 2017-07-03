#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from django.forms import fields as django_fields
from django import forms as django_forms
from repository import models
class MyForm(django_forms.ModelForm):
    class Meta:
        model =models.UserInfo
        fields = '__all__'
        exclude =['fans','avatar']

