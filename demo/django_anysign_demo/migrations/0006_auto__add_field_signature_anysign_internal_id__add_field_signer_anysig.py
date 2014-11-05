# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Signature.anysign_internal_id'
        db.add_column(u'django_anysign_demo_signature', 'anysign_internal_id',
                      self.gf('uuidfield.fields.UUIDField')(default='fake', unique=False, max_length=36, blank=True),
                      keep_default=False)

        # Adding field 'Signer.anysign_internal_id'
        db.add_column(u'django_anysign_demo_signer', 'anysign_internal_id',
                      self.gf('uuidfield.fields.UUIDField')(default='fake', unique=False, max_length=36, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Signature.anysign_internal_id'
        db.delete_column(u'django_anysign_demo_signature', 'anysign_internal_id')

        # Deleting field 'Signer.anysign_internal_id'
        db.delete_column(u'django_anysign_demo_signer', 'anysign_internal_id')


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
