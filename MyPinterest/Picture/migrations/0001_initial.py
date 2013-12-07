# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'Picture_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'Picture', ['Tag'])

        # Adding model 'Picture'
        db.create_table(u'Picture_picture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_piner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='first_piner', to=orm['User.User'])),
            ('web_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'Picture', ['Picture'])

        # Adding M2M table for field tags on 'Picture'
        m2m_table_name = db.shorten_name(u'Picture_picture_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('picture', models.ForeignKey(orm[u'Picture.picture'], null=False)),
            ('tag', models.ForeignKey(orm[u'Picture.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['picture_id', 'tag_id'])

        # Adding M2M table for field liked_by_users on 'Picture'
        m2m_table_name = db.shorten_name(u'Picture_picture_liked_by_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('picture', models.ForeignKey(orm[u'Picture.picture'], null=False)),
            ('user', models.ForeignKey(orm[u'User.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['picture_id', 'user_id'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'Picture_tag')

        # Deleting model 'Picture'
        db.delete_table(u'Picture_picture')

        # Removing M2M table for field tags on 'Picture'
        db.delete_table(db.shorten_name(u'Picture_picture_tags'))

        # Removing M2M table for field liked_by_users on 'Picture'
        db.delete_table(db.shorten_name(u'Picture_picture_liked_by_users'))


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
            'username': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['Picture']