import pytest
from labtwo import main, DB, Clients
from random import randint
import os.path

def test_without_argv():
    with pytest.raises(SystemExit) as excinfo:
        main(["labone.py"])
    assert excinfo.value.code == 1

def test_init():
    main(["labone.py", "init"])
    if not os.path.exists("labone.sqlite"):
        raise Exception("Файл не создался")
    DB.connect(True)
    tables = DB.get_tables()
    assert "clients" in tables
    assert "orders" in tables
    if not DB.is_closed():
        DB.close()

def test_fill():
    amount = randint(10, 50)
    for i in range(amount):
        main(["labone.py", "fill"])
    DB.connect(True)
    assert Clients.select().count() == (amount * 10)
    if not DB.is_closed():
        DB.close()

def test_show_without_table():
    with pytest.raises(SystemExit) as excinfo:
        main(["labone.py", "show"])
    assert excinfo.value.code == 1

def test_show():
    main(["labone.py", "show", "orders"])
