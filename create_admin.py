
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pbc_project.settings')
django.setup()

from django.contrib.auth.models import User

username = 'admin' # Default username since only email was provided, or use email as username if custom user model (but here it's default User)
email = 'mahi.peruva@gmail.com'
password = 'Myowngod@1'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superuser '{username}' created successfully with email '{email}'.")
else:
    print(f"Superuser '{username}' already exists.")
