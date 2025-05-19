import allure
import pytest


@pytest.fixture(autouse=True)
def allure_device(device: str):
    # Allure doesn't support environments with spaces.
    device_name = device.lower().replace(" ", "_")

    yield

    allure.dynamic.label("device", device_name)


def pytest_generate_tests(metafunc):
    devices = [metafunc.config.option.device]
    metafunc.parametrize("device", devices, scope="session")
