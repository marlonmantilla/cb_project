# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'Envio', fields ['guia']
        db.delete_unique('shippings_envio', ['guia'])


    def backwards(self, orm):
        
        # Adding unique constraint on 'Envio', fields ['guia']
        db.create_unique('shippings_envio', ['guia'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'offers.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'main_category'", 'null': 'True', 'blank': 'True', 'to': "orm['offers.Categoria']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'offers.oferta': {
            'Meta': {'object_name': 'Oferta'},
            'activa': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['offers.Categoria']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'oferta_del_dia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'precio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'precio_anterior': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'productos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['offers.Producto']", 'symmetrical': 'False', 'blank': 'True'}),
            'tienda': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['offers.Tienda']", 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'offers.producto': {
            'Meta': {'object_name': 'Producto'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {'default': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Profile']", 'null': 'True', 'blank': 'True'}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'offers.tienda': {
            'Meta': {'object_name': 'Tienda'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['offers.Categoria']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            'about_me': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'ciudadcasa': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ciudadofi': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dircasa': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dirofi': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'es'", 'max_length': '5'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'mugshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'privacy': ('django.db.models.fields.CharField', [], {'default': "'registered'", 'max_length': '15'}),
            'telcasa': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'telofi': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['auth.User']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'shippings.envio': {
            'Meta': {'object_name': 'Envio'},
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'comprado': ('django.db.models.fields.CharField', [], {'default': "'Por usuario'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'guia': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'oferta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['offers.Oferta']", 'null': 'True', 'blank': 'True'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'productos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['offers.Producto']", 'symmetrical': 'False'}),
            'proveedor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'transportadora': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shippings.Transportadora']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Profile']", 'null': 'True', 'blank': 'True'})
        },
        'shippings.transportadora': {
            'Meta': {'object_name': 'Transportadora'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['shippings']
