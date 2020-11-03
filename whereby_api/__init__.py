from dataclasses import dataclass, field
from datetime import datetime
import dateutil.parser
from functools import partialmethod

import requests
from requests.exceptions import HTTPError


@dataclass(frozen=True)
class Meeting:
    meeting_id: str
    room_url: str
    start_date: datetime = field(repr=False)
    end_date: datetime = field(repr=False)
    host_room_url: str = field(repr=False)


class WherebyClient:
    api_base_url = 'https://api.whereby.dev/v1'

    def __init__(self, api_key):
        self.api_key = api_key
        self.session = self._create_session()

    # HTTP requests
    def _create_session(self):
        session = requests.Session()
        session.headers.update({'Authorization': f'Bearer {self.api_key}'})
        return session

    def _make_request(self, method, path, *args, **kwargs):
        resp = getattr(self.session, method)(
            f'{self.api_base_url}{path}', *args, **kwargs
        )
        resp.raise_for_status()
        return resp

    _get = partialmethod(_make_request, 'get')
    _post = partialmethod(_make_request, 'post')
    _delete = partialmethod(_make_request, 'delete')

    # Helpers

    def _build_meeting_from_api_response(self, meeting):
        return Meeting(
            meeting_id=meeting['meetingId'],
            room_url=meeting['roomUrl'],
            start_date=dateutil.parser.parse(meeting['startDate']),
            end_date=dateutil.parser.parse(meeting['endDate']),
            host_room_url=meeting.get('hostRoomUrl'),
        )

    def _force_datetime_str(self, dt):
        if isinstance(dt, datetime):
            return dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        return dt

    # API methods

    # Create meeting
    # https://whereby.dev/http-api/#/paths/~1meetings/post
    def create_meeting(
        self,
        start_date,
        end_date,
        is_locked=False,
        room_name_prefix=None,
        room_mode='normal',
        fields=[],
    ):
        data = {
            'startDate': self._force_datetime_str(start_date),
            'endDate': self._force_datetime_str(end_date),
            'isLocked': is_locked,
            'roomNamePrefix': room_name_prefix,
            'roomMode': room_mode,
            'fields': fields,
        }
        r = self._post('/meetings', json=data)
        return self._build_meeting_from_api_response(r.json())

    # Delete meeting
    # https://whereby.dev/http-api/#/paths/~1meetings~1{meetingId}/delete
    def delete_meeting(self, meeting_id):
        r = self._delete(f'/meetings/{meeting_id}')

    # Get meeting
    # https://whereby.dev/http-api/#/paths/~1meetings~1{meetingId}/get
    def get_meeting(self, meeting_id):
        r = self._get(f'/meetings/{meeting_id}')
        return self._build_meeting_from_api_response(r.json())
