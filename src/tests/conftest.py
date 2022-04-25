import pytest
import os
from src.tests.env_test import *

@pytest.fixture(scope="session", autouse=True)
def setup_env_var():
    old_environ = dict(os.environ)
    os.environ.update(ENV_VARS)

    yield
    os.environ.clear()
    os.environ.update(old_environ)