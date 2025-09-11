"""
Test domain event name value object.
"""

from object_mother_pattern import StringMother
from pytest import mark, raises as assert_raises

from domain_event_pattern.models.domain_event_name import DomainEventName
from domain_event_pattern.models.testing.mothers import DomainEventNameMother


@mark.unit_testing
def test_domain_event_name_creation() -> None:
    """
    Test domain event name creation with valid value.
    """
    domain_event_name = DomainEventNameMother.create()

    assert type(domain_event_name.value) is str


@mark.unit_testing
def test_domain_event_name_creation_value() -> None:
    """
    Test domain event name creation with valid value.
    """
    domain_event_name_value = DomainEventNameMother.create().value
    domain_event_name = DomainEventName(value=domain_event_name_value)

    assert domain_event_name == domain_event_name


@mark.unit_testing
def test_domain_event_name_invalid_type() -> None:
    """
    Test domain event name creation with invalid type.
    """
    invalid_name = StringMother.invalid_type()

    with assert_raises(
        expected_exception=TypeError,
        match=r'DomainEventName value <<<.*>>> must be a string. Got <<<.*>>> type.',
    ):
        DomainEventName(value=invalid_name)


@mark.unit_testing
def test_domain_event_name_invalid_value() -> None:
    """
    Test domain event name creation with invalid characters.
    """
    invalid_name = StringMother.invalid_value()

    with assert_raises(
        expected_exception=ValueError,
        match=r'DomainEventName value <<<.*>>> contains invalid characters. Only printable characters are allowed.',
    ):
        DomainEventName(value=invalid_name)


@mark.unit_testing
def test_domain_event_name_not_trimmed() -> None:
    """
    Test domain event name creation with not trimmed value.
    """
    invalid_name = StringMother.not_trimmed()

    with assert_raises(
        expected_exception=ValueError,
        match=r'DomainEventName value <<<.*>>> contains leading or trailing whitespaces. Only trimmed values are allowed.',  # noqa: E501
    ):
        DomainEventName(value=invalid_name)


@mark.unit_testing
def test_domain_event_name_empty_value() -> None:
    """
    Test domain event name creation with empty value.
    """
    invalid_name = StringMother.empty()

    with assert_raises(
        expected_exception=ValueError,
        match=r'DomainEventName value <<<>>> is an empty string. Only non-empty strings are allowed.',
    ):
        DomainEventName(value=invalid_name)
