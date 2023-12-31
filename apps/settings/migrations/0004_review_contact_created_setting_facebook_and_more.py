# Generated by Django 4.2.4 on 2023-09-06 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_benefit_contact_team_alter_news_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=400, verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AddField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата заявки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='setting',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='setting',
            name='tiktok',
            field=models.URLField(blank=True, null=True, verbose_name='TikTok'),
        ),
        migrations.AddField(
            model_name='setting',
            name='whatsapp',
            field=models.URLField(blank=True, null=True, verbose_name='WhatsApp'),
        ),
    ]
