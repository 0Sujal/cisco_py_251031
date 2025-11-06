from mail import send_gmail
from config import to_address 

result = send_gmail(
    to_address,
    "Sujal - Test Subject from pystud19 - 06-11-2025",
    "Hello from Cisco!",
    attachment_path="/Users/sujdua/Downloads/IMG-20251023-WA0068.jpg"   # <-- put your image file path here
)

print("Mail sent successfully?", result)
