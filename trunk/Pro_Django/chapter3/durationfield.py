import datetime
import re

from django.core.exceptions import ValidationError

from django.db import models
from django.db.models.fields.subclassing import SubfieldBase
from django.utils import _decimal

class DurationField(models.DecimalField):
    __metaclass__ = SubfieldBase

    def get_db_prep_value(self, value):
        return _decimal.Decimal('%s.%s' % (value.days * 86400 + value.seconds,
                                           value.microseconds))

    def to_python(self, value):
        if isinstance(value, datetime.timedelta):
            return value
        match = re.match(r'(?:(\d+) days?, )?(\d+):(\d+):(\d+)(?:\.(\d+))?', str(value))
        if match:
            parts = list(match.groups())
            # The parts in this list are as follows:
            # [days, hours, minutes, seconds, microseconds]
            # But microseconds need to be padded with zeros to work properly.
            parts[4] = parts[4].ljust(6, '0')
            # And they all need to be converted to integers, defaulting to 0
            parts = [part and int(part) or 0 for part in parts]
    
            return datetime.timedelta(parts[0], parts[3], parts[4],
                                      hours=parts[1], minutes=parts[2])
        try:
            return datetime.timedelta(seconds=float(value))
        except (TypeError, ValueError):
            raise ValidationError('This value must be a real number.')
        except OverflowError:
            raise ValidationError('The maximum allowed value is %s' % \
                                  datetime.timedelta.max)

if __name__ == '__main__':
    field = DurationField()
    assert field.to_python('1.23') == datetime.timedelta(seconds=1.23)
    assert field.to_python(1.23) == datetime.timedelta(seconds=1.23)
    assert field.to_python('3 days, 1:03:15.123456') == \
           datetime.timedelta(days=3, hours=1, seconds=15, minutes=3,
                              microseconds=123456)
