"""
Custom Validators.
"""

import re
from django.core.exceptions import ValidationError


def validate_mobile_format(value):
    """
    Check for correct mobile number.
    """
    match = re.match(r'^[6789]\d{9}$', str(value))
    if match is None:
        raise ValidationError("Wrong mobile number.")
    if int(value) in [6666666666, 7777777777, 8888888888, 9999999999]:
        raise ValidationError("Wrong mobile number.")


def validate_email_format(value):
    """
    Check for correct email.
    """
    match = re.match(
        r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', value)
    if match is None:
        raise ValidationError("Wrong Email format.")
