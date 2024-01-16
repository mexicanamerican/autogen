import os

import pytest


def test_gpt_assistant():
    try:
        with open("notebook/OAI_CONFIG_LIST") as file:
            config_list = file.read()
    except FileNotFoundError:
        pytest.fail("Missing OAI_CONFIG_LIST file")

    # Rest of the test logic
    # ...
