from .stream import Stream
from ..exceptions import StreamError
from ..packages.libmms import MMS, MMSError


class MMSStream(Stream):
    """A MMS stream using the requests library.

    *Attributes:*

    - :attr:`url`  The URL to the stream.

    """

    __shortname__ = "mms"

    def __init__(self, session_, url):
        Stream.__init__(self, session_)

        self._url = url

    def __repr__(self):
        return "<MMSStream({0!r})>".format(self.url)

    def __json__(self):
        return dict(type=type(self).shortname(), url=self.url)

    @property
    def url(self):
        return self._url

    def open(self):
        try:
            stream = MMS(self.url)
        except MMSError as e:
            raise StreamError(e)
        return stream
