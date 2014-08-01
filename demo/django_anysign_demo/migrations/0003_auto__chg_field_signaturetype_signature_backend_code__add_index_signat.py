# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'SignatureType.signature_backend_code'
        db.alter_column(u'django_anysign_demo_signaturetype', 'signature_backend_code', self.gf('django.db.models.fields.CharField')(max_length=50))
        # Adding index on 'SignatureType', fields ['signature_backend_code']
        db.create_index(u'django_anysign_demo_signaturetype', ['signature_backend_code'])


    def backwards(self, orm):
        # Removing index on 'SignatureType', fields ['signature_backend_code']
        db.delete_index(u'django_anysign_demo_signaturetype', ['signature_backend_code'])


        # Changing field 'SignatureType.signature_backend_code'
        db.alter_column(u'django_anysign_demo_signaturetype', 'signature_backend_code', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'django_anysign_demo.signature': {
            'Meta': {'object_name': 'Signature'},
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signature': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'signers'", 'to': u"orm['django_anysign_demo.Signature']"})
        }
    }

    complete_apps = ['django_anysign_demo']