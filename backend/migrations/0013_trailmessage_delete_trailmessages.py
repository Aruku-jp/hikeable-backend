# Generated by Django 4.1.3 on 2022-12-09 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_merge_0009_trailmessages_0011_remove_account_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrailMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=12)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=13)),
                ('message', models.TextField()),
                ('likes', models.IntegerField(blank=True)),
                ('dislikes', models.IntegerField(blank=True)),
                ('date', models.DateField()),
                ('trail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.trail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.account')),
            ],
        ),
        migrations.DeleteModel(
            name='TrailMessages',
        ),
    ]
