import grpc
import random

import todo_pb2
import todo_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = todo_pb2_grpc.TodoServiceStub(channel)
    user_id = random.randint(100, 1000)
    response = stub.CreateUser(todo_pb2.User(id=user_id, name='first user', email='fu@user.com'))
    print("create user\n", response)
    response = stub.GetUser(todo_pb2.User(id=user_id))
    print("get user\n", response)

    todo_id = random.randint(100, 1000)
    response = stub.CreateTodo(todo_pb2.Todo(id=todo_id, user_id=user_id, details='first todo', status=1))
    print("create todo\n", response)
    response = stub.GetTodo(todo_pb2.Todo(id=todo_id))
    print("get todo\n", response)

    response = stub.GetUserTodos(todo_pb2.User(id=user_id))
    print("get user todos\n", response)

    todo_id = random.randint(100, 1000)
    response = stub.CreateTodo(todo_pb2.Todo(id=todo_id, user_id=user_id, details='second todo', status=1))
    print("create second todo\n", response)
    response = stub.GetTodo(todo_pb2.Todo(id=todo_id))
    print("get second todo\n", response)

    response = stub.GetUserTodos(todo_pb2.User(id=user_id))
    print("get user todos\n", response)

    response = stub.DeleteTodo(todo_pb2.Todo(id=todo_id, user_id=user_id))
    print("delete second todo\n", response)

    response = stub.GetTodo(todo_pb2.Todo(id=todo_id, user_id=user_id))
    print("get second todo\n", response)

    response = stub.GetUserTodos(todo_pb2.User(id=user_id))
    print("get user todos\n", response)

    response = stub.DeleteUser(todo_pb2.User(id=user_id))
    print("delete user\n", response)
    response = stub.GetUser(todo_pb2.User(id=user_id))
    print("get user\n", response)


if __name__ == '__main__':
    run()
