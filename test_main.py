import sys

sys.path.insert(0, "./mylib")
from read import read  # noqa: E402
from create import create  # noqa: E402
from update import update  # noqa: E402
from delete import delete  # noqa: E402
from delete import create_summary  # noqa: E402

Database_name = "ranking.db"


def test_read(Database_name):
    result = read(Database_name)
    assert result.returncode == 0
    assert "Reading Database..." in result.stdout


def test_create(Database_name):
    result = create(Database_name)
    assert result.returncode == 0
    assert "Creating Databse..." in result.stdout


def test_update(Database_name):
    result = update(Database_name)
    assert result.returncode == 0
    assert "Updating Databse..." in result.stdout


def test_delete(Database_name):
    result = delete(Database_name)
    assert result.returncode == 0
    assert "Deleting Databse..." in result.stdout

create_summary(file_path="./Generated summary report.md")
