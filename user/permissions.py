from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone


class RegistedMoreThanAWeekUser(BasePermission):
    """
    가입일 기준 1주일 이상 지난 사용자만 접근 가능
    """
    message = '가입 후 1주일 이상 지난 사용자만 사용하실 수 있습니다.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.join_date < (timezone.now() - timedelta(minutes=3)))
