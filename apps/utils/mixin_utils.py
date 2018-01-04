# -*- coding:utf-8 -*-
# author: msun1996

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginRequiredMinxin(object):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMinxin, self).dispatch(request, *args, **kwargs)