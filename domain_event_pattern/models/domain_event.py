"""
DomainEvent module.
"""

from __future__ import annotations

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from datetime import UTC, datetime
from typing import Any
from uuid import uuid4

from value_object_pattern import BaseModel
from value_object_pattern.decorators import classproperty

from .domain_event_aggregate_identifier import DomainEventAggregateIdentifier
from .domain_event_identifier import DomainEventIdentifier
from .domain_event_name import DomainEventName
from .domain_event_occurred_datetime import DomainEventOccurredDatetime


class DomainEvent(BaseModel):
    """
    Base class for all domain events.

    ***This class is abstract and should not be instantiated directly***.

    Example:
    ```python
    # TODO:
    ```
    """  # noqa: E501  # fmt: skip

    _identifier: DomainEventIdentifier
    _aggregate_identifier: DomainEventAggregateIdentifier
    _name: str  # Define this attribute in subclasses
    _occurred_datetime: DomainEventOccurredDatetime

    @override
    def __init_subclass__(cls, **kwargs: object) -> None:
        """
        Validate event name when subclass is defined.
        """
        super().__init_subclass__(**kwargs)

        if not hasattr(cls, '_name') or cls._name is None:
            raise ValueError(f'{cls.__name__} must define _name class attribute.')

        DomainEventName(value=cls._name, title=cls.__name__, parameter='_name')

    def __init__(
        self,
        *,
        aggregate_identifier: str,
        identifier: str | None = None,
        occurred_datetime: str | None = None,
    ) -> None:
        """
        Initialize a domain event.

        Args:
            identifier (str | None, optional): The unique identifier for the event. Defaults to random UUIDv4.
            aggregate_identifier (str): The identifier of the aggregate root associated with the event.
            occurred_datetime (str | None, optional): When the event occurred. Defaults to UTC now.

        Raises:
            ValueError: If the event name class attribute is not defined.

        Example:
        ```python
        # TODO:
        ```
        """  # noqa: E501  # fmt: skip
        if identifier is None:
            identifier = str(uuid4())

        if occurred_datetime is None:
            occurred_datetime = datetime.now(tz=UTC).isoformat()

        self._aggregate_identifier = DomainEventAggregateIdentifier(value=aggregate_identifier, title='DomainEvent', parameter='aggregate_identifier')  # noqa: E501  # fmt: skip
        self._identifier = DomainEventIdentifier(value=identifier, title='DomainEvent', parameter='identifier')
        self._occurred_datetime = DomainEventOccurredDatetime(value=occurred_datetime, title='DomainEvent', parameter='occurred_datetime')  # noqa: E501  # fmt: skip

    @override
    @classmethod
    def from_primitives(cls, primitives: dict[str, Any]) -> DomainEvent:
        """
        Create a domain event from a dictionary of primitive types.

        Args:
            data (dict[str, Any]): A dictionary representation of the domain event.

        Returns:
            DomainEvent: An instance of the domain event.

        Example:
        ```python
        # TODO:
        ```
        """  # noqa: E501  # fmt: skip
        name = primitives.get('name')
        identifier = primitives.get('identifier')
        aggregate_identifier = primitives.get('aggregate_identifier')
        occurred_datetime = primitives.get('occurred_datetime')
        event_data = primitives.get('data', {})

        if name != cls.name:
            raise ValueError(f'DomainEvent name mismatch expected <<<{cls.name}>>> got <<<{name}>>>.')

        return cls(
            identifier=identifier,
            aggregate_identifier=aggregate_identifier,  # type: ignore[arg-type]
            occurred_datetime=occurred_datetime,
            **event_data,
        )

    @override
    def to_primitives(self) -> dict[str, Any]:
        """
        Convert the domain event to a dictionary of primitive types.

        Returns:
            dict[str, Any]: A dictionary representation of the domain event.

        Example:
        ```python
        # TODO:
        ```
        """  # noqa: E501  # fmt: skip
        event_data = super().to_primitives()
        event_data.pop('name', None)
        event_data.pop('identifier', None)
        event_data.pop('aggregate_identifier', None)
        event_data.pop('occurred_datetime', None)

        return {
            'name': self.name,
            'identifier': self.identifier,
            'aggregate_identifier': self.aggregate_identifier,
            'occurred_datetime': self.occurred_datetime,
            'data': event_data,
        }

    @property
    def identifier(self) -> str:
        """
        Get the unique identifier for the event.

        Returns:
            str: The unique identifier for the event.

        Example:
        ```python
        # TODO:
        ```
        """  # noqa: E501  # fmt: skip
        return self._identifier.value

    @property
    def aggregate_identifier(self) -> str:
        """
        Get the identifier of the aggregate root associated with the event.

        Returns:
            str: The identifier of the aggregate root associated with the event.

        Example:
        ```python
        # TODO:
        ```
        """
        return self._aggregate_identifier.value

    @classproperty
    def name(self) -> str:
        """
        Get the name of the event.

        Raises:
            ValueError: If the event name class attribute is not defined.

        Returns:
            str: The name of the event.

        Example:
        ```python
        # TODO:
        ```
        """  # noqa: E501  # fmt: skip
        if not hasattr(self, '_name') or self._name is None:
            raise ValueError(f'{self.__name__} must define _name class attribute.')  # type: ignore[attr-defined]

        return self._name

    @property
    def occurred_datetime(self) -> str:
        """
        Get the timestamp when the event occurred.

        Returns:
            str: The timestamp when the event occurred.

        Example:
        ```python
        # TODO:
        ```
        """  # noqa: E501  # fmt: skip
        return self._occurred_datetime.value
