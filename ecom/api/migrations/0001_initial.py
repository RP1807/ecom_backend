from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):

    dependencies = [

    ]

    def seed_data(apps, schema_editor):
        user = CustomUser(name="rushikesh", email="rushikesh@google.com", is_staff=True, is_superuser=True,
                          phone="9769188860", gender="Male")
        user.set_password("Rushi@123")
        user.save()

    operations = [
        migrations.RunPython(seed_data),
    ]