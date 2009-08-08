#!/usr/bin/env python
import sys
sys.path.append('..')

from django.core.management import execute_manager
from mysite import settings

if __name__ == "__main__":
    execute_manager(settings)
