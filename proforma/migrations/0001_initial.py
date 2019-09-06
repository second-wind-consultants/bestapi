# Generated by Django 2.0.7 on 2019-09-05 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PLAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=250)),
                ('subcategory', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('note', models.TextField(blank=True, null=True)),
                ('accountnumber', models.CharField(blank=True, max_length=250, null=True)),
                ('pltype', models.CharField(choices=[('REV', 'Revenue'), ('COG', 'Cost of Goods'), ('EXP', 'Expense')], default='EXP', max_length=3)),
            ],
        ),
    ]