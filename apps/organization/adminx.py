# -*- coding:utf8 -*-

import xadmin

from .models import CourseOrg, CityDict, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fileds = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'dec', 'category', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'students', 'courses_nums', 'image', 'add_time']
    search_fileds = ['name', 'dec', 'category', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'students', 'courses_nums', 'image']
    list_filter = ['name', 'dec', 'category', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'students', 'courses_nums', 'image', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'points', 'click_nums', 'fav_nums', 'image', 'add_time']
    search_fileds = ['org', 'name', 'work_years', 'work_company', 'points', 'click_nums', 'fav_nums', 'image']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'points', 'click_nums', 'fav_nums', 'image', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)