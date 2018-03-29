# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import todo_pb2 as todo__pb2


class TodoServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.CreateTodo = channel.unary_unary(
            '/todo.TodoService/CreateTodo',
            request_serializer=todo__pb2.Todo.SerializeToString,
            response_deserializer=todo__pb2.CreateTodoResponse.FromString,
        )
        self.GetTodo = channel.unary_unary(
            '/todo.TodoService/GetTodo',
            request_serializer=todo__pb2.Todo.SerializeToString,
            response_deserializer=todo__pb2.Todo.FromString,
        )
        self.GetAllTodos = channel.unary_unary(
            '/todo.TodoService/GetAllTodos',
            request_serializer=todo__pb2.GetTodoList.SerializeToString,
            response_deserializer=todo__pb2.TodoList.FromString,
        )
        self.DeleteTodo = channel.unary_unary(
            '/todo.TodoService/DeleteTodo',
            request_serializer=todo__pb2.Todo.SerializeToString,
            response_deserializer=todo__pb2.DeleteTodoResponse.FromString,
        )


class TodoServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def CreateTodo(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTodo(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllTodos(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTodo(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TodoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'CreateTodo': grpc.unary_unary_rpc_method_handler(
            servicer.CreateTodo,
            request_deserializer=todo__pb2.Todo.FromString,
            response_serializer=todo__pb2.CreateTodoResponse.SerializeToString,
        ),
        'GetTodo': grpc.unary_unary_rpc_method_handler(
            servicer.GetTodo,
            request_deserializer=todo__pb2.Todo.FromString,
            response_serializer=todo__pb2.Todo.SerializeToString,
        ),
        'GetAllTodos': grpc.unary_unary_rpc_method_handler(
            servicer.GetAllTodos,
            request_deserializer=todo__pb2.GetTodoList.FromString,
            response_serializer=todo__pb2.TodoList.SerializeToString,
        ),
        'DeleteTodo': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteTodo,
            request_deserializer=todo__pb2.Todo.FromString,
            response_serializer=todo__pb2.DeleteTodoResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'todo.TodoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))