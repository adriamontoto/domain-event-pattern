"""
DomainEventOccurredDatetime mother.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover


from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers.dates import StringDatetimeMother

from domain_event_pattern.models.domain_event_occurred_datetime import DomainEventOccurredDatetime


class DomainEventOccurredDatetimeMother(BaseMother[DomainEventOccurredDatetime]):
    """
    DomainEventOccurredDatetimeMother class is responsible for generating domain event occurred datetime values.

    Example:
    ```python
    from domain_event_pattern.models.testing.mothers import DomainEventOccurredDatetimeMother

    occurred_datetime = DomainEventOccurredDatetimeMother.create()
    print(occurred_datetime)
    # >>> 2025-09-11T18:11:41.008191+00:00
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> DomainEventOccurredDatetime:
        """
        Create a domain event occurred datetime. If a specific value is provided via `value`, it is used after
        validation. Otherwise, a random ISO datetime string is generated.

        Args:
            value (str | None, optional): Domain event occurred datetime value. Defaults to None.

        Raises:
            TypeError: If `value` is not a string.
            ValueError: If `value` is an empty string.
            ValueError: If `value` is not a trimmed string.
            ValueError: If `value` is not a valid ISO datetime string.

        Returns:
            DomainEventOccurredDatetime: A domain event occurred datetime.

        Example:
        ```python
        from domain_event_pattern.models.testing.mothers import DomainEventOccurredDatetimeMother

        occurred_datetime = DomainEventOccurredDatetimeMother.create()
        print(occurred_datetime)
        # >>> 2025-09-11T18:11:41.008191+00:00
        ```
        """
        if value is not None:
            return DomainEventOccurredDatetime(value=value)

        return DomainEventOccurredDatetime(value=StringDatetimeMother.create())
