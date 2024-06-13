#!/user/bin/python3

import json
import unittest
from mon_module_a_tester import user


def test_user_json():
    with open("user.json", "r") as user_file:
        user_data = json.load(user_file)

    expected_data = {
        "id": 1,
        "name": "Jordy",
        "email": "jordymoukiana@gmail.com"
    }

    assert user_data == expected_data, f"User data mismatch: {user_data} != {expected_data}"
