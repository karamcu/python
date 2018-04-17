
#!/usr/bin/env python
import django
import os
import sys
if __name__ == "__main__":
  os.environ.setdefault("DJANGO_SETTING_MODULE", "myproject.settings")
  django.setup()
  from django.core.management import execute_from_command_line
  execute_from_command_line(sys.argv)
