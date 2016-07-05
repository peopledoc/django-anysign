# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_anysign_demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signer',
            name='signing_order',
            field=models.PositiveSmallIntegerField(default=0, help_text='Position in the list of signers.', verbose_name='signing order'),
        ),
    ]
