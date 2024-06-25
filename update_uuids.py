import uuid
from django.core.management.base import BaseCommand
from role.models import Role, Nav, Child

class Command(BaseCommand):
    help = 'Update invalid UUIDs in the database'

    def handle(self, *args, **kwargs):
        models = [Role, Nav, Child]

        for model in models:
            instances = model.objects.all()
            for instance in instances:
                try:
                    # Try to convert id to UUID
                    uuid.UUID(str(instance.id))
                except ValueError:
                    # If conversion fails, generate a new UUID
                    instance.id = uuid.uuid4()
                    instance.save()
                    self.stdout.write(self.style.SUCCESS(f'Updated {model.__name__} ID: {instance.id}'))

        self.stdout.write(self.style.SUCCESS('UUID update complete'))
