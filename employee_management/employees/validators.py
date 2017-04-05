from django.core.exceptions import ValidationError
from datetime import datetime

def valid_date(value):
    current = datetime.now().date()
    if value < current:
        raise ValidationError("Zła data")
