# Whereby API Client for Python

This is a tiny wrapper around [Whereby](https://whereby.com/)'s [HTTP API](https://whereby.dev/http-api/).

[![PyPI version](https://badge.fury.io/py/whereby-api.svg)](https://badge.fury.io/py/whereby-api)

## Installation

```shell
$ pip install whereby_api
```

## API reference

### `class whereby_api.WherebyClient(api_key)`
#### Parameters
- **`api_key`** – the API key you received from Whereby (_string_)
#### Usage
```python
from whereby_api import WherebyClient
whereby = WherebyClient(api_key='<your api key>')
```
#### Methods
- ### `create_meeting(start_date, end_date, is_locked=False, room_name_prefix=None, room_mode='normal', fields=[])`
  Create a new meeting
  #### Parameters
  - **`start_date`** – When the meeting starts (_required, either a `datetime` object or an [ISO 8601] string_)
  - **`end_date`** – When the meeting ends (_required, either a `datetime` object or an [ISO 8601] string_)
  - **`is_locked`** – The initial lock state of the room (_boolean_)
  - **`room_name_prefix`** – The prefix for the room name. (_string_)
  - **`room_mode`** – The mode of the created room. (_string – `normal` or `group`_)
  - **`fields`** – Additional fields that should be populated. (_list of strings, currently the only option is `hostRoomUrl`_)

  Please refer to the [official documentation](https://whereby.dev/http-api/#/paths/~1meetings/post) for details.

  #### Return type
  [`whereby_api.Meeting`](#class-whereby_apimeetingmeeting_id-room_url-start_date-end_date-host_room_url) instance

  #### Usage
  ```python
  from datetime import datetime, timedelta
  whereby.create_meeting(
    start_date=datetime.now(),
    end_date=datetime.now() + timedelta(days=2),
  )
  ```

- ### `delete_meeting(meeting_id)`
  Delete an existing meeting
  #### Parameters
  - **`meeting_id`** – the ID of the meeting (_required, string_)

  Please refer to the [official documentation](https://whereby.dev/http-api/#/paths/~1meetings~1{meetingId}/delete) for details.

  #### Usage
  ```python
  whereby.delete_meeting(meeting_id='123456')
  ```

- ### `get_meeting(meeting_id)`
  Get details about an existing meeting
  #### Parameters
  - **`meeting_id`** – the ID of the meeting (_required, string_)

  Please refer to the [official documentation](https://whereby.dev/http-api/#/paths/~1meetings~1{meetingId}/delete) for details.

  #### Return type
  [`whereby_api.Meeting`](#class-whereby_apimeetingmeeting_id-room_url-start_date-end_date-host_room_url) instance

  #### Usage
  ```python
  meeting = whereby.get_meeting(meeting_id='123456')
  ```

---

### `class whereby_api.Meeting(meeting_id, room_url, start_date, end_date, host_room_url)`
Represents a meeting

#### Properties
- **`meeting_id`** – The ID of the meeting. (_string_)
- **`room_url`** – The URL to room where the meeting will be hosted. (_string_)
- **`start_date`** – When the meeting starts. (_datetime_)
- **`end_date`** – When the meeting ends. (_datetime_)
- **`host_room_url`** – The URL to room where the meeting will be hosted which will also make the user the host of the meeting. (_string_)

Please refer to the [official documentation](https://whereby.dev/http-api/) for details.


[ISO 8601]: https://www.w3.org/TR/NOTE-datetime
