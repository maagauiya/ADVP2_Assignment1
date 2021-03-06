# Generated by Django 3.2.9 on 2021-12-02 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(1, 'later'), (2, 'doing'), (3, 'done')], default=2, verbose_name='status')),
            ],
        ),
    ]
