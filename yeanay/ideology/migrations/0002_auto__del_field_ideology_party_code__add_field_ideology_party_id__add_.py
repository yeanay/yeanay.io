# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ideology.party_code'
        db.delete_column(u'ideology_ideology', 'party_code')

        # Adding field 'ideology.party_id'
        db.add_column(u'ideology_ideology', 'party_id',
                      self.gf('django.db.models.fields.IntegerField')(default=9999999),
                      keep_default=False)

        # Adding field 'ideology.district'
        db.add_column(u'ideology_ideology', 'district',
                      self.gf('django.db.models.fields.IntegerField')(default=9999999),
                      keep_default=False)

        # Adding field 'ideology.chamber'
        db.add_column(u'ideology_ideology', 'chamber',
                      self.gf('django.db.models.fields.CharField')(default='None', max_length=6),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'ideology.party_code'
        raise RuntimeError("Cannot reverse this migration. 'ideology.party_code' and its values cannot be restored.")
        # Deleting field 'ideology.party_id'
        db.delete_column(u'ideology_ideology', 'party_id')

        # Deleting field 'ideology.district'
        db.delete_column(u'ideology_ideology', 'district')

        # Deleting field 'ideology.chamber'
        db.delete_column(u'ideology_ideology', 'chamber')


    models = {
        u'ideology.ideology': {
            'Meta': {'object_name': 'ideology'},
            'chamber': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'congress': ('django.db.models.fields.IntegerField', [], {}),
            'district': ('django.db.models.fields.IntegerField', [], {}),
            'first_dimension': ('django.db.models.fields.FloatField', [], {}),
            'icpsr_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'party_id': ('django.db.models.fields.IntegerField', [], {}),
            'second_dimension': ('django.db.models.fields.FloatField', [], {}),
            'state_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['ideology']