import sys
import pytest
import main


def test_main_add(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "add", "2", "3"])
    main.main()
    captured = capsys.readouterr()
    assert "5.0" in captured.out


def test_main_subtract(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "subtract", "10", "4"])
    main.main()
    captured = capsys.readouterr()
    assert "6.0" in captured.out


def test_main_divide(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "divide", "10", "2"])
    main.main()
    captured = capsys.readouterr()
    assert "5.0" in captured.out


def test_main_wrong_arg_count(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "add", "2"])
    with pytest.raises(SystemExit) as exc_info:
        main.main()
    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Usage:" in captured.out


def test_main_invalid_operation(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "multiply", "2", "3"])
    with pytest.raises(SystemExit) as exc_info:
        main.main()
    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Unknown operation" in captured.out
