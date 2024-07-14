from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetRequest(_message.Message):
    __slots__ = ("filter", "keyword", "limit", "page")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    filter: str
    keyword: str
    limit: int
    page: int
    def __init__(self, filter: _Optional[str] = ..., keyword: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("status", "data", "metadata")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    status: str
    data: _containers.RepeatedCompositeFieldContainer[DataResponse]
    metadata: MetaDataResponse
    def __init__(self, status: _Optional[str] = ..., data: _Optional[_Iterable[_Union[DataResponse, _Mapping]]] = ..., metadata: _Optional[_Union[MetaDataResponse, _Mapping]] = ...) -> None: ...

class DataResponse(_message.Message):
    __slots__ = ("id", "name", "execute_date", "duration", "test_status", "efectiveness", "executor", "DataTag")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_DATE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    TEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    EFECTIVENESS_FIELD_NUMBER: _ClassVar[int]
    EXECUTOR_FIELD_NUMBER: _ClassVar[int]
    DATATAG_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    execute_date: str
    duration: float
    test_status: str
    efectiveness: float
    executor: str
    DataTag: _containers.RepeatedCompositeFieldContainer[DataDetail]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., execute_date: _Optional[str] = ..., duration: _Optional[float] = ..., test_status: _Optional[str] = ..., efectiveness: _Optional[float] = ..., executor: _Optional[str] = ..., DataTag: _Optional[_Iterable[_Union[DataDetail, _Mapping]]] = ...) -> None: ...

class DataDetail(_message.Message):
    __slots__ = ("name", "color")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    color: str
    def __init__(self, name: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class MetaDataResponse(_message.Message):
    __slots__ = ("current_page", "per_page", "total", "last_page")
    CURRENT_PAGE_FIELD_NUMBER: _ClassVar[int]
    PER_PAGE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
    current_page: int
    per_page: int
    total: int
    last_page: int
    def __init__(self, current_page: _Optional[int] = ..., per_page: _Optional[int] = ..., total: _Optional[int] = ..., last_page: _Optional[int] = ...) -> None: ...

class DetailRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class DetailResponse(_message.Message):
    __slots__ = ("status", "DataById")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATABYID_FIELD_NUMBER: _ClassVar[int]
    status: str
    DataById: _containers.RepeatedCompositeFieldContainer[ResultDetail]
    def __init__(self, status: _Optional[str] = ..., DataById: _Optional[_Iterable[_Union[ResultDetail, _Mapping]]] = ...) -> None: ...

class ResultDetail(_message.Message):
    __slots__ = ("id", "name", "test_count", "duration", "test_status", "efectiveness", "executor", "DataTag", "fail_message")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEST_COUNT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    TEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    EFECTIVENESS_FIELD_NUMBER: _ClassVar[int]
    EXECUTOR_FIELD_NUMBER: _ClassVar[int]
    DATATAG_FIELD_NUMBER: _ClassVar[int]
    FAIL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    test_count: int
    duration: float
    test_status: str
    efectiveness: float
    executor: str
    DataTag: _containers.RepeatedCompositeFieldContainer[DataDetail]
    fail_message: _containers.RepeatedCompositeFieldContainer[DetailMessage]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., test_count: _Optional[int] = ..., duration: _Optional[float] = ..., test_status: _Optional[str] = ..., efectiveness: _Optional[float] = ..., executor: _Optional[str] = ..., DataTag: _Optional[_Iterable[_Union[DataDetail, _Mapping]]] = ..., fail_message: _Optional[_Iterable[_Union[DetailMessage, _Mapping]]] = ...) -> None: ...

class DetailMessage(_message.Message):
    __slots__ = ("type", "method", "message")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    type: str
    method: str
    message: str
    def __init__(self, type: _Optional[str] = ..., method: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

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
