# Generated by Django 3.2.23 on 2023-11-29 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=45)),
                ('desc', models.CharField(max_length=45)),
                ('website', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=45)),
                ('location', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('logo', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'company',
                'managed': False,
            },
        ),
    ]
