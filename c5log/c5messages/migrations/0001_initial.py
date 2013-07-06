# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MessageLog'
        db.create_table(u'c5messages_messagelog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('logtime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'c5messages', ['MessageLog'])


    def backwards(self, orm):
        # Deleting model 'MessageLog'
        db.delete_table(u'c5messages_messagelog')


    models = {
        u'c5messages.messagelog': {
            'Meta': {'object_name': 'MessageLog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logtime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['c5messages']