import os
import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/calendar"]

class GoogleCalendarHelper:
    """
    Helper class to manage Google Calendar events.
    """

    # Add required attributes for OpenAI SDK compatibility
    name = "google_calendar_helper"
    description = "Manage Google Calendar events, including creating, updating, and deleting events."

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

    def create_event(self, event_details: dict):
        """
        Create a calendar event.
        :param event_details: A dictionary containing event details.
        :return: A success message or error.
        """
        summary = event_details.get("summary")
        start_time = event_details.get("start_time")
        end_time = event_details.get("end_time")
        description = event_details.get("description", "")
        attendees = event_details.get("attendees", [])

        event = {
            "summary": summary,
            "description": description,
            "start": {"dateTime": start_time, "timeZone": "UTC"},
            "end": {"dateTime": end_time, "timeZone": "UTC"},
            "attendees": [{"email": email} for email in attendees] if attendees else [],
        }
        event = self.service.events().insert(calendarId="primary", body=event).execute()
        return "Event created successfully."

    def list_events(self, max_results=5):
        now = datetime.datetime.utcnow().isoformat() + "Z"
        events_result = self.service.events().list(
            calendarId="primary", timeMin=now, maxResults=max_results, singleEvents=True, orderBy="startTime"
        ).execute()
        events = events_result.get("items", [])
        return events
    
    def update_event(self, event_id: str, updated_details: dict):
        """
        Update an existing calendar event.
        :param event_id: The ID of the event to update.
        :param updated_details: A dictionary containing updated event details.
        :return: A success message or error.
        """
        event = self.service.events().get(calendarId="primary", eventId=event_id).execute()

        # Update fields if provided
        if "summary" in updated_details:
            event["summary"] = updated_details["summary"]
        if "start_time" in updated_details and "end_time" in updated_details:
            event["start"] = {"dateTime": updated_details["start_time"], "timeZone": "UTC"}
            event["end"] = {"dateTime": updated_details["end_time"], "timeZone": "UTC"}
        if "description" in updated_details:
            event["description"] = updated_details["description"]
        if "attendees" in updated_details:
            event["attendees"] = [{"email": email} for email in updated_details["attendees"]]

        updated_event = self.service.events().update(calendarId="primary", eventId=event_id, body=event).execute()
        return "Event updated successfully."

    def delete_event(self, event_id: str):
        """
        Delete a calendar event.
        :param event_id: The ID of the event to delete.
        :return: A success message or error.
        """
        self.service.events().delete(calendarId="primary", eventId=event_id).execute()
        return "Event deleted successfully."

    def test_google_calendar_auth(self):
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

# Test functions
if __name__ == "__main__":
    google_calendar_helper = GoogleCalendarHelper()
    google_calendar_helper.test_google_calendar_auth()
    events = google_calendar_helper.list_events()
    for event in events:
        print(event['summary'])