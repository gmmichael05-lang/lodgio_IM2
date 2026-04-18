import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lodgio.settings')
django.setup()

from accounts.models import User

try:
    user = User.objects.get(username='admin')
    user.set_password('admin123')
    user.save()
    print(f'Password reset for: {user.email} / password: admin123')
except User.DoesNotExist:
    user = User.objects.create_superuser(
        email='test@lodgio.com', username='testadmin',
        full_name='Test Admin', password='admin123',
    )
    user.role = 'Host'
    user.save()
    print(f'Created user: test@lodgio.com / password: admin123')
