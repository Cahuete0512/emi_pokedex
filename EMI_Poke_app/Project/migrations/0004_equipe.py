# Generated by Django 4.1.3 on 2022-11-25 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0003_remove_pokemon_catchrate_remove_pokemon_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pokemons', models.ManyToManyField(to='Project.pokemon')),
            ],
        ),
    ]
