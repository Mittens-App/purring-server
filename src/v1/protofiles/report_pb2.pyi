from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReportRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("total_testcases", "total_tags")
    TOTAL_TESTCASES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TAGS_FIELD_NUMBER: _ClassVar[int]
    total_testcases: str
    total_tags: str
    def __init__(self, total_testcases: _Optional[str] = ..., total_tags: _Optional[str] = ...) -> None: ...
