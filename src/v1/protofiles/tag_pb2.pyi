from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("name", "desc", "color")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    desc: str
    color: str
    def __init__(self, name: _Optional[str] = ..., desc: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: str
    message: str
    def __init__(self, status: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("keyword",)
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    keyword: str
    def __init__(self, keyword: _Optional[str] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("status", "data")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: str
    data: _containers.RepeatedCompositeFieldContainer[DataResponse]
    def __init__(self, status: _Optional[str] = ..., data: _Optional[_Iterable[_Union[DataResponse, _Mapping]]] = ...) -> None: ...

class DataResponse(_message.Message):
    __slots__ = ("id", "name", "desc", "color")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    desc: str
    color: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., desc: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: str
    message: str
    def __init__(self, status: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "name", "desc", "color")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    desc: str
    color: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., desc: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: str
    message: str
    def __init__(self, status: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class DeleteAllRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAllResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: str
    message: str
    def __init__(self, status: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
