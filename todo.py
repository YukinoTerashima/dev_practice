import argparse
import json
import os

TODO_FILE = 'todo_list.json'
 
# TODO リストを JSON ファイルから読み込む関数
def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

# TODO リストを JSON ファイルに保存する関数
def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file, indent=4)

# TODO にユニークな ID を割り当てる関数
def generate_id(todos):
    if todos:
        return max(todo['id'] for todo in todos) + 1
    return 1

# TODO を追加する関数
def add_todo(title, description=""):
    todos = load_todos()
    
    for todo in todos:
        if todo['title'] == title:
            todo['description'] = description
            print(f'TODO "{title}" を更新しました。')
            save_todos(todos)
            return

    new_todo = {
        'id': generate_id(todos),
        'title': title,
        'description': description,
        'completed': False
    }
    todos.append(new_todo)
    save_todos(todos)
    print(f'TODO "{title}" を追加しました。')

# TODO を削除する関数
def delete_todo(todo_id):
    todos = load_todos()
    todos = [todo for todo in todos if todo['id'] != todo_id]
    save_todos(todos)
    print(f'TODO ID {todo_id} を削除しました。')

# TODO の完了状態を変更する関数
def complete_todo(todo_id, completed=True):
    todos = load_todos()
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = completed
            save_todos(todos)
            state = "完了" if completed else "未完了"
            print(f'TODO ID {todo_id} を{state}にしました。')
            return
    print(f'TODO ID {todo_id} が見つかりません。')



# TODO リストを表示する関数
def list_todos(show_all=False):
    todos = load_todos()
    for todo in todos:
        if show_all or not todo['completed']:
            status = '完了' if todo['completed'] else '未完了'
            print(f"ID: {todo['id']} | タイトル: {todo['title']} | 状態: {status}")

# 特定の TODO を表示する関数
def show_todo_detail(todo_id):
    todos = load_todos()
    for todo in todos:
        if todo['id'] == todo_id:
            status = '完了' if todo['completed'] else '未完了'
            print(f"ID: {todo['id']}\nタイトル: {todo['title']}\n説明: {todo['description']}\n状態: {status}")
            return
    print(f'TODO ID {todo_id} が見つかりません。')

# コマンドライン引数の処理
def main():
    parser = argparse.ArgumentParser(description="TODO 管理アプリ")
    
    subparsers = parser.add_subparsers(dest='command')

    # add コマンド
    parser_add = subparsers.add_parser('add', help="TODO を追加します")
py    parser_add.add_argument('title', help="TODO のタイトル")
    parser_add.add_argument('--description', help="TODO の詳しい説明", default="")

    # list コマンド
    parser_list = subparsers.add_parser('list', help="TODO を一覧表示します")
    parser_list.add_argument('--all', action='store_true', help="完了済みの TODO も表示します")

    # delete コマンド
    parser_delete = subparsers.add_parser('delete', help="TODO を削除します")
    parser_delete.add_argument('id', type=int, help="削除する TODO の ID")

    # complete コマンド
    parser_complete = subparsers.add_parser('complete', help="TODO を完了状態にします")
    parser_complete.add_argument('id', type=int, help="完了状態にする TODO の ID")

    # incomplete コマンド
    parser_incomplete = subparsers.add_parser('incomplete', help="TODO を未完了状態にします")
    parser_incomplete.add_argument('id', type=int, help="未完了状態にする TODO の ID")

    # show コマンド
    parser_show = subparsers.add_parser('show', help="特定の TODO の詳細を表示します")
    parser_show.add_argument('id', type=int, help="詳細を表示する TODO の ID")

    # 引数の解析
    args = parser.parse_args()

    if args.command == 'add':
        add_todo(args.title, args.description)
    elif args.command == 'list':
        list_todos(args.all)
    elif args.command == 'delete':
        delete_todo(args.id)
    elif args.command == 'complete':
        complete_todo(args.id, True)
    elif args.command == 'incomplete':
        complete_todo(args.id, False)
    elif args.command == 'show':
        show_todo_detail(args.id)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
