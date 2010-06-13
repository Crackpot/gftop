# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SearchKeyword'
        db.create_table('search_searchkeyword', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flatpages.FlatPage'])),
        ))
        db.send_create_signal('search', ['SearchKeyword'])


    def backwards(self, orm):
        
        # Deleting model 'SearchKeyword'
        db.delete_table('search_searchkeyword')


    models = {
        'flatpages.flatpage': {
            'Meta': {'object_name': 'FlatPage', 'db_table': "'django_flatpage'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'search.searchkeyword': {
            'Meta': {'object_name': 'SearchKeyword'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flatpages.FlatPage']"})
        },
        'sites.site': {
            'Meta': {'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['search']
