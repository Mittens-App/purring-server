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
