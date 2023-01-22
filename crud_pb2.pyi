from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class createRequest(_message.Message):
    __slots__ = ["config_body", "service_name"]
    CONFIG_BODY_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    config_body: str
    service_name: str
    def __init__(self, service_name: _Optional[str] = ..., config_body: _Optional[str] = ...) -> None: ...

class createResponse(_message.Message):
    __slots__ = ["version"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: str
    def __init__(self, version: _Optional[str] = ...) -> None: ...

class deleteRequest(_message.Message):
    __slots__ = ["service_name", "version"]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    version: str
    def __init__(self, service_name: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class deleteResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...

class getRequest(_message.Message):
    __slots__ = ["service_name", "version"]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    version: str
    def __init__(self, service_name: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class getResponse(_message.Message):
    __slots__ = ["config_body", "result"]
    CONFIG_BODY_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    config_body: str
    result: str
    def __init__(self, config_body: _Optional[str] = ..., result: _Optional[str] = ...) -> None: ...

class updateRequest(_message.Message):
    __slots__ = ["config_body", "service_name", "version"]
    CONFIG_BODY_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    config_body: str
    service_name: str
    version: str
    def __init__(self, service_name: _Optional[str] = ..., version: _Optional[str] = ..., config_body: _Optional[str] = ...) -> None: ...

class updateResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: str
    def __init__(self, result: _Optional[str] = ...) -> None: ...
