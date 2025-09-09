import json

def save_todos(todos):
    with open("todo.json", "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)  # indent=2는 예쁘게 저장

def load_todos():
    try:
        with open("todo.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # 파일이 없으면 빈 리스트 반환
        return []
    except json.JSONDecodeError:
        # 파일이 비어있거나 손상된 경우
        return []

def add_todo(task):
    for tasks in todos:
        if task == tasks['task']:
            print('이미 존재하는이름의 TODO 입니다.')
            return
    todo = {"task": task, "done": False}
    todos.append(todo)
    save_todos(todos)
    print(f'{task} 추가 완료')

def list_todos():
    print('======== Todo ========')
    for tasks in todos:
        print(f'할일 : {tasks["task"]} -> {"O" if tasks["done"] else "X"}')
    print("======================")

def change_todo(task):
    for tasks in todos:
        if task == tasks['task']:
            tasks['done'] = not tasks['done']
            save_todos(todos)
            print(f'{task} 변경 완료 !')
            print(f'{"O" if not tasks["done"] else "X"} -> {"O" if tasks["done"] else "X"}')
            return
    print(f'입력하신 {task}는 존재하지 않는 TODO 입니다.')

def delete_todo(task):
    for tasks in todos:
        if task == tasks['task']:
            todos.remove(tasks)
            save_todos(todos)
            print(f'{task} 삭제 완료')
            return
    print(f'입력하신 {task}는 존재하지 않는 TODO 입니다.')
def main_ui():
    print('============================================================')
    print('1.ADD_TODO 2.LIST_TODO 3.CHANGE_TODO 4.DELETE_TODO 5.QUIT')
    print('============================================================')

todos = load_todos() or []
while True:
    main_ui()
    choose = input('숫자를 입력하세요 >>> ')
    if choose == '1':
        task = input('추가할 TODO를 입력하세요 >>> ')
        add_todo(task)
    elif choose == '2':
        list_todos()
    elif choose == '3':
        change_todo(input('상태를 변경할 TODO를 입력하세요 >>> '))
    elif choose == '4':
        delete_todo(input('삭제할 TODO를 입력하세요 >>> '))
    elif choose == '5':
        break
    else:
        print('다시 입력해주세요.')

