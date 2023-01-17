import uuid
import re
import random

from django.db import models


class Plate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plate_number = models.CharField(max_length=10)

    @classmethod
    def generate_plate(cls, amount=1):
        plates = []
        for _ in range(amount):
            plate = cls(
                plate_number=
                ''.join(random.choice('АВЕКМНОРСТУХ') for _ in range(1)) +
                ''.join(random.choice('0123456789') for _ in range(3)) +
                ''.join(random.choice('АВЕКМНОРСТУХ') for _ in range(2))
            )
            plate.save()
            plates.append(plate)
        return plates

    @classmethod
    def is_valid_plate(cls, plate):
        pattern = '^[АВЕКМНОРСТУХ]{1}[0-9]{3}[АВЕКМНОРСТУХ]{2}$'
        return bool(re.match(pattern, plate))
