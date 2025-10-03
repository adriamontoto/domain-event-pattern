"""
DomainEventSubscriberName module.
"""

from value_object_pattern.usables import NotEmptyStringValueObject, PrintableStringValueObject, TrimmedStringValueObject


class DomainEventSubscriberName(NotEmptyStringValueObject, TrimmedStringValueObject, PrintableStringValueObject):
    """
    Value object for domain event subscriber name.
    """
