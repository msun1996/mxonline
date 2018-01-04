# -*- coding:utf8 -*-
from django.shortcuts import render
from django.views.generic import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Course
# Create your views here.


class CourseListView(View):
    def get(self, request):
        all_course = Course.objects.all().order_by('-add_time')

        hot_courses = Course.objects.all().order_by('-click_num')[:3]
        # 课程排序
        sort = request.GET.get('sort','')
        if sort:
            if sort == 'students':
                all_course = all_course.order_by('-students')
            if sort == 'hot':
                all_orgs = all_course.order_by('-click_num')

        # 课程分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_course, 6, request=request)
        courses = p.page(page)

        return render(request, 'course-list.html', {
            'all_course':courses,
            'sort':sort,
            'hot_courses':hot_courses,
        })