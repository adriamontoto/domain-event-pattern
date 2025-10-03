"""
EventBus module.
"""

from abc import ABC, abstractmethod
from typing import Sequence

from domain_event_pattern.models import DomainEvent


class EventBus(ABC):
    """
    Abstract class for event bus implementations.

    ***This class is abstract and should not be instantiated directly***.

    Example:
    ```python
    # TODO:
    ```
    """

    @abstractmethod
    async def publish(self, *, events: Sequence[DomainEvent]) -> None:
        """
        Publish a sequence of domain events.

        Args:
            events (Sequence[DomainEvent]): Sequence of domain events to publish.

        Raises:
            PublicationError: If there is an error during publication.

        Example:
        ```python
        # TODO:
        ```
        """
