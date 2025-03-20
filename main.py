import os
import datetime
import google.auth
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]

class GoogleCalendarHelper:
    def __init__(self, credentials_path="credentials.json", token_path="token.json"):
        self.credentials_path = credentials_path
        self.token_path = token_path
        self.service = self.authenticate()

    def authenticate(self):
        creds = None
        if os.path.exists(self.token_path):
            creds = Credentials.from_authorized_user_file(self.token_path, SCOPES)

        if not creds or not creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
            with open(self.token_path, "w") as token:
                token.write(creds.to_json())

        return build("calendar", "v3", credentials=creds)

    def create_event(self, summary, start_time, end_time, description="", attendees=None):
        event = {
            "summary": summary,
            "description": description,
            "start": {"dateTime": start_time, "timeZone": "UTC"},
            "end": {"dateTime": end_time, "timeZone": "UTC"},
            "attendees": [{"email": email} for email in attendees] if attendees else [],
        }
        event = self.service.events().insert(calendarId="primary", body=event).execute()
        return event.get("htmlLink")

    def list_events(self, max_results=5):
        now = datetime.datetime.utcnow().isoformat() + "Z"
        events_result = self.service.events().list(
            calendarId="primary", timeMin=now, maxResults=max_results, singleEvents=True, orderBy="startTime"
        ).execute()
        events = events_result.get("items", [])
        return events

    def test_google_calendar_auth(self):
        # Load credentials from the 'token.json' file
        # remember to add your email as a test user in google auth plataform.
        creds = None
        if os.path.exists(self.token_path):
            creds = Credentials.from_authorized_user_file(self.token_path, SCOPES)

        if not creds or not creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
            with open(self.token_path, "w") as token:
                    token.write(creds.to_json())
        
        try:
            # Build the Google Calendar API service
            service = build('calendar', 'v3', credentials=creds)
            
            # Fetch the list of calendars
            calendars = service.calendarList().list().execute()
            print("Authentication successful! Here are your calendars:")
            for calendar in calendars.get('items', []):
                print(f"- {calendar['summary']}")
        except Exception as e:
            print("Authentication failed:", e)

# Call the test function
if __name__ == "__main__":
    google_calendar_helper = GoogleCalendarHelper()
    
    # Test authentication
    google_calendar_helper.test_google_calendar_auth()
    
    # List events
    events = google_calendar_helper.list_events()
    for event in events:
        print(event['summary'])
    