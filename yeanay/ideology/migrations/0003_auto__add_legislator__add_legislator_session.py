# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'legislator'
        db.create_table(u'ideology_legislator', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('govtrackid', self.gf('django.db.models.fields.IntegerField')()),
            ('lastname', self.gf('django.db.models.fields.TextField')()),
            ('firstname', self.gf('django.db.models.fields.TextField')()),
            ('namemodifier', self.gf('django.db.models.fields.TextField')()),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.TextField')()),
            ('pvsid', self.gf('django.db.models.fields.TextField')()),
            ('bioguideid', self.gf('django.db.models.fields.TextField')()),
            ('youtubeid', self.gf('django.db.models.fields.TextField')()),
            ('twitterid', self.gf('django.db.models.fields.TextField')()),
            ('facebookid', self.gf('django.db.models.fields.TextField')()),
            ('thomasid', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'ideology', ['legislator'])

        # Adding model 'legislator_session'
        db.create_table(u'ideology_legislator_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('govtrackid', self.gf('django.db.models.fields.IntegerField')()),
            ('chamber', self.gf('django.db.models.fields.TextField')()),
            ('district', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.TextField')()),
            ('startdate', self.gf('django.db.models.fields.DateField')()),
            ('enddate', self.gf('django.db.models.fields.DateField')()),
            ('party', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'ideology', ['legislator_session'])


    def backwards(self, orm):
        # Deleting model 'legislator'
        db.delete_table(u'ideology_legislator')

        # Deleting model 'legislator_session'
        db.delete_table(u'ideology_legislator_session')


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
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'facebookid': ('django.db.models.fields.TextField', [], {}),
            'firstname': ('django.db.models.fields.TextField', [], {}),
            'gender': ('django.db.models.fields.TextField', [], {}),
            'govtrackid': ('django.db.models.fields.IntegerField', [], {}),
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
            'enddate': ('django.db.models.fields.DateField', [], {}),
            'govtrackid': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.TextField', [], {}),
            'startdate': ('django.db.models.fields.DateField', [], {}),
            'state': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['ideology']