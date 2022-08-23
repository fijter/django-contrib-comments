# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def migrate_string_to_int(apps, schema_editor):
    """
    Use the data already in the object_pk field and convert it to
    and integer and store to the object_id field
    :param apps:
    :param schema_editor:
    :return: None
    """
    # Fetch the historical Comment model
    Comment = apps.get_model("django_comments", "Comment")
    for com in Comment.objects.all():
        com.object_id = int(com.object_pk)
        com.save()


class Migration(migrations.Migration):
    """
    Add the new object_id field and fill it with data from the object_pk field.
    """

    dependencies = [
        ('django_comments', '0002_update_user_email_field_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.RunPython(migrate_string_to_int),
    ]
