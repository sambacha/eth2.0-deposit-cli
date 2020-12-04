import pytest

from eth2deposit.credentials import (
  validate_withdrawal_credentials,
  validate_withdrawal_pk
)
from eth2deposit.exceptions import ValidationError

@pytest.mark.parametrize(
    'withdrawal_credentials, is_valid',
    [
        ('0x2222', False),
        ('40517ce98f810', False),
        ('0x00040517ce98f81070cea20e35610a3ae23a45f0883b0b035afc5717cc2e833e', False),
        ('ab040517ce98f81070cea20e35610a3ae23a45f0883b0b035afc5717cc2e833e', False),
        ('00040517ce98f81070cea20e35610a3ae23a45f0883b0b035afc5717cc2e833e', True),
        ('00040517ce98f81070cea20e35610a3ae23a45f0883b0b035afc5717cc2e833e123', False),
    ]
)
def test_validate_withdrawal_credentials(withdrawal_credentials, is_valid) -> None:
    if is_valid:
        validate_withdrawal_credentials(withdrawal_credentials)
    else:
        with pytest.raises((ValidationError, ValueError)):
            validate_withdrawal_credentials(withdrawal_credentials)

@pytest.mark.parametrize(
    'withdrawal_pk, is_valid',
    [
        ('0x2222', False),
        ('8f2e1407c5f712c3f2885670204a9b5a42a6629da1e76cfb3e0ec', False),
        ('0x8f2e1407c5f712c3f2885670204a9b5a42a6629da1e76cfb3e0ecf34b03fb1bc7f0ed3fe453266dba6a91ed39989cf2e', False),
        ('8f2e1407c5f712c3f2885670204a9b5a42a6629da1e76cfb3e0ecf34b03fb1bc7f0ed3fe453266dba6a91ed39989cf2e', True),
        ('8f2e1407c5f712c3f2885670204a9b5a42a6629da1e76cfb3e0ecf34b03fb1bc7f0ed3fe453266dba6a91ed39989cf2e11aa', False),
        ('jy4UB8X3EsPyiFZwIEqbWkKmYp2h52z7Pg7PNLA/sbx/DtP+RTJm26apHtOZic8u', False),
    ]
)
def test_validate_withdrawal_pk(withdrawal_pk, is_valid) -> None:
    if is_valid:
        validate_withdrawal_pk(withdrawal_pk)
    else:
        with pytest.raises((ValidationError, ValueError)):
            validate_withdrawal_pk(withdrawal_pk)            