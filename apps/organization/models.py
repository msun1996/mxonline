# -*- coding:utf8 -*-
from django.db import models
from datetime import datetime
# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'城市')
    desc = models.CharField(max_length=200, verbose_name=u'描述')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'机构名称')
    dec = models.TextField(verbose_name=u'机构描述')
    category = models.CharField(default='pxjg', max_length=20, choices=(('pxjg', '培训机构'), ('gx', '高校'),('gr', '个人')), verbose_name=u'机构类型')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name=u'logo')
    address = models.CharField(max_length=150, verbose_name=u'机构地址')
    city = models.ForeignKey(CityDict, verbose_name=u'所在城市')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    courses_nums = models.IntegerField(default=0, verbose_name=u'课程数')
    image = models.ImageField(default='', upload_to='orgs/%Y/%m', max_length=100, verbose_name=u'图像')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'课程机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u's所属机构')
    name = models.CharField(max_length=50, verbose_name=u'教师名')
    work_years = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=50, verbose_name=u'就职公司')
    points = models.CharField(max_length=50, verbose_name=u'教学特点')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')
    image = models.ImageField(default='', upload_to='teachers/%Y/%m', max_length=100, verbose_name=u'头像')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
