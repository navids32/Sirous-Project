# Generated by Django 3.2.4 on 2021-06-13 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_alter_anyitem_status_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anyitem',
            name='brand_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.branditem'),
        ),
        migrations.AlterField(
            model_name='anyitem',
            name='model_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.modelitem'),
        ),
    ]
