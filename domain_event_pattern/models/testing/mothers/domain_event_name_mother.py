"""
DomainEventName mother.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from object_mother_pattern.models import BaseMother
from object_mother_pattern.mothers import StringMother

from domain_event_pattern.models.domain_event_name import DomainEventName


class DomainEventNameMother(BaseMother[DomainEventName]):
    """
    DomainEventNameMother class is responsible for generating domain event names.

    Example:
    ```python
    from domain_event_pattern.models.testing.mothers import DomainEventNameMother

    name = DomainEventNameMother.create()
    print(name)
    # >>> user.created
    ```
    """

    @classmethod
    @override
    def create(cls, *, value: str | None = None) -> DomainEventName:
        """
        Create a domain event name. If a specific value is provided via `value`, it is used after validation.
        Otherwise, a random string value is generated.

        Args:
            value (str | None, optional): Domain event name value. Defaults to None.

        Raises:
            TypeError: If `value` is not a string.
            ValueError: If `value` is empty.
            ValueError: If `value` is not a trimmed string.
            ValueError: If `value` contains invalid characters.

        Returns:
            DomainEventName: A domain event name.

        Example:
        ```python
        from domain_event_pattern.models.testing.mothers import DomainEventNameMother

        name = DomainEventNameMother.create()
        print(name)
        # >>> user.created
        ```
        """
        if value is not None:
            return DomainEventName(value=value)

        return DomainEventName(value=StringMother.create())
