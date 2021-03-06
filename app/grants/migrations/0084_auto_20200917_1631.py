# Generated by Django 2.2.4 on 2020-09-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0083_matchpledge_clr_round_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='gas_price',
            field=models.DecimalField(decimal_places=18, default=1, help_text='The required gas price for the Subscription.', max_digits=50),
        ),
    ]
