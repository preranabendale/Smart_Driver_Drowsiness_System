import smtplib
from email.message import EmailMessage
import requests
import json
import mimetypes

# Email credentials
Sender_Email = "prerana.sct@gmail.com"
Receiver_Email = "preranabendale1@gmail.com"
Password = 'ymtp edak ytds hgvk'  # App Password

# Image path to attach (change this to your actual image path)
image_path = "drowsiness_capture.jpg"

# Create the email message
newMessage = EmailMessage()
newMessage['Subject'] = "🚨 Drowsiness Detected - Urgent Help Needed!"
newMessage['From'] = Sender_Email
newMessage['To'] = Receiver_Email

# Get location using IPStack API
location_req_url = 'http://api.ipstack.com/103.51.95.183?access_key=2a52b4c622bd8d465b8aeb4fe498cbdd'
try:
    r = requests.get(location_req_url)
    location_obj = json.loads(r.text)

    lat = location_obj.get('latitude', 'N/A')
    lon = location_obj.get('longitude', 'N/A')
    city = location_obj.get('city', 'Unknown')

    print(f"Latitude: {lat}")
    print(f"Longitude: {lon}")
    print(f"City: {city}")

    # Email body text with Google Maps link
    email_body = (
        "Hi,\n\n"
        "⚠️ Driver drowsiness has been detected. Please respond immediately.\n\n"
        f"📍 Location details:\n"
        f"City: {city}\n"
        f"Latitude: {lat}\n"
        f"Longitude: {lon}\n"
        f"🌐 Google Maps: https://www.google.com/maps/search/?api=1&query={lat},{lon}\n\n"
        "🛡️ Sent by your Safety App"
    )

    newMessage.set_content(email_body)

    # Attach image
    with open(image_path, 'rb') as img:
        mime_type, _ = mimetypes.guess_type(image_path)
        mime_main, mime_sub = mime_type.split('/')
        newMessage.add_attachment(img.read(), maintype=mime_main, subtype=mime_sub, filename=image_path)

    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)
        smtp.send_message(newMessage)
        print("✅ Mail with image and location sent successfully")

except Exception as e:
    print("❌ Error sending mail:", e)
