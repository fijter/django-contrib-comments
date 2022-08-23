# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    """
    Remove the old object_pk field and rename the object_id field to object_pk
    """

    dependencies = [
        ('django_comments', '0003_comment_object_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='object_pk',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='object_id',
            new_name='object_pk',
        ),
        migrations.AlterField(
            model_name='comment',
            name='object_pk',
            field=models.PositiveIntegerField(verbose_name='object ID'),
            preserve_default=True,
        ),
    ]
