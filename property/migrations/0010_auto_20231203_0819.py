# Generated by Django 4.2.7 on 2023-12-03 05:07

from django.db import migrations


def transfer_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat', )
    Owner = apps.get_model('property', 'Owner')

    flat_set = Flat.objects.all()
    if flat_set.exists():
        for flat in flat_set.iterator():
            Owner.objects.get_or_create(
                name=flat.owner,
                phone_number=flat.owners_phonenumber,
                pure_phone=flat.owner_pure_phone,
            )


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(transfer_owners),
    ]
