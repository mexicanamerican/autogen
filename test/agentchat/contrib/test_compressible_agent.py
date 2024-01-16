import os

import pytest


def test_compressible_agent():
    try:
        # Read the OAI_CONFIG_LIST file
        with open("notebook/OAI_CONFIG_LIST") as file:
            config_list = file.read()
    except FileNotFoundError:
        # Handle the missing file error
        pytest.fail("Missing OAI_CONFIG_LIST file")

    # Rest of the test logic
    # ...
