import grpc

import todo_pb2
import todo_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = todo_pb2_grpc.TodoServiceStub(channel)
    response = stub.CreateTodo(todo_pb2.Todo(id=1, details='first todo', status=1))
    print(response)
    response = stub.GetTodo(todo_pb2.Todo(id=1))
    print(response)
    response = stub.CreateTodo(todo_pb2.Todo(id=2, details='second todo', status=1))
    print(response)
    response = stub.GetTodo(todo_pb2.Todo(id=2, details='second todo', status=1))
    print(response)
    response = stub.GetAllTodos(todo_pb2.GetTodoList())
    print(response)
    response = stub.DeleteTodo(todo_pb2.Todo(id=1, details='first todo', status=1))
    print(response)
    response = stub.GetAllTodos(todo_pb2.GetTodoList())
    print(response)


if __name__ == '__main__':
    run()
