"""
HandlerError module.
"""

from typing import Awaitable, Callable

from domain_event_pattern.models.domain_event import DomainEvent

from .domain_event_pattern_base_error import DomainEventPatternBaseError


class HandlerError(DomainEventPatternBaseError):
    """
    Exception raised when there is an error with a domain event handler.
    """

    _handler: Callable[[DomainEvent], Awaitable[None]]
    _event: DomainEvent
    _error: Exception

    def __init__(
        self,
        *,
        handler: Callable[[DomainEvent], Awaitable[None]],
        event: DomainEvent,
        error: Exception,
    ) -> None:
        """
        Initialize the HandlerError.

        Args:
            handler (Callable[[DomainEvent], Awaitable[None]]): The handler that caused the error.
            event (DomainEvent): The event being processed when the error occurred.
            error (Exception): The original exception that was raised.

        Example:
        ```python
        # TODO:
        ```
        """
        self._handler = handler
        self._event = event
        self._error = error

        message = f'Handler <<<{handler.__name__}>>> failed to process event <<<{event.name}>>> with error <<<{error}>>>.'  # noqa: E501  # fmt: skip
        super().__init__(message=message)

    @property
    def handler(self) -> Callable[[DomainEvent], Awaitable[None]]:
        """
        Get the handler that caused the error.

        Returns:
            Callable[[DomainEvent], Awaitable[None]]: The handler that caused the error.

        Example:
        ```python
        # TODO:
        ```
        """
        return self._handler

    @property
    def event(self) -> DomainEvent:
        """
        Get the event being processed when the error occurred.

        Returns:
            DomainEvent: The event being processed when the error occurred.

        Example:
        ```python
        # TODO:
        ```
        """
        return self._event

    @property
    def error(self) -> Exception:
        """
        Get the original exception that was raised.

        Returns:
            Exception: The original exception that was raised.

        Example:
        ```python
        # TODO:
        ```
        """
        return self._error
