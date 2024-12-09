import re
from datetime import datetime

FIELD_TYPES = {
    "email": "email",
    "phone": "phone",
    "date": "date",
    "text": "text"
}

def validate_field(value, field_type):
    if field_type == "email":
        return re.match(r"[^@]+@[^@]+\.[^@]+", value)
    elif field_type == "phone":
        return re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value)
    elif field_type == "date":
        try:
            datetime.strptime(value, "%d.%m.%Y")
            return True
        except ValueError:
            try:
                datetime.strptime(value, "%Y-%m-%d")
                return True
            except ValueError:
                return False
    else:
        return True
