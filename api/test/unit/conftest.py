from unittest.mock import MagicMock

import pytest


@pytest.fixture(autouse=True)
def capture_exception(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr("sentry_sdk.capture_exception", mock)

    yield mock
