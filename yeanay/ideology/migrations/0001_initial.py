# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ideology'
        db.create_table(u'ideology_ideology', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('congress', self.gf('django.db.models.fields.IntegerField')()),
            ('icpsr_id', self.gf('django.db.models.fields.IntegerField')()),
            ('first_dimension', self.gf('django.db.models.fields.FloatField')()),
            ('second_dimension', self.gf('django.db.models.fields.FloatField')()),
            ('state_id', self.gf('django.db.models.fields.IntegerField')()),
            ('party_code', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'ideology', ['ideology'])


    def backwards(self, orm):
        # Deleting model 'ideology'
        db.delete_table(u'ideology_ideology')


    models = {
        u'ideology.ideology': {
            'Meta': {'object_name': 'ideology'},
            'congress': ('django.db.models.fields.IntegerField', [], {}),
            'first_dimension': ('django.db.models.fields.FloatField', [], {}),
            'icpsr_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'party_code': ('django.db.models.fields.IntegerField', [], {}),
            'second_dimension': ('django.db.models.fields.FloatField', [], {}),
            'state_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['ideology']