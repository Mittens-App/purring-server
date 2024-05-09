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

class DataResponse(_message.Message):
    __slots__ = ("id", "name", "desc", "tags", "creator", "last_execute_date", "last_execute_result")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    LAST_EXECUTE_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_EXECUTE_RESULT_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    desc: str
    tags: _containers.RepeatedCompositeFieldContainer[Tag]
    creator: str
    last_execute_date: str
    last_execute_result: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., desc: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[Tag, _Mapping]]] = ..., creator: _Optional[str] = ..., last_execute_date: _Optional[str] = ..., last_execute_result: _Optional[str] = ...) -> None: ...

class Tag(_message.Message):
    __slots__ = ("name", "color")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    color: str
    def __init__(self, name: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("name", "desc", "file", "tag_ids")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    TAG_IDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    desc: str
    file: str
    tag_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, name: _Optional[str] = ..., desc: _Optional[str] = ..., file: _Optional[str] = ..., tag_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: str
    message: str
    def __init__(self, status: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class RunRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class RunResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: str
    message: str
    def __init__(self, status: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
