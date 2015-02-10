# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Buttons'
        db.create_table(u'blahblahbuttons_buttons', (
            (u'product_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['myshop.Product'], unique=True, primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'blahblahbuttons', ['Buttons'])


    def backwards(self, orm):
        # Deleting model 'Buttons'
        db.delete_table(u'blahblahbuttons_buttons')


    models = {
        u'blahblahbuttons.buttons': {
            'Meta': {'object_name': 'Buttons', '_ormbases': ['myshop.Product']},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'product_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['myshop.Product']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'myshop.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_shop.product_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'})
        }
    }

    complete_apps = ['blahblahbuttons']