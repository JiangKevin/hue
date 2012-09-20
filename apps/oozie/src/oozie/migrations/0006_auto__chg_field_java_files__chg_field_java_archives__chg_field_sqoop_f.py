# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'Java.files'
        db.alter_column('oozie_java', 'files', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Java.archives'
        db.alter_column('oozie_java', 'archives', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sqoop.files'
        db.alter_column('oozie_sqoop', 'files', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sqoop.archives'
        db.alter_column('oozie_sqoop', 'archives', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Pig.files'
        db.alter_column('oozie_pig', 'files', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Pig.archives'
        db.alter_column('oozie_pig', 'archives', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Mapreduce.files'
        db.alter_column('oozie_mapreduce', 'files', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Mapreduce.archives'
        db.alter_column('oozie_mapreduce', 'archives', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Streaming.files'
        db.alter_column('oozie_streaming', 'files', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Streaming.archives'
        db.alter_column('oozie_streaming', 'archives', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Shell.files'
        db.alter_column('oozie_shell', 'files', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Shell.archives'
        db.alter_column('oozie_shell', 'archives', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Hive.files'
        db.alter_column('oozie_hive', 'files', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Hive.archives'
        db.alter_column('oozie_hive', 'archives', self.gf('django.db.models.fields.TextField')())
    
    
    def backwards(self, orm):
        
        # Changing field 'Java.files'
        db.alter_column('oozie_java', 'files', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Java.archives'
        db.alter_column('oozie_java', 'archives', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Sqoop.files'
        db.alter_column('oozie_sqoop', 'files', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Sqoop.archives'
        db.alter_column('oozie_sqoop', 'archives', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Pig.files'
        db.alter_column('oozie_pig', 'files', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Pig.archives'
        db.alter_column('oozie_pig', 'archives', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Mapreduce.files'
        db.alter_column('oozie_mapreduce', 'files', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Mapreduce.archives'
        db.alter_column('oozie_mapreduce', 'archives', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Streaming.files'
        db.alter_column('oozie_streaming', 'files', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Streaming.archives'
        db.alter_column('oozie_streaming', 'archives', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Shell.files'
        db.alter_column('oozie_shell', 'files', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Shell.archives'
        db.alter_column('oozie_shell', 'archives', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Hive.files'
        db.alter_column('oozie_hive', 'files', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'Hive.archives'
        db.alter_column('oozie_hive', 'archives', self.gf('django.db.models.fields.CharField')(max_length=512))
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'oozie.coordinator': {
            'Meta': {'object_name': 'Coordinator', '_ormbases': ['oozie.Job']},
            'concurrency': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'end': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 23, 14, 58, 35, 963525)'}),
            'execution': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'frequency_number': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'frequency_unit': ('django.db.models.fields.CharField', [], {'default': "'days'", 'max_length': '20'}),
            'job_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Job']", 'unique': 'True', 'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 20, 14, 58, 35, 963495)'}),
            'throttle': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'timeout': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'America/Los_Angeles'", 'max_length': '24'}),
            'workflow': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oozie.Workflow']", 'null': 'True'})
        },
        'oozie.datainput': {
            'Meta': {'object_name': 'DataInput'},
            'coordinator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oozie.Coordinator']"}),
            'dataset': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Dataset']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'oozie.dataoutput': {
            'Meta': {'object_name': 'DataOutput'},
            'coordinator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oozie.Coordinator']"}),
            'dataset': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Dataset']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'oozie.dataset': {
            'Meta': {'object_name': 'Dataset'},
            'coordinator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oozie.Coordinator']"}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'done_flag': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64', 'blank': 'True'}),
            'frequency_number': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'frequency_unit': ('django.db.models.fields.CharField', [], {'default': "'days'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 20, 14, 58, 35, 964734)'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'America/Los_Angeles'", 'max_length': '24'}),
            'uri': ('django.db.models.fields.CharField', [], {'default': "'/data/${YEAR}${MONTH}${DAY}'", 'max_length': '1024'})
        },
        'oozie.end': {
            'Meta': {'object_name': 'End'},
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Node']", 'unique': 'True', 'primary_key': 'True'})
        },
        'oozie.fork': {
            'Meta': {'object_name': 'Fork'},
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Node']", 'unique': 'True', 'primary_key': 'True'})
        },
        'oozie.history': {
            'Meta': {'object_name': 'History'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oozie.Job']"}),
            'oozie_job_id': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'properties': ('django.db.models.fields.TextField', [], {}),
            'submission_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'submitter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'oozie.hive': {
            'Meta': {'object_name': 'Hive'},
            'archives': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'files': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'job_properties': ('django.db.models.fields.TextField', [], {'default': '\'[{"name":"oozie.use.system.libpath","value":"true"},{"name":"oozie.hive.defaults","value":"${hive.default.xml}"}]\''}),
            'job_xml': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512', 'blank': 'True'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'params': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'prepares': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'script_path': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'oozie.java': {
            'Meta': {'object_name': 'Java'},
            'archives': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'args': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'blank': 'True'}),
            'files': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'jar_path': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'java_opts': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'job_properties': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'job_xml': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512', 'blank': 'True'}),
            'main_class': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'prepares': ('django.db.models.fields.TextField', [], {'default': "'[]'"})
        },
        'oozie.job': {
            'Meta': {'object_name': 'Job'},
            'deployment_dir': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_shared': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True', 'blank': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'parameters': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'schema_version': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'oozie.join': {
            'Meta': {'object_name': 'Join'},
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Node']", 'unique': 'True', 'primary_key': 'True'})
        },
        'oozie.kill': {
            'Meta': {'object_name': 'Kill'},
            'message': ('django.db.models.fields.CharField', [], {'default': "'Action failed, error message[${wf:errorMessage(wf:lastErrorNode())}]'", 'max_length': '256'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Node']", 'unique': 'True', 'primary_key': 'True'})
        },
        'oozie.link': {
            'Meta': {'object_name': 'Link'},
            'child': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parent_node'", 'to': "orm['oozie.Node']"}),
            'comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'child_node'", 'to': "orm['oozie.Node']"})
        },
        'oozie.mapreduce': {
            'Meta': {'object_name': 'Mapreduce'},
            'archives': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'files': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'jar_path': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'job_properties': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'job_xml': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512', 'blank': 'True'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Node']", 'unique': 'True'}),
            'prepares': ('django.db.models.fields.TextField', [], {'default': "'[]'"})
        },
        'oozie.node': {
            'Meta': {'object_name': 'Node'},
            'children': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'parents'", 'symmetrical': 'False', 'through': "orm['oozie.Link']", 'to': "orm['oozie.Node']"}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'node_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'workflow': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oozie.Workflow']"})
        },
        'oozie.pig': {
            'Meta': {'object_name': 'Pig'},
            'archives': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'files': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'job_properties': ('django.db.models.fields.TextField', [], {'default': '\'[{"name":"oozie.use.system.libpath","value":"true"}]\''}),
            'job_xml': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512', 'blank': 'True'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'params': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'prepares': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'script_path': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'oozie.shell': {
            'Meta': {'object_name': 'Shell'},
            'archives': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'capture_output': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'command': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'files': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'job_properties': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'job_xml': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512', 'blank': 'True'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'params': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'prepares': ('django.db.models.fields.TextField', [], {'default': "'[]'"})
        },
        'oozie.sqoop': {
            'Meta': {'object_name': 'Sqoop'},
            'archives': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'files': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'job_properties': ('django.db.models.fields.TextField', [], {'default': '\'[{"name":"oozie.use.system.libpath","value":"true"}]\''}),
            'job_xml': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512', 'blank': 'True'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'params': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'prepares': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'script_path': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'blank': 'True'})
        },
        'oozie.ssh': {
            'Meta': {'object_name': 'Ssh'},
            'capture_output': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'command': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'params': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'oozie.start': {
            'Meta': {'object_name': 'Start'},
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Node']", 'unique': 'True'})
        },
        'oozie.streaming': {
            'Meta': {'object_name': 'Streaming'},
            'archives': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'files': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'job_properties': ('django.db.models.fields.TextField', [], {'default': '\'[{"name":"oozie.use.system.libpath","value":"true"}]\''}),
            'mapper': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'node_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Node']", 'unique': 'True', 'primary_key': 'True'}),
            'reducer': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'oozie.workflow': {
            'Meta': {'object_name': 'Workflow', '_ormbases': ['oozie.Job']},
            'end': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'end_workflow'", 'null': 'True', 'to': "orm['oozie.End']"}),
            'is_single': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'job_properties': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'job_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['oozie.Job']", 'unique': 'True', 'primary_key': 'True'}),
            'job_xml': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '512', 'blank': 'True'}),
            'start': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'start_workflow'", 'null': 'True', 'to': "orm['oozie.Start']"})
        }
    }
    
    complete_apps = ['oozie']
