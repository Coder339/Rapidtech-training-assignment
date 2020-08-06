import re
from django.core.exceptions import ValidationError

def validate_phone_number(phone):
    """Validate the phone number to match expected format"""

    p = re.compile(r'\d{3}\s?\d{3}\s?\d{4}')

    if not p.fullmatch(phone):
        raise ValidationError(
            "Phone number must be of the format xxx xxx xxxx"
        )
