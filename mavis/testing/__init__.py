from .fixtures import *
from .steps import *


def pytest_generate_tests(metafunc):
    devices = [metafunc.config.option.device]
    metafunc.parametrize("device", devices, scope="session")
