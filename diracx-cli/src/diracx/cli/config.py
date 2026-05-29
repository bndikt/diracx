# Can't using PEP-604 with typer: https://github.com/tiangolo/typer/issues/348
# from __future__ import annotations
from __future__ import annotations

__all__ = ["dump"]

import base64
import json

from rich import print_json

from diracx.client.aio import AsyncDiracClient
from diracx.core.preferences import OutputFormats, get_diracx_preferences

from .utils import AsyncTyper

app = AsyncTyper()


@app.async_command()
async def dump():
    async with AsyncDiracClient() as api:
        config = await api.config.serve_config()
        display(config)


def display(data):
    output_format = get_diracx_preferences().output_format
    match output_format:
        case OutputFormats.JSON:
            print(json.dumps(data, indent=2))
        case OutputFormats.RICH:
            print_json(data=data)
        case _:
            raise NotImplementedError(output_format)


def reveal_answer(encoded: str) -> str:
    return base64.b64decode(encoded.encode()).decode("utf-8")


@app.async_command()
async def show_joke():
    print("Why did the 🐣 cross the road?")
    input("Press Enter to see the answer...")
    print(reveal_answer("VG8gZ2V0IHRvIHRoZSBvdGhlciBzaWRlISDwn5iK"))
