"""
EventHandlerRegistry module.
"""

from typing import Any, ClassVar

from value_object_pattern.decorators import classproperty

from .domain_event import DomainEvent
from .domain_event_subscriber import DomainEventSubscriber


class EventHandlerRegistry:
    """
    Registry for domain event subscribers using decorator registration.
    """

    _subscribers: ClassVar[dict[DomainEventSubscriber[Any], tuple[type[DomainEvent], ...]]] = {}

    @classmethod
    def register(cls, *, subscriber: DomainEventSubscriber[Any], event_types: tuple[type[DomainEvent], ...]) -> None:
        """
        Register a domain event subscriber with its associated event types.

        Args:
            subscriber (DomainEventSubscriber[Any]): The subscriber instance to register.
            event_types (tuple[type[DomainEvent], ...]): The event types this subscriber handles.
        """
        cls._subscribers[subscriber] = event_types

    @classproperty
    def subscribers(self) -> dict[DomainEventSubscriber[Any], tuple[type[DomainEvent], ...]]:
        """
        Get all registered subscribers with their associated event types.

        Returns:
            dict[DomainEventSubscriber[Any], tuple[type[DomainEvent], ...]]: A dictionary mapping subscriber instances
            to tuples of event types they handle.
        """
        return self._subscribers.copy()
