"""
DeferredEventBus module.
"""

from sys import version_info

if version_info >= (3, 12):
    from typing import override  # pragma: no cover
else:
    from typing_extensions import override  # pragma: no cover

from typing import Sequence

from domain_event_pattern.models import DomainEvent

from .event_bus import EventBus


class DeferredEventBus(EventBus):
    """
    An event bus that defers the publishing of events until explicitly requested.

    Example:
    ```python
    # TODO:
    ```
    """

    _bus: EventBus
    _events: list[DomainEvent]

    def __init__(self, *, bus: EventBus) -> None:
        """
        Initialize the DeferredEventBus with an underlying EventBus.

        Args:
            bus (EventBus): The underlying event bus to use for publishing events.

        Example:
        ```python
        # TODO:
        ```
        """
        self._bus = bus
        self._events = []

    @override
    async def publish(self, *, events: Sequence[DomainEvent]) -> None:
        """
        Publish a sequence of domain events, this will be deferred until `publish_deferred_events` is called.

        Args:
            events (Sequence[DomainEvent]): Sequence of domain events to publish.

        Example:
        ```python
        # TODO:
        ```
        """
        self._events.extend(events)

    async def publish_deferred_events(self) -> None:
        """
        Publish all deferred events.

        Raises:
            PublicationError: If there is an error during publication.

        Example:
        ```python
        # TODO:
        ```
        """
        await self._bus.publish(events=self._events)

        self._events = []
