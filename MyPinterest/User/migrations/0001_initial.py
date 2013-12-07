# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'User_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=255, db_index=True)),
            ('createTime', self.gf('django.db.models.fields.DateTimeField')()),
            ('lastLoginTime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('lastLoginIP', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'User', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'User_user')


    models = {
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

    complete_apps = ['User']