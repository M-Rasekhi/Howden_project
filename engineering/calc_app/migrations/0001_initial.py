# Generated by Django 2.2.2 on 2019-07-30 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EarthQuake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_class', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], default='D', max_length=1)),
                ('res_mod_coeff', models.DecimalField(decimal_places=5, default=3, max_digits=6, verbose_name='R Value')),
                ('risk_cat', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='2', max_length=100, verbose_name='Risk Category')),
                ('s1', models.DecimalField(decimal_places=5, max_digits=6, verbose_name='S1')),
                ('ss', models.DecimalField(decimal_places=5, max_digits=6, verbose_name='Ss')),
                ('fund_period', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='T')),
                ('long_period', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='TL')),
                ('height', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Height')),
                ('structure_type', models.CharField(choices=[('Steel moment-resisting frames', 'Steel moment-resisting frames'), ('Concrete moment-resisting frames', 'Concrete moment-resisting frames'), ('Steel eccentrically braced frames in accordance with Table 12.2-1 lines B1 or D1', 'Steel eccentrically braced frames in accordance with Table 12.2-1 lines B1 or D1'), ('Steel buckling-restrained braced frames', 'Steel buckling-restrained braced frames'), ('All other structural systems', 'All other structural systems')], default='All other structural systems', max_length=100, verbose_name='Structure Type')),
                ('site_class_calculated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FanUnbalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_grade', models.CharField(choices=[('1', '1'), ('2.5', '2.5'), ('6.3', '6.3')], default='2.5', max_length=10)),
                ('impeller_mass', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fan_speed', models.DecimalField(decimal_places=2, max_digits=10)),
                ('backplate_dia', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Rectangle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rec_height', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_recorded', models.DateField(auto_now=True)),
            ],
        ),
    ]
