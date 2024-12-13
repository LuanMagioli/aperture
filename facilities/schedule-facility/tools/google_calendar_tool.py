from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime

class GoogleCalendarTool:
    def __init__(self, credentials_file, calendar_id):
        self.credentials_file = credentials_file
        self.calendar_id = calendar_id
        self.service = self.authenticate_google_calendar()

    def authenticate_google_calendar(self):
        credentials = service_account.Credentials.from_service_account_file(
            self.credentials_file,
            scopes=['https://www.googleapis.com/auth/calendar']
        )
        service = build('calendar', 'v3', credentials=credentials)
        return service

    def create_event(self, summary, description, start_time, end_time, timezone='UTC'):
        event = {
            'summary': summary,
            'description': description,
            'start': {
                'dateTime': start_time,
                'timeZone': timezone,
            },
            'end': {
                'dateTime': end_time,
                'timeZone': timezone,
            },
        }
        event = self.service.events().insert(calendarId=self.calendar_id, body=event).execute()
        return event

    def list_events(self, time_min=None, time_max=None, max_results=10):
        events_result = self.service.events().list(
            calendarId=self.calendar_id,
            timeMin=time_min,
            timeMax=time_max,
            maxResults=max_results,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])
        return events

    def delete_event(self, event_id):
        self.service.events().delete(calendarId=self.calendar_id, eventId=event_id).execute()

# Example usage:
# tool = GoogleCalendarTool('path/to/credentials.json', 'your_calendar_id')
# tool.create_event('Meeting', 'Discuss project', '2023-10-10T10:00:00Z', '2023-10-10T11:00:00Z')
# events = tool.list_events()
# for event in events:
#     print(event['summary'])