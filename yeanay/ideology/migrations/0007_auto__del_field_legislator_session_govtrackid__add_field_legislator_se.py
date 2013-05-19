# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'legislator_session.govtrackid'
        db.delete_column(u'ideology_legislator_session', 'govtrackid')

        # Adding field 'Legislator_session.legis_key'
        db.add_column(u'ideology_legislator_session', 'legis_key',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.datetime(2013, 5, 17, 0, 0), to=orm['ideology.Legislator'], db_column='govtrackid'),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'legislator_session.govtrackid'
        raise RuntimeError("Cannot reverse this migration. 'legislator_session.govtrackid' and its values cannot be restored.")
        # Deleting field 'Legislator_session.legis_key'
        db.delete_column(u'ideology_legislator_session', 'govtrackid')


    models = {
        u'ideology.ideology': {
            'Meta': {'object_name': 'Ideology'},
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
            'Meta': {'object_name': 'Legislator'},
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
            'Meta': {'object_name': 'Legislator_session'},
            'chamber': ('django.db.models.fields.TextField', [], {}),
            'district': ('django.db.models.fields.IntegerField', [], {}),
            'enddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legis_key': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ideology.Legislator']", 'db_column': "'govtrackid'"}),
            'party': ('django.db.models.fields.TextField', [], {}),
            'session': ('django.db.models.fields.IntegerField', [], {}),
            'startdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['ideology']