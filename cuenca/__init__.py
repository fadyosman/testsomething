__all__ = [
    '__version__',
    'ApiKey',
    'Account',
    'Arpc',
    'BalanceEntry',
    'BillPayment',
    'Card',
    'CardActivation',
    'CardTransaction',
    'CardValidation',
    'CurpValidation',
    'Commission',
    'Deposit',
    'Identity',
    'IdentityEvent',
    'LoginToken',
    'Saving',
    'ServiceProvider',
    'Statement',
    'Transfer',
    'User',
    'UserCredential',
    'UserEvent',
    'UserLogin',
    'WalletTransaction',
    'WhatsappTransfer',
    'configure',
    'get_balance',
]

from typing import cast

from .http import Session, session
from .resources import (
    Account,
    ApiKey,
    Arpc,
    BalanceEntry,
    BillPayment,
    Card,
    CardActivation,
    CardTransaction,
    CardValidation,
    Commission,
    CurpValidation,
    Deposit,
    Identity,
    IdentityEvent,
    LoginToken,
    Saving,
    ServiceProvider,
    Statement,
    Transfer,
    User,
    UserCredential,
    UserEvent,
    UserLogin,
    WalletTransaction,
    WhatsappTransfer,
)
from .version import __version__

configure = session.configure


def get_balance(session: Session = session) -> int:
    balance_entry = cast('BalanceEntry', BalanceEntry.first(session=session))
    return balance_entry.rolling_balance if balance_entry else 0
