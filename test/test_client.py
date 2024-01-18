# test/test_client.py

import openai
import pytest


@pytest.mark.skipif(not openai.is_installed(), reason="openai package is not installed")
def test_openai_dependency():
    # Test code that requires openai package
    pass

def test_other_functionality():
    # Test code that does not require openai package
    pass
