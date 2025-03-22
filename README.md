# Google Calendar Agent: API and Whatsapp Bot

Code for using a calendar agent built with langchain.

## Google Cloud Setup

To use the Google Calendar API, follow these steps to obtain the `credentials.json` file for authentication:

### Steps to Obtain `credentials.json`

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

## Whatsap Setup

- Refer to [Daveebbelaar - Python Whatssap Bot repo](https://github.com/daveebbelaar/python-whatsapp-bot/tree/main)

### Get Started

1. **Overview & Setup**: Begin your journey [here](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started).
2. **Locate Your Bots**: Your bots can be found [here](https://developers.facebook.com/apps/).
3. **WhatsApp API Documentation**: Familiarize yourself with the [official documentation](https://developers.facebook.com/docs/whatsapp).
4. **Helpful Guide**: Here's a [Python-based guide](https://developers.facebook.com/blog/post/2022/10/24/sending-messages-with-whatsapp-in-your-python-applications/) for sending messages.
5. **API Docs for Sending Messages**: Check out [this documentation](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages).

#### Step 1: Select Phone Numbers

- Make sure WhatsApp is added to your App.
- You begin with a test number that you can use to send messages to up to 5 numbers.
- Go to API Setup and locate the test number from which you will be sending messages.
- Here, you can also add numbers to send messages to. Enter your **own WhatsApp number**.
- You will receive a code on your phone via WhatsApp to verify your number.

#### Step 2: Send Messages with the API

1. Obtain a 24-hour access token from the API access section.
2. It will show an example of how to send messages using a `curl` command which can be send from the terminal or with a tool like Postman.
3. Let's convert that into a [Python function with the request library](https://github.com/daveebbelaar/python-whatsapp-bot/blob/main/start/whatsapp_quickstart.py).
4. Create a `.env` files based on `example.env` and update the required variables. [Video example here](https://www.youtube.com/watch?v=sOwG0bw0RNU).
5. You will receive a "Hello World" message (Expect a 60-120 second delay for the message).

Creating an access that works longer then 24 hours

1. Create a [system user at the Meta Business account level](https://business.facebook.com/settings/system-users).
2. On the System Users page, configure the assets for your System User, assigning your WhatsApp app with full control. Don't forget to click the Save Changes button.
   - [See step 1 here](https://github.com/daveebbelaar/python-whatsapp-bot/blob/main/img/meta-business-system-user-token.png)
   - [See step 2 here](https://github.com/daveebbelaar/python-whatsapp-bot/blob/main/img/adding-assets-to-system-user.png)
3. Now click `Generate new token` and select the app, and then choose how long the access token will be valid. You can choose 60 days or never expire.
4. Select all the permissions, as I was running into errors when I only selected the WhatsApp ones.
5. Confirm and copy the access token.

Now we have to find the following information on the **App Dashboard**:

- **APP_ID**: "<YOUR-WHATSAPP-BUSINESS-APP_ID>" (Found at App Dashboard)
- **APP_SECRET**: "<YOUR-WHATSAPP-BUSINESS-APP_SECRET>" (Found at App Dashboard)
- **RECIPIENT_WAID**: "<YOUR-RECIPIENT-TEST-PHONE-NUMBER>" (This is your WhatsApp ID, i.e., phone number. Make sure it is added to the account as shown in the example test message.)
- **VERSION**: "v18.0" (The latest version of the Meta Graph API)
- **ACCESS_TOKEN**: "<YOUR-SYSTEM-USER-ACCESS-TOKEN>" (Created in the previous step)

> You can only send a template type message as your first message to a user. That's why you have to send a reply first before we continue. Took me 2 hours to figure this out.

## Notes

- Ensure the `credentials.json` file is kept secure and not shared publicly.
- Refer to the [Google Calendar API Documentation](https://developers.google.com/calendar) for additional details.
