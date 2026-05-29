from __future__ import annotations

from typer.testing import CliRunner

from diracx.cli import app

runner = CliRunner()


def test_show_joke():
    result = runner.invoke(app, ["config", "show-joke"], input="\n")
    assert result.exit_code == 0, result.output
    assert "Why did the 🐣 cross the road?" in result.stdout
    assert "To get to the other side" in result.stdout
