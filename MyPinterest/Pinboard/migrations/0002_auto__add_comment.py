# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comment'
        db.create_table(u'Pinboard_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['User.User'])),
            ('pin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Pinboard.Pin'])),
            ('payload', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('comment_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'Pinboard', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Comment'
        db.delete_table(u'Pinboard_comment')


    models = {
        u'Picture.picture': {
            'Meta': {'object_name': 'Picture'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'first_piner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'first_piner'", 'to': u"orm['User.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'liked_by_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['User.User']", 'symmetrical': 'False'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Picture.Tag']", 'symmetrical': 'False'}),
            'web_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
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
        u'Pinboard.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payload': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'pin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Pinboard.Pin']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['User.User']"})
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