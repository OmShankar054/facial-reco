import cv2
import boto3
import os
from botocore.exceptions import NoCredentialsError
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv  # For loading credentials securely from .env file

# Load environment variables from .env file
load_dotenv()

# Initialize webcam (0 for the default camera)
cap = cv2.VideoCapture(0)

# Capture a frame from the video feed
ret, frame = cap.read()

# Save the frame as a snapshot if successful
snapshot_path = 'snapshot.jpg'
if ret:
    cv2.imwrite(snapshot_path, frame)

# Release the camera
cap.release()

s3 = boto3.client('s3')

# Upload the image to S3
def upload_to_s3(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    try:
        s3.upload_file(file_name, bucket, object_name)
        # Get the public URL for the uploaded image
        snapshot_url = f"https://{bucket}.s3.amazonaws.com/{object_name}"
        return snapshot_url
    except NoCredentialsError:
        print("Credentials not available")
        return None

# Replace with your S3 bucket name
bucket_name = 'face-reco-storage' 
snapshot_url = upload_to_s3('snapshot.jpg', bucket_name, f"snapshots/{snapshot_path}")

def send_email_with_attachment(snapshot_path, snapshot_url):
    from_email = os.getenv('EMAIL')  # Use environment variable
    to_email = 'akgabhay11@gmail.com'
    email_password = os.getenv('EMAIL_PASSWORD')  # Use environment variable
    subject = 'New Face Detected'

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add a body message
    body = f"A new face was detected. You can view the snapshot here: {snapshot_url}"
    msg.attach(MIMEText(body, 'plain'))

    # Attach the image (optional if not using the URL)
    with open(snapshot_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename={os.path.basename(snapshot_path)}")
        msg.attach(part)

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, email_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Send the email
if snapshot_url:
    send_email_with_attachment(snapshot_path, snapshot_url)
else:
    print("Snapshot URL is not available, email not sent.")
