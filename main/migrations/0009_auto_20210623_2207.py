# Generated by Django 3.2.3 on 2021-06-24 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210621_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='num_documento',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='tipo_comprobante',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='tipo_documento',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
