# Generated by Django 3.2.9 on 2021-11-11 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20211111_1432'),
        ('event', '0003_auto_20211110_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='image_paths',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=255)),
                ('dir_path', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255)),
                ('display_order', models.SmallIntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.events')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.users')),
            ],
            options={
                'db_table': 'image_path',
            },
        ),
    ]
