import unittest
from todo import load_save_type
from todo import connect_sqlite
from todo import load_todos_sqlite
from todo import load_todos
from todo import delete_todo_sqlite
from todo import complete_todo_sqlite
from todo import list_todos_sqlite
from todo import show_todo_detail_sqlite
from todo import add_todo_sqlite

class TestFunction(unittest.TestCase):

    # def test_load_json(self):
    #     self.assertEqual(load_save_type(), 'json')

    # def test_connect_sqlite(self):
    #     connect_sqlite()        

    # def test_load_todos_sqlite(self):
    #     cur = connect_sqlite() 
    #     res = load_todos_sqlite(cur)
    #     print(res)

    # def test_load_todos(self):
    #     print(load_todos()[0])

    # def test_delete_todo_sqlite(self):
    #     conn, cur = connect_sqlite() 
    #     delete_todo_sqlite(conn, cur, 1)

    # def test_complete_todo_sqlite(self):
    #     conn, cur = connect_sqlite()
    #     complete_todo_sqlite(conn, cur, 1, 1)

    # def test_list_todo_sqlite(self):
    #     conn, cur = connect_sqlite()
    #     list_todos_sqlite(cur, False)

    # def test_show_todo_detail_sqlite(self):
    #     conn, cur = connect_sqlite()
    #     show_todo_detail_sqlite(cur, 2)

    def test_add_todo_sqlite(self):
        conn, cur = connect_sqlite()
        add_todo_sqlite(cur, conn, 'testTitle', 'description123')

if __name__ == '__main__':
    unittest.main()