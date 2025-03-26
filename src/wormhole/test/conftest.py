from twisted.internet.defer import ensureDeferred

import pytest
import pytest_twisted


@pytest.fixture(scope="session")
def reactor():
    from twisted.internet import reactor
    yield reactor

from .common import setup_mailbox, setup_transit_relay


@pytest.fixture(scope="session")
def mailbox(reactor):
    mb = pytest_twisted.blockon(ensureDeferred(setup_mailbox(reactor)))
    mb.service.startService()
    yield mb
    pytest_twisted.blockon(mb.service.stopService())


@pytest.fixture(scope="session")
def transit_relay(reactor):
    url, service = setup_transit_relay(reactor)
    service.startService()
    yield url
    pytest_twisted.blockon(service.stopService())
