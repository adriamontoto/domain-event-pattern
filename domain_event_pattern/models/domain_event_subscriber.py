"""
DomainEventSubscriber module.
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, get_args, get_origin

from value_object_pattern.decorators import classproperty

from .domain_event import DomainEvent

T = TypeVar('T', bound=DomainEvent)


class DomainEventSubscriber(ABC, Generic[T]):  # noqa: UP046
    """
    Interface for domain event subscribers.

    ***This class is abstract and should not be instantiated directly***.

    Example:
    ```python
    # TODO:
    ```
    """

    @abstractmethod
    async def on(self, *, event: T) -> None:
        """
        Handle a domain event.

        Args:
            event (T): The domain event to handle.

        Example:
        ```python
        # TODO:
        ```
        """

    @classproperty
    def subscribed_to(self) -> tuple[type[DomainEvent], ...]:
        """
        Get the types of domain events this subscriber can handle.

        Returns:
            tuple[type[DomainEvent], ...]: A tuple of domain event types that this subscriber can handle.

        Example:
        ```python
        # TODO:
        ```
        """
        for base in self.__orig_bases__:
            origin = get_origin(tp=base)
            if origin is not None and issubclass(origin, DomainEventSubscriber):
                arguments = get_args(tp=base)
                if arguments:
                    union_origin = get_origin(tp=arguments[0])
                    if union_origin is not None:
                        subscriber_events = get_args(tp=arguments[0])
                        return tuple(event for event in subscriber_events if issubclass(event, DomainEvent))

                    subscriber_event = arguments[0]
                    if issubclass(subscriber_event, DomainEvent):
                        return (subscriber_event,)

        return ()
