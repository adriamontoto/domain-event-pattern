"""
DomainEventIdentifier module.
"""

from value_object_pattern.usables.identifiers import StringUuidV4ValueObject


class DomainEventIdentifier(StringUuidV4ValueObject):
    """
    Value object for domain event identifier.
    """
