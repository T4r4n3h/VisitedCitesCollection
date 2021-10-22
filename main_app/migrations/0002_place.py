# Generated by Django 3.2.8 on 2021-10-21 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=150)),
                ('style', models.CharField(choices=[('H', 'Historical'), ('S', 'Scientific'), ('V', 'View'), ('I', 'Interesting')], default='I', max_length=1)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.city')),
            ],
        ),
    ]