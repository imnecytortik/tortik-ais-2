import pytest
from labtwo import main, DB, Clients
from random import randint
import os.path

def test_without_argv():
    with pytest.raises(SystemExit) as excinfo:
        main(["labtwo.py"])
    assert excinfo.value.code == 1

def test_init():
    main(["labtwo.py", "init"])
    if not os.path.exists("labtwo.sqlite"):
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
        main(["labtwo.py", "fill"])
    DB.connect(True)
    assert Clients.select().count() == (amount * 10)
    if not DB.is_closed():
        DB.close()

def test_show_without_table():
    with pytest.raises(SystemExit) as excinfo:
        main(["labtwo.py", "show"])
    assert excinfo.value.code == 1
    

def test_show():
    main(["labtwo.py", "show", "orders"])
