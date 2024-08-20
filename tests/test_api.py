import os
from unittest.mock import patch, mock_open, call
import pytest
from app.api import is_valid, export, write_csv


@pytest.fixture
def min_user():
    """Represents a valid user with minimal data."""
    return {
        'email': 'minimal@example.com',
        'name': 'Primus Minimus',
        'age': 18,
    }


@pytest.fixture
def full_user():
    """Represents a valid user with full dat."""
    return {
        'email': 'full@example.com',
        'name': 'Maximus Plenus',
        'age': 65,
        'role': 'emperor',
    }


def users(min_user, full_user):
    """List of users, two valid and one invalid"""
    bad_user = {
        'email': 'invalid@example.com',
        'name': 'Horribilis',

    }

    return [min_user, bad_user, full_user]


class TestIsValid:
    """Test how code verifies whether a user is valid or not."""
    def test_minimal(self, min_user):
        assert is_valid(min_user)

    def test_full(self, full_user):
        assert is_valid(full_user)

    @pytest.mark.parametrize('age', range(18))
    def test_invalid_age_too_young(self, age, min_user):
        min_user['age'] = age
        assert not is_valid(min_user)


    @pytest.mark.parametrize('age', range(66, 100))
    def test_invalid_age_too_old(self, age, min_user):
        min_user['age'] = age
        assert not is_valid(min_user)


    @pytest.mark.parametrize('age', ['NaN', 3.1415, None])
    def test_invalid_age_wrong_type(self, age, min_user):
        min_user['age'] = age
        assert not is_valid(min_user)


    @pytest.mark.parametrize('age', range(18, 66))
    def test_valid_age(self, age, min_user):
        min_user['age'] = age
        assert is_valid(min_user)
    


    
