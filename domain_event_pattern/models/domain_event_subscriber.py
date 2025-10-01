"""
DomainEventSubscriber module.
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, get_args, get_origin, override

from value_object_pattern.decorators import classproperty

from .domain_event import DomainEvent
from .domain_event_subscriber_name import DomainEventSubscriberName

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

    _name: str

    @override
    def __init_subclass__(cls, **kwargs: object) -> None:
        """
        Validate subscriber name when subclass is defined.

        Raises:
            ValueError: If the subscriber name class attribute is not defined.
        """
        super().__init_subclass__(**kwargs)

        if not hasattr(cls, '_name') or cls._name is None:
            raise ValueError(f'{cls.__name__} must define _name class attribute.')

        DomainEventSubscriberName(value=cls._name, title=cls.__name__, parameter='_name')

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
    def name(self) -> str:
        """
        Get the name of the subscriber.

        Raises:
            ValueError: If the subscriber name class attribute is not defined.

        Returns:
            str: The subscriber of the event.

        Example:
        ```python
        # TODO:
        ```
        """  # noqa: E501  # fmt: skip
        if not hasattr(self, '_name') or self._name is None:
            raise ValueError(f'{self.__name__} must define _name class attribute.')  # type: ignore[attr-defined]

        return self._name

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
        for base in self.__orig_bases__:  # type: ignore[attr-defined]
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
