# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Board'
        db.create_table(u'Pinboard_board', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['User.User'])),
            ('access_level', self.gf('django.db.models.fields.CharField')(default=2, max_length=1)),
        ))
        db.send_create_signal(u'Pinboard', ['Board'])

        # Adding model 'Pin'
        db.create_table(u'Pinboard_pin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('to_board', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Pinboard.Board'])),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Picture.Picture'])),
            ('from_pin', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='children', null=True, blank=True, to=orm['Pinboard.Pin'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'Pinboard', ['Pin'])


    def backwards(self, orm):
        # Deleting model 'Board'
        db.delete_table(u'Pinboard_board')

        # Deleting model 'Pin'
        db.delete_table(u'Pinboard_pin')


    models = {
        u'Picture.picture': {
            'Meta': {'object_name': 'Picture'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'first_piner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'first_piner'", 'to': u"orm['User.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'liked_by_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['User.User']", 'symmetrical': 'False'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Picture.Tag']", 'symmetrical': 'False'}),
            'web_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'Picture.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'Pinboard.board': {
            'Meta': {'object_name': 'Board'},
            'access_level': ('django.db.models.fields.CharField', [], {'default': '2', 'max_length': '1'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['User.User']"})
        },
        u'Pinboard.pin': {
            'Meta': {'object_name': 'Pin'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'from_pin': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'children'", 'null': 'True', 'blank': 'True', 'to': u"orm['Pinboard.Pin']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Picture.Picture']"}),
            'to_board': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Pinboard.Board']"})
        },
        u'User.user': {
            'Meta': {'object_name': 'User'},
            'createTime': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lastLoginIP': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'lastLoginTime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'})
        }
    }

    complete_apps = ['Pinboard']