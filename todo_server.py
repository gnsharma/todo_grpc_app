from concurrent import futures
import time

import grpc

import todo_pb2
import todo_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

DATA_DICT = {}


class TodoServicer(todo_pb2_grpc.TodoServiceServicer):

    def CreateTodo(self, request, context):
        todo = todo_pb2.Todo()
        todo.id = request.id
        todo.details = request.details
        todo.status = request.status

        DATA_DICT[request.id] = todo
        action_status = todo_pb2.ActionStatus(status=1)

        return todo_pb2.CreateTodoResponse(status=action_status)

    def GetTodo(self, request, context):
        todo = DATA_DICT.get(request.id, None)

        if todo is not None:
            return todo
        else:
            return todo_pb2.Todo()

    def GetAllTodos(self, request, context):
        return todo_pb2.TodoList(todos=DATA_DICT.values())

    def DeleteTodo(self, request, context):
        todo = DATA_DICT.pop(request.id, None)

        success_status = todo_pb2.ActionStatus(status=1)
        failed_status = todo_pb2.ActionStatus(status=2)

        if todo is not None:
            return todo_pb2.DeleteTodoResponse(status=success_status)
        else:
            return todo_pb2.DeleteTodoResponse(status=failed_status)


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoServicer(), server)
    print("Starting server. Listening on port 50051.")
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
