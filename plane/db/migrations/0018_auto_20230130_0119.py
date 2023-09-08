# Generated by Django 3.2.16 on 2023-01-29 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import plane.db.models.api_token
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0017_alter_workspace_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_bot',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='description_html',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='description_stripped',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='APIToken',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified At')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('token', models.CharField(default=plane.db.models.api_token.generate_token, max_length=255, unique=True)),
                ('label', models.CharField(default=plane.db.models.api_token.generate_label_token, max_length=255)),
                ('user_type', models.PositiveSmallIntegerField(choices=[(0, 'Human'), (1, 'Bot')], default=0)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apitoken_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apitoken_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Last Modified By')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bot_tokens', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'API Token',
                'verbose_name_plural': 'API Tokems',
                'db_table': 'api_tokens',
                'ordering': ('-created_at',),
            },
        ),
    ]
