# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FollowStream'
        db.create_table(u'Relations_followstream', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['User.User'])),
        ))
        db.send_create_signal(u'Relations', ['FollowStream'])

        # Adding M2M table for field boards on 'FollowStream'
        m2m_table_name = db.shorten_name(u'Relations_followstream_boards')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('followstream', models.ForeignKey(orm[u'Relations.followstream'], null=False)),
            ('board', models.ForeignKey(orm[u'Pinboard.board'], null=False))
        ))
        db.create_unique(m2m_table_name, ['followstream_id', 'board_id'])


    def backwards(self, orm):
        # Deleting model 'FollowStream'
        db.delete_table(u'Relations_followstream')

        # Removing M2M table for field boards on 'FollowStream'
        db.delete_table(db.shorten_name(u'Relations_followstream_boards'))


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