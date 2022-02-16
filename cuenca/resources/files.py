from io import BytesIO
from typing import ClassVar, cast

from cuenca_validations.types import (
    FileFormat,
    FileQuery,
    FileRequest,
    KYCFileType,
)
from pydantic import HttpUrl
from pydantic.dataclasses import dataclass

from ..http import Session, session as global_session
from .base import Downloadable, Queryable, Uploadable


@dataclass
class File(Downloadable, Queryable, Uploadable):
    _resource: ClassVar = 'files'
    _query_params: ClassVar = FileQuery

    extension: str
    type: KYCFileType
    url: HttpUrl
    user_id: str

    @classmethod
    def upload(
        cls,
        file: BytesIO,
        user_id: str = 'me',
        *,
        session: Session = global_session,
    ) -> 'File':
        """
        Stores an encrypted version of the file,
        only users with permissions can access it.

        :param file:
        :param user_id:
        :param session:
        :return: New encrypted file object
        """
        req = FileRequest(file=file.read())
        return cast(
            'File', cls._upload(id=user_id, session=session, **req.dict())
        )

    @property
    def file(self) -> bytes:
        """
        Bytes of the decrypted file.
        Format of the file is found on `file_type` property.
        """
        return self.download(self, file_format=FileFormat.any).read()

    @property
    def pdf(self) -> bytes:
        """
        Override from `Downloadable`, this property does not apply.
        """
        raise NotImplementedError

    @property
    def xml(self) -> bytes:
        """
        Override from `Downloadable`, this property does not apply.
        """
        raise NotImplementedError