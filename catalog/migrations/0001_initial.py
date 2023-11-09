# Generated by Django 4.2.7 on 2023-11-09 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('category', models.IntegerField(choices=[(1, 'Product'), (2, 'Service'), (3, 'Other')], default=2)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='catalogs')),
                ('is_featured', models.BooleanField(default=False)),
                ('is_popular', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Catalogs',
                'ordering': ['-is_featured', '-is_popular', '-is_new', 'name'],
                'get_latest_by': 'created_at',
            },
        ),
    ]
