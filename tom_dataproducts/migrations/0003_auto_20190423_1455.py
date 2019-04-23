# Generated by Django 2.1.7 on 2019-04-23 14:55

from django.db import migrations, models
import tom_dataproducts.models


class Migration(migrations.Migration):

    dependencies = [
        ('tom_dataproducts', '0002_auto_20190409_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataproduct',
            name='thumbnail',
            field=models.FileField(default=None, null=True, upload_to=tom_dataproducts.models.data_product_path),
        ),
        migrations.AlterField(
            model_name='reduceddatum',
            name='data_type',
            field=models.CharField(choices=[('SPECTROSCOPY', 'Spectroscopy'), ('PHOTOMETRY', 'Photometry')], default='', max_length=100),
        ),
    ]
