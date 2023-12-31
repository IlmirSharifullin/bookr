# Generated by Django 4.2.6 on 2023-12-06 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_book_contributor_review_bookcontributor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='created_at',
            new_name='date_created',
        ),
        migrations.RemoveField(
            model_name='review',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='review',
            name='date_edited',
            field=models.DateTimeField(help_text='The date and time the review was last edited.', null=True),
        ),
    ]
