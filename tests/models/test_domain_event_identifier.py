"""
Test domain event identifier value object.
"""

from uuid import UUID

from object_mother_pattern import StringMother
from object_mother_pattern.mothers.identifiers import StringUuidV4Mother
from pytest import mark, raises as assert_raises

from domain_event_pattern.models.domain_event_identifier import DomainEventIdentifier
from domain_event_pattern.models.testing.mothers import DomainEventIdentifierMother


@mark.unit_testing
def test_domain_event_identifier_creation() -> None:
    """
    Test domain event identifier creation with valid value.
    """
    domain_event_identifier = DomainEventIdentifierMother.create()

    assert type(domain_event_identifier.value) is str
    assert UUID(domain_event_identifier.value).version == 4


@mark.unit_testing
def test_domain_event_identifier_creation_value() -> None:
    """
    Test domain event identifier creation with valid value.
    """
    domain_event_identifier_value = DomainEventIdentifierMother.create().value
    domain_event_identifier = DomainEventIdentifier(value=domain_event_identifier_value)

    assert domain_event_identifier == domain_event_identifier


@mark.unit_testing
def test_domain_event_identifier_invalid_type() -> None:
    """
    Test domain event identifier creation with invalid type.
    """
    invalid_identifier = StringUuidV4Mother.invalid_type()

    with assert_raises(
        expected_exception=TypeError,
        match=r'DomainEventIdentifier value <<<.*>>> must be a string. Got <<<.*>>> type.',
    ):
        DomainEventIdentifier(value=invalid_identifier)


@mark.unit_testing
def test_domain_event_identifier_empty_value() -> None:
    """
    Test domain event identifier creation with empty value.
    """
    invalid_identifier = StringMother.empty()

    with assert_raises(
        expected_exception=ValueError,
        match=r'DomainEventIdentifier value <<<>>> is an empty string. Only non-empty strings are allowed.',
    ):
        DomainEventIdentifier(value=invalid_identifier)


@mark.unit_testing
def test_domain_event_identifier_not_trimmed() -> None:
    """
    Test domain event identifier creation with not trimmed value.
    """
    invalid_identifier = StringMother.not_trimmed()

    with assert_raises(
        expected_exception=ValueError,
        match=r'DomainEventIdentifier value <<<.*>>> contains leading or trailing whitespaces. Only trimmed values are allowed.',  # noqa: E501
    ):
        DomainEventIdentifier(value=invalid_identifier)


@mark.unit_testing
def test_domain_event_identifier_invalid_value() -> None:
    """
    Test domain event identifier creation with invalid UUID value.
    """
    invalid_identifier = StringUuidV4Mother.invalid_value()

    with assert_raises(
        expected_exception=ValueError,
        match=r'DomainEventIdentifier value <<<.*>>> is not a valid UUID.',
    ):
        DomainEventIdentifier(value=invalid_identifier)
