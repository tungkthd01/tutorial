# Generated by Django 3.2.9 on 2021-11-18 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20211111_1457'),
        ('event', '0005_alter_image_paths_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performances',
            fields=[
                ('performance_id', models.IntegerField(primary_key=True, serialize=False)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('ticket_available_flag', models.BooleanField()),
            ],
            options={
                'db_table': 'performance',
            },
        ),
        migrations.AlterField(
            model_name='events',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='user.clients'),
        ),
        migrations.AlterField(
            model_name='image_paths',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('ticket_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=0, max_digits=15, null=True)),
                ('drawing_flag', models.BooleanField()),
                ('drawing_application_deadline', models.DateTimeField(null=True)),
                ('drawing_status', models.BooleanField()),
                ('performance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performance', to='event.performances')),
            ],
            options={
                'db_table': 'ticket',
            },
        ),
        migrations.AddField(
            model_name='performances',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='event.events'),
        ),
    ]
