#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


# application이 시작되는 부분
def main():
    """Run administrative tasks."""
    # 여기서 setting.py의 설정값을 불러와 서버를 실행시킴
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
