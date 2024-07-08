from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReportRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("total_testcases", "total_tags", "total_efectiveness", "ResultData", "TagData", "current_month_string", "current_month", "current_year", "status")
    TOTAL_TESTCASES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TAGS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EFECTIVENESS_FIELD_NUMBER: _ClassVar[int]
    RESULTDATA_FIELD_NUMBER: _ClassVar[int]
    TAGDATA_FIELD_NUMBER: _ClassVar[int]
    CURRENT_MONTH_STRING_FIELD_NUMBER: _ClassVar[int]
    CURRENT_MONTH_FIELD_NUMBER: _ClassVar[int]
    CURRENT_YEAR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    total_testcases: int
    total_tags: int
    total_efectiveness: float
    ResultData: _containers.RepeatedCompositeFieldContainer[DataResponse]
    TagData: _containers.RepeatedCompositeFieldContainer[TagDataResponse]
    current_month_string: str
    current_month: int
    current_year: int
    status: str
    def __init__(self, total_testcases: _Optional[int] = ..., total_tags: _Optional[int] = ..., total_efectiveness: _Optional[float] = ..., ResultData: _Optional[_Iterable[_Union[DataResponse, _Mapping]]] = ..., TagData: _Optional[_Iterable[_Union[TagDataResponse, _Mapping]]] = ..., current_month_string: _Optional[str] = ..., current_month: _Optional[int] = ..., current_year: _Optional[int] = ..., status: _Optional[str] = ...) -> None: ...

class DataResponse(_message.Message):
    __slots__ = ("id", "date", "name", "status", "executor")
    ID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXECUTOR_FIELD_NUMBER: _ClassVar[int]
    id: int
    date: str
    name: str
    status: str
    executor: str
    def __init__(self, id: _Optional[int] = ..., date: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[str] = ..., executor: _Optional[str] = ...) -> None: ...

class TagDataResponse(_message.Message):
    __slots__ = ("id", "name", "total", "efectiveness")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    EFECTIVENESS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    total: int
    efectiveness: float
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., total: _Optional[int] = ..., efectiveness: _Optional[float] = ...) -> None: ...
