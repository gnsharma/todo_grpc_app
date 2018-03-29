from concurrent import futures
import time
import grpc

import todo_pb2
import todo_pb2_grpc
from todo_pb2 import User as User_pb2, TodoList
from database.models import session, User, Todo

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class TodoServicer(todo_pb2_grpc.TodoServiceServicer):

    def CreateUser(self, request, context):
        user = User(name=request.name, email=request.email)

        try:
            session.add(user)
            session.commit()
            request.id = user.id
            action_status = todo_pb2.ActionStatus(status=1)
        except:
            print("Not able to create User")
            session.rollback()
            action_status = todo_pb2.ActionStatus(status=2)
        finally:
            return todo_pb2.CreateUserResponse(status=action_status, user=request)

    def GetUser(self, request, context):
        user = session.query(User).filter(User.id == request.id).first()
        user_pb2 = User_pb2()

        if user:
            user_pb2.id = user.id
            user_pb2.name = user.name
            user_pb2.email = user.email

        return user_pb2

    def CreateTodo(self, request, context):
        todo = Todo(details=request.details, user_id=request.user_id, status=request.status)

        try:
            session.add(todo)
            session.commit()
            request.id = todo.id
            action_status = todo_pb2.ActionStatus(status=1)
        except:
            print("Not able to create Todo")
            session.rollback()
            action_status = todo_pb2.ActionStatus(status=2)
        finally:
            return todo_pb2.CreateTodoResponse(status=action_status, todo=request)

    def GetTodo(self, request, context):
        todo = session.query(Todo).filter(Todo.id == request.id).first()
        todo_pb = todo_pb2.Todo()

        if todo:
            todo_pb.id = todo.id
            todo_pb.user_id = todo.user_id
            todo_pb.details = todo.details
            todo_pb.status = todo.status

        return todo_pb

    def GetUserTodos(self, request, context):
        user = session.query(User).filter(User.id == request.id).first()

        if user:
            todoList = session.query(Todo).filter(Todo.user_id == user.id)
            todoList_pb2 = []
            for todo in todoList:
                todoList_pb2.append(todo_pb2.Todo(id=todo.id, user_id=todo.user_id, details=todo.details, status=todo.status))
            return TodoList(todos=todoList_pb2)
        else:
            return TodoList()

    def DeleteTodo(self, request, context):
        todo = session.query(Todo).filter(Todo.id == request.id).first()

        if todo:
            session.delete(todo)
            success_status = todo_pb2.ActionStatus(status=1)
            return todo_pb2.DeleteResponse(status=success_status)
        else:
            failed_status = todo_pb2.ActionStatus(status=2)
            return todo_pb2.DeleteResponse(status=failed_status)

    def DeleteUser(self, request, context):
        user = session.query(User).filter(User.id == request.id).first()

        if user:
            todoList = session.query(Todo).filter(Todo.user_id == user.id)
            for todo in todoList:
                session.delete(todo)
            session.delete(user)
            success_status = todo_pb2.ActionStatus(status=1)
            return todo_pb2.DeleteResponse(status=success_status)
        else:
            failed_status = todo_pb2.ActionStatus(status=2)
            return todo_pb2.DeleteResponse(status=failed_status)


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
