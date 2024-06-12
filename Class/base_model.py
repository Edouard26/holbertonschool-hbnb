from uuid import uuid4
from datetime import datetime, timezone

class basemodel:
    """
    id : uuid4
    datetime.utc() is deprecated, have to use timezone.utc

    created_at: datetime = datetime.now(timezone)
    updated_at: datetime = datetime.now(timezone)