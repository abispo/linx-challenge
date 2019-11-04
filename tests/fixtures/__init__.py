from asynctest import CoroutineMock

import json
import os


def getcity_content() -> CoroutineMock:
    current_dir = os.path.dirname(__file__)
    with open(os.path.join(current_dir, "london.json"), "r") as f:
        data = json.load(f)

        return CoroutineMock(side_effect=[data])
