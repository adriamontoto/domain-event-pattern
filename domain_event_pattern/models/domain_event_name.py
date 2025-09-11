"""
DomainEventName module.
"""

from value_object_pattern.usables import NotEmptyStringValueObject, PrintableStringValueObject, TrimmedStringValueObject


class DomainEventName(NotEmptyStringValueObject, TrimmedStringValueObject, PrintableStringValueObject):
    """
    Value object for domain event name.
    """
