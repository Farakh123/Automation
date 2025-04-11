import smtplib
from email.message import EmailMessage
import time

# Email configuration (replace with your details)
YOUR_EMAIL = "farakhfrq@gmail.com"  # Your email address
YOUR_PASSWORD = ""  # Use an App Password if using Gmail
SMTP_SERVER = "smtp.gmail.com"  # For Gmail
SMTP_PORT = 465  # For TLS

# List of recipient emails (from the document)
recipient_emails = [
    "moeen.alam@7vals.com",
    "hr@abark.pk",
    "hr@bigentities.com",
    "hr@brainxtech.com",
    "careers@cba.com.pk",
    "mmasood@cinnova.com",
    "hr@clustox.com", "faryal.butt@clustox.com",
    "careers@codeFulcrum.com",
    "hr@coderzhunt.com",
    "hr@conradlabs.com",
    "contourhr@contour-software.com",
    "billal@deducationist.com",
    "careers@datumbrain.com",
    "sahar.afzal@devsinc.com",
    "shahroz.ahmed@dubizzlelabs.com",
    "rana.salman@educative.io",
    "mahvish.qasim@ewsystemsinc.com",
    "careers@focustext.com",
    "people@folium.ai",
    "farahijaz@gsoftconsulting.com",
    "anum@hazen.ai",
    "reena@hrint.io",
    "rkhalid01@i2cinc.com", "Recruitment@i2cinc.com",
    "hr@innovaxel.com",
    "hr@inovaqo.com",
    "hr@ml1.a",
    "hr.pk@ccjk.com", "qasim.cheema@ccjk.com",
    "bilal.nazir@mcb.com.pk",
    "career@mergestack.com",
    "pk-recruiting@gomotive.com",
    "maggie.ma@gomotive.com",
    "sherjeel@shaleeglobal.com",
    "careers@netsoltech.com",
    "kainat.all@nxb.com.pk",
    "hr@nkutechnologies.com",
    "saad.jaral@northbaysolutions.net",
    "hr@pakeventures.com",
    "hr@pikessoft.com",
    "careers@rolustech.com",
    "hr@senarios.co",
    "hr@spearlogicsolutions.com",
    "hr@staunch.co",
    "TBS-PKHR@stewart",
    "Hr@symufolk.com",
    "imaan.naseer@tajir-app.com",
    "careers@tboxsolutionz.com",
    "hrm@techbridgeconsultancy.com",
    "hr@technocares.com",
    "hr@techtics.ai",
    "hr@techtimize.co",
    "careers@thehexatown.com",
    "amina.ahmed@corp.tkxel.com",
    "hiba.waleed@unduit.com",
    "muhammadumais@webncodes.com",
    "careers@whiteboxtech.net"
]
RESUME_PATH = "./FarakhFarooq.pdf"
# Email content
subject = "Application for Data Analyst Internship Opportunity"
body = """Dear Hiring Manager,

I hope this email finds you well. My name is Farakh Farooq, and I am currently a 6th semester student at FCIT, Punjab University Lahore with a strong passion for data analysis and Automation.

I came across your company during the 14th FCIT Career Fair 2025 and was impressed by your work and your team culture that I briefly viewed. I am writing to express my interest in a Data Analyst internship opportunity at your organization.

I have experience with Python, SQL, Tableau,Tesseract and have completed projects involving [briefly mention 1-2 relevant projects]. I am eager to contribute my skills and learn from your team.

I have attached my resume for your review. I would greatly appreciate the opportunity to discuss how I can contribute to your team. Please let me know if there are any internship openings or if I can provide any additional information.
Currently, I am also learning Japanese and at the level of N5. I would be perfect match for your international clients and give you an edge on how to make them feel welcome culturally. I have achieved this level in just two months. And it also means
that I can learn anything faster than most people. I know that if you give me a chance you will not regret it

Thank you for your time and consideration. I look forward to your response.

Best regards,
Farakh Farooq
+923206878178
https://www.linkedin.com/in/farakh-farooq-a52037232/
"""

# Function to send emails
def send_emails_with_resume():
    try:
        # Connect to SMTP server
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(YOUR_EMAIL, YOUR_PASSWORD)
        print("Success! Server supports SSL.")

        # Read resume file
        try:
            with open(RESUME_PATH, "rb") as f:
                resume_data = f.read()
                resume_name = RESUME_PATH.split("/")[-1]  # Extracts filename
        except Exception as e:
            print(f"Failed to read resume file: {str(e)}")
            return

        # Send emails to each recipient
        for email in recipient_emails:
            if not "@" in email:
                continue

            msg = EmailMessage()
            msg["From"] = YOUR_EMAIL
            msg["To"] = email
            msg["Subject"] = subject
            msg.set_content(body)

            # Attach resume
            msg.add_attachment(
                resume_data,
                maintype="application",
                subtype="pdf",  # or "octet-stream" if not PDF
                filename=resume_name
            )

            try:
                server.send_message(msg)
                print(f"Email with resume sent to {email}")
                time.sleep(2)  # Anti-spam delay
            except Exception as e:
                print(f"Failed to send to {email}: {str(e)}")

        server.quit()
        print("All emails with resumes sent successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")

# Run the function
send_emails_with_resume()