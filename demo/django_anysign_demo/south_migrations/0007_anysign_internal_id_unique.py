# -*- coding: utf-8 -*-
import uuid

from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models


class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        for signature in orm['django_anysign_demo.Signature'].objects.all():
            signature.anysign_interal_id = uuid.uuid4()
            signature.save()

        # Adding field 'Signer.anysign_internal_id'
        for signer in orm['django_anysign_demo.Signer'].objects.all():
            signer.anysign_internal_id = uuid.uuid4()
            signer.save()

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'django_anysign_demo.signature': {
            'Meta': {'object_name': 'Signature'},
            'anysign_internal_id': ('uuidfield.fields.UUIDField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signature_backend_id': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100', 'db_index': 'True', 'blank': 'True'}),
            'signature_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_anysign_demo.SignatureType']"})
        },
        u'django_anysign_demo.signaturetype': {
            'Meta': {'object_name': 'SignatureType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signature_backend_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'django_anysign_demo.signer': {
            'Meta': {'object_name': 'Signer'},
            'anysign_internal_id': ('uuidfield.fields.UUIDField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signature': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'signers'", 'to': u"orm['django_anysign_demo.Signature']"}),
            'signature_backend_id': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '100', 'db_index': 'True', 'blank': 'True'}),
            'signing_order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['django_anysign_demo']
    symmetrical = True
