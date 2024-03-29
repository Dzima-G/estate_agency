# Generated by Django 4.2.7 on 2023-12-04 17:09

from django.db import migrations


def bind_owner_with_flat(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat', )
    Owner = apps.get_model('property', 'Owner')

    owner_set = Owner.objects.all()
    if owner_set.exists():
        for owner in owner_set.iterator():
            owner.owned_apartments.set(Flat.objects.filter(owner_deprecated=owner.name).only('id'))


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0011_rename_owner_flat_owner_deprecated_alter_owner_name'),
    ]

    operations = [
        migrations.RunPython(bind_owner_with_flat),
    ]
