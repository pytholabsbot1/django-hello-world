# Generated by Django 4.2.4 on 2024-02-26 11:23

import cropperjs.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppLeads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('code', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BaseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=50)),
                ('whatsapp', models.CharField(max_length=50)),
                ('test_server', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('booking_date', models.CharField(blank=True, max_length=50, null=True)),
                ('unit_no', models.CharField(blank=True, max_length=50, null=True)),
                ('unit_type', models.CharField(blank=True, default='Discrete', max_length=50, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CashCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(blank=True, max_length=50, null=True)),
                ('item_type', models.CharField(blank=True, default='Discrete', max_length=50, null=True)),
                ('qty', models.CharField(blank=True, max_length=50, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('mobile', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('called', models.BooleanField(default=False, null=True)),
                ('priority', models.BooleanField(default=False, null=True)),
                ('alternate_num', models.CharField(blank=True, max_length=50, null=True)),
                ('wa_num', models.CharField(blank=True, max_length=50, null=True)),
                ('appointment_dt', models.DateTimeField(blank=True, null=True)),
                ('adset_name', models.CharField(blank=True, max_length=100, null=True)),
                ('campaign_name', models.CharField(blank=True, max_length=100, null=True)),
                ('p_interest', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('location_str', models.CharField(blank=True, max_length=1000, null=True)),
                ('purpose', models.CharField(blank=True, max_length=50, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('occupation', models.CharField(blank=True, max_length=500, null=True)),
                ('lead_type', models.CharField(blank=True, choices=[('ORGANIC', 'ORGANIC'), ('PAID', 'PAID')], max_length=50, null=True)),
                ('occupation_type', models.CharField(blank=True, choices=[('SALARIED', 'SALARIED'), ('BUSINESS', 'BUSINESS'), ('RETIRED', 'RETIRED')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeadList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('filter_string', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeadLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeadSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('starting_price', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('duration', models.CharField(blank=True, max_length=200, null=True)),
                ('project_type', models.CharField(blank=True, max_length=200, null=True)),
                ('alert', models.CharField(blank=True, max_length=200, null=True)),
                ('tour', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(max_length=10000)),
                ('listing_image', cropperjs.models.CropperImageField(aspectratio=1.5, null=True, upload_to='')),
                ('total_area', models.CharField(blank=True, max_length=200, null=True)),
                ('unit_types', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('total_units', models.CharField(blank=True, max_length=200, null=True)),
                ('bathrooms', models.CharField(blank=True, max_length=200, null=True)),
                ('open_area', models.CharField(blank=True, max_length=200, null=True)),
                ('rera', models.CharField(blank=True, max_length=200, null=True)),
                ('card_key', models.CharField(blank=True, max_length=200, null=True)),
                ('brochure', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='NotifyEmails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=200, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('cus_img', cropperjs.models.CropperImageField(aspectratio=1, null=True, upload_to='')),
                ('cus_name', models.CharField(max_length=50, null=True)),
                ('cus_designation', models.CharField(max_length=50, null=True)),
                ('cus_prod', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TourPics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField(default=0, null=True)),
                ('pitch', models.CharField(blank=True, max_length=20, null=True)),
                ('yaw', models.CharField(blank=True, max_length=20, null=True)),
                ('scene_text', models.CharField(blank=True, max_length=20, null=True)),
                ('scene_id', models.CharField(blank=True, max_length=20, null=True)),
                ('scene_img', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TravelledKms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kms', models.CharField(blank=True, max_length=50, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('mode', models.CharField(blank=True, choices=[('Income', 'Income'), ('Expense', 'Expense')], max_length=50, null=True)),
                ('amount', models.CharField(blank=True, max_length=50, null=True)),
                ('head', models.TextField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.cashcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', cropperjs.models.CropperImageField(aspectratio=1, null=True, upload_to='')),
                ('head', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=50)),
                ('occ', models.CharField(max_length=50)),
                ('remarks', models.CharField(max_length=100)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example.listing')),
            ],
        ),
        migrations.CreateModel(
            name='Reimbursement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('amount', models.CharField(blank=True, max_length=50, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NearbyPlaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=500)),
                ('distance', models.CharField(max_length=50)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example.listing')),
            ],
        ),
        migrations.CreateModel(
            name='MarkLeads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
                ('stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example.stage')),
            ],
        ),
        migrations.CreateModel(
            name='LeadStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField(blank=True, null=True)),
                ('call_by', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('lead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example.lead')),
                ('stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example.stage')),
            ],
        ),
        migrations.AddField(
            model_name='lead',
            name='Location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='example.leadlocation'),
        ),
        migrations.AddField(
            model_name='lead',
            name='Source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='example.leadsource'),
        ),
        migrations.AddField(
            model_name='lead',
            name='product_interested',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='example.product'),
        ),
        migrations.CreateModel(
            name='KeyPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example.listing')),
            ],
        ),
        migrations.CreateModel(
            name='JCB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('mode', models.CharField(blank=True, choices=[('START', 'START'), ('STOP', 'STOP')], max_length=50, null=True)),
                ('photo', cropperjs.models.CropperImageField(aspectratio=1.5, blank=True, null=True, upload_to='')),
                ('remarks', models.TextField(blank=True, null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cropperjs.models.CropperImageField(aspectratio=1.5, null=True, upload_to='')),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example.listing')),
            ],
        ),
        migrations.CreateModel(
            name='FloorPlanType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('yt_link', models.TextField(blank=True, null=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example.listing')),
            ],
        ),
        migrations.CreateModel(
            name='FloorPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('plan', models.FileField(blank=True, null=True, upload_to='')),
                ('sold_out', models.BooleanField(default=False, null=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example.listing')),
                ('tp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='example.floorplantype')),
            ],
        ),
        migrations.CreateModel(
            name='ElectricityReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', cropperjs.models.CropperImageField(aspectratio=1.5, null=True, upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DownloadLeads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='example.leadlocation')),
            ],
        ),
        migrations.CreateModel(
            name='Construction_Updates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('image', cropperjs.models.CropperImageField(aspectratio=1.5, null=True, upload_to='')),
                ('text', models.TextField(blank=True, null=True)),
                ('unit_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example.booking')),
            ],
        ),
        migrations.CreateModel(
            name='CallLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.lead')),
            ],
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(max_length=50)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example.listing')),
            ],
        ),
        migrations.CreateModel(
            name='AgentAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.leadlocation')),
            ],
        ),
    ]
