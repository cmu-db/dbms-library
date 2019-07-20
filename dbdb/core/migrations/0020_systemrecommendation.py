# Generated by Django 2.0.13 on 2019-07-19 02:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20190717_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendation_from', to='core.System')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendation_to', to='core.System')),
            ],
        ),
    ]
