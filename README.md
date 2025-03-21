# Google Calendar API Configuration

To use the Google Calendar API, follow these steps to obtain the `credentials.json` file for authentication:

## Steps to Obtain `credentials.json`

1. **Go to the Google Cloud Console**  
   Visit [Google Cloud Console](https://console.cloud.google.com/).

2. **Create a New Project**  
   - Click on the project dropdown at the top of the page and select **New Project**.
   - Provide a name for your project and click **Create**.

3. **Enable the Google Calendar API**  
   - In the Cloud Console, go to **APIs & Services > Library**.
   - Search for "Google Calendar API" and click on it.
   - Click **Enable**.

4. **Set Up OAuth Consent Screen**  
   - Go to **APIs & Services > OAuth consent screen**.
   - Select **External** (if you're not part of an organization) and click **Create**.
   - Fill in the required fields (e.g., app name, email) and save.

5. **Create Credentials**  
   - Go to **APIs & Services > Credentials**.
   - Click **Create Credentials** and select **OAuth 2.0 Client IDs**.
   - Choose **Desktop app** as the application type.
   - Click **Create**.

6. **Download the `credentials.json` File**  
   - After creating the credentials, you’ll see a **Download** button.
   - Click it to download the `credentials.json` file.
   - Save this file in the same directory as your script or the path specified in your code.

7. **Add user email to test users**
    - Go to google auth plataform
    - Add test user

## Notes

- Ensure the `credentials.json` file is kept secure and not shared publicly.
- Refer to the [Google Calendar API Documentation](https://developers.google.com/calendar) for additional details.
