# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FriendStatus'
        db.create_table(u'Relations_friendstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_user', to=orm['User.User'])),
            ('to_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_user', to=orm['User.User'])),
            ('status', self.gf('django.db.models.fields.CharField')(default=0, max_length=1)),
        ))
        db.send_create_signal(u'Relations', ['FriendStatus'])


    def backwards(self, orm):
        # Deleting model 'FriendStatus'
        db.delete_table(u'Relations_friendstatus')


    models = {
        u'Pinboard.board': {
            'Meta': {'object_name': 'Board'},
            'access_level': ('django.db.models.fields.CharField', [], {'default': '2', 'max_length': '1'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['User.User']"})
        },
        u'Relations.followstream': {
            'Meta': {'object_name': 'FollowStream'},
            'boards': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Pinboard.Board']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['User.User']"})
        },
        u'Relations.friendstatus': {
            'Meta': {'object_name': 'FriendStatus'},
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_user'", 'to': u"orm['User.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '1'}),
            'to_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_user'", 'to': u"orm['User.User']"})
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

    complete_apps = ['Relations']