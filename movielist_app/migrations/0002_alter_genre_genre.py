# Generated by Django 4.2.3 on 2023-07-17 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movielist_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Science Fiction', 'Science Fiction'), ('Thriller', 'Thriller'), ('Western', 'Western'), ('Biography', 'Biography'), ('Documentary', 'Documentary'), ('Family', 'Family'), ('Historical', 'Historical'), ('Musical', 'Musical'), ('Noir', 'Noir'), ('Sports', 'Sports'), ('War', 'War')], max_length=50, unique=True),
        ),
    ]