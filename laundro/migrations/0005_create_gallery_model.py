# Generated by Django 2.2.16 on 2020-11-12 10:32

from django.db import migrations, models
import django.db.models.deletion
import laundro.models
import laundro.vallidators
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('laundro', '0004_create_order_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=80, unique=True)),
                ('content_type', models.CharField(choices=[('img', 'Image'), ('vid', 'Video')], max_length=3)),
                ('media', models.ImageField(blank=True, max_length=512, null=True, upload_to=laundro.models.get_gallery_media_upload_path, validators=[laundro.vallidators.validate_media_file_extension])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('rcv', 'Recieved'), ('inp', 'In Progress'), ('com', 'Completed'), ('ful', 'Fulfilles')], default='rcv', max_length=3),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('rcv', 'Recieved'), ('inp', 'In Progress'), ('com', 'Completed'), ('ful', 'Fulfilles')], default='rcv', max_length=3)),
                ('cost', models.FloatField()),
                ('amount', models.PositiveIntegerField(default=1)),
                ('total_cost', models.FloatField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='laundro.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='laundro.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
