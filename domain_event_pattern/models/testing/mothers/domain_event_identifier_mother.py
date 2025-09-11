"""
DomainEventIdentifier mother.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.identifiers import StringUuidV4Mother

from domain_event_pattern.models.domain_event_identifier import DomainEventIdentifier


class DomainEventIdentifierMother(BaseMother[DomainEventIdentifier]):
    """
    DomainEventIdentifierMother class is responsible for generating domain event identifiers.

    Example:
    ```python
    from domain_event_pattern.models.testing.mothers import DomainEventIdentifierMother

    identifier = DomainEventIdentifierMother.create()
    print(identifier)
    # >>> 4b5fb882-9d39-4179-94d3-c1d39785b774
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> DomainEventIdentifier:
        """
        Create a domain event identifier. If a specific value is provided via `value`, it is used after validation.
        Otherwise, a random UUID v4 value is generated.

        Args:
            value (str | None, optional): Domain event identifier value. Defaults to None.

        Raises:
            TypeError: If `value` is not a string.
            ValueError: If `value` is an empty string.
            ValueError: If `value` is not a trimmed string.
            ValueError: If `value` is not a valid UUID.
            ValueError: If `value` is not a valid UUID v4.

        Returns:
            DomainEventIdentifier: A domain event identifier.

        Example:
        ```python
        from domain_event_pattern.models.testing.mothers import DomainEventIdentifierMother

        identifier = DomainEventIdentifierMother.create()
        print(identifier)
        # >>> 4b5fb882-9d39-4179-94d3-c1d39785b774
        ```
        """
        if value is not None:
            return DomainEventIdentifier(value=value)

        return DomainEventIdentifier(value=StringUuidV4Mother.create())
