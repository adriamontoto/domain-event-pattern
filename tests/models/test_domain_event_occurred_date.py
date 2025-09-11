"""
Test domain event occurred datetime value object.
"""

from datetime import datetime

from object_mother_pattern import StringDatetimeMother, StringMother
from pytest import mark, raises as assert_raises

from domain_event_pattern.models.domain_event_occurred_datetime import DomainEventOccurredDatetime
from domain_event_pattern.models.testing.mothers import DomainEventOccurredDatetimeMother


@mark.unit_testing
def test_domain_event_occurred_datetime_creation() -> None:
    """
    Test domain event occurred datetime creation with valid value.
    """
    occurred_datetime_value = DomainEventOccurredDatetimeMother.create()

    assert type(occurred_datetime_value.value) is str
    assert datetime.fromisoformat(occurred_datetime_value.value).isoformat() == occurred_datetime_value.value


@mark.unit_testing
def test_domain_event_occurred_datetime_creation_value() -> None:
    """
    Test domain event occurred_datetime creation with valid value.
    """
    domain_event_occurred_datetime_value = DomainEventOccurredDatetimeMother.create().value
    domain_event_occurred_datetime = DomainEventOccurredDatetime(value=domain_event_occurred_datetime_value)

    assert domain_event_occurred_datetime == domain_event_occurred_datetime


@mark.unit_testing
def test_domain_event_occurred_datetime_invalid_type() -> None:
    """
    Test domain event occurred datetime creation with invalid type.
    """
    invalid_occurred_datetime = StringDatetimeMother.invalid_type()

    with assert_raises(
        expected_exception=TypeError,
        match=r'DomainEventOccurredDatetime value <<<.*>>> must be a string. Got <<<.*>>> type.',
    ):
        DomainEventOccurredDatetime(value=invalid_occurred_datetime)


@mark.unit_testing
def test_domain_event_occurred_datetime_invalid_value() -> None:
    """
    Test domain event occurred datetime creation with invalid datetime value.
    """
    invalid_occurred_datetime = StringDatetimeMother.invalid_value()

    with assert_raises(
        expected_exception=ValueError,
        match=r'DomainEventOccurredDatetime value <<<.*>>> is not a valid datetime.',
    ):
        DomainEventOccurredDatetime(value=invalid_occurred_datetime)


@mark.unit_testing
def test_domain_event_occurred_datetime_empty_value() -> None:
    """
    Test domain event occurred datetime creation with empty value.
    """
    invalid_occurred_datetime = StringMother.empty()

    with assert_raises(
        expected_exception=ValueError,
        match=r'DomainEventOccurredDatetime value <<<.*>>> is an empty string. Only non-empty strings are allowed.',
    ):
        DomainEventOccurredDatetime(value=invalid_occurred_datetime)


@mark.unit_testing
def test_domain_event_occurred_datetime_not_trimmed_value() -> None:
    """
    Test domain event occurred datetime creation with not trimmed value.
    """
    invalid_occurred_datetime = StringMother.not_trimmed()

    with assert_raises(
        expected_exception=ValueError,
        match=r'DomainEventOccurredDatetime value <<<.*>>> contains leading or trailing whitespaces. Only trimmed values are allowed.',  # noqa: E501
    ):
        DomainEventOccurredDatetime(value=invalid_occurred_datetime)
