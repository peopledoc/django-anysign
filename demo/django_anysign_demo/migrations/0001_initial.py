# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('signature_backend_id', models.CharField(default='', max_length=100, verbose_name='ID for signature backend', db_index=True, blank=True)),
                ('anysign_internal_id', uuidfield.fields.UUIDField(verbose_name='ID in internal database', unique=True, max_length=32, editable=False, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SignatureType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('signature_backend_code', models.CharField(max_length=50, verbose_name='signature backend', db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Signer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('signing_order', models.PositiveSmallIntegerField(default=0, help_text='Position in the list of signers. Starts at 1.', verbose_name='signing order')),
                ('signature_backend_id', models.CharField(default='', max_length=100, verbose_name='ID in signature backend', db_index=True, blank=True)),
                ('anysign_internal_id', uuidfield.fields.UUIDField(verbose_name='ID in internal database', unique=True, max_length=32, editable=False, blank=True)),
                ('signature', models.ForeignKey(related_name='signers', to='django_anysign_demo.Signature')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='signature',
            name='signature_type',
            field=models.ForeignKey(verbose_name='signature type', to='django_anysign_demo.SignatureType'),
        ),
    ]
