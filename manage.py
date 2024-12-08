#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinejobportal.settings')
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
    # For deployment (like Heroku) where the platform provides a dynamic PORT
    if 'PORT' in os.environ:
        port = os.environ['PORT']
        sys.argv.append(f'runserver 0.0.0.0:{port}')
    else:
        sys.argv.append('runserver 0.0.0.0:8000')

    main()