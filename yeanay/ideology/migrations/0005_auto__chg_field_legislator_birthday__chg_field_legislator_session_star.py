# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'legislator.birthday'
        db.alter_column(u'ideology_legislator', 'birthday', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'legislator_session.startdate'
        db.alter_column(u'ideology_legislator_session', 'startdate', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'legislator_session.enddate'
        db.alter_column(u'ideology_legislator_session', 'enddate', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'legislator.birthday'
        raise RuntimeError("Cannot reverse this migration. 'legislator.birthday' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'legislator_session.startdate'
        raise RuntimeError("Cannot reverse this migration. 'legislator_session.startdate' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'legislator_session.enddate'
        raise RuntimeError("Cannot reverse this migration. 'legislator_session.enddate' and its values cannot be restored.")

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
        },
        u'ideology.legislator': {
            'Meta': {'object_name': 'legislator'},
            'bioguideid': ('django.db.models.fields.TextField', [], {}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'facebookid': ('django.db.models.fields.TextField', [], {}),
            'firstname': ('django.db.models.fields.TextField', [], {}),
            'gender': ('django.db.models.fields.TextField', [], {}),
            'govtrackid': ('django.db.models.fields.IntegerField', [], {}),
            'icpsrid': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.TextField', [], {}),
            'namemodifier': ('django.db.models.fields.TextField', [], {}),
            'pvsid': ('django.db.models.fields.TextField', [], {}),
            'thomasid': ('django.db.models.fields.TextField', [], {}),
            'twitterid': ('django.db.models.fields.TextField', [], {}),
            'youtubeid': ('django.db.models.fields.TextField', [], {})
        },
        u'ideology.legislator_session': {
            'Meta': {'object_name': 'legislator_session'},
            'chamber': ('django.db.models.fields.TextField', [], {}),
            'district': ('django.db.models.fields.IntegerField', [], {}),
            'enddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'govtrackid': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.TextField', [], {}),
            'startdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['ideology']