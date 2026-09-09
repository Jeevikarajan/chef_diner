from app.database import SessionLocal
from app.models import Dialogue

dialogues = [
    {
        "dialogue_text": "Congratulations! You have won ₹50,000. Click this link to claim your prize.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Reject",
        "explanation": "Unexpected prize messages and suspicious links are common phishing attempts."
    },
    {
        "dialogue_text": "Your bank account will be blocked today. Share your OTP immediately to keep your account active.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Reject",
        "explanation": "Banks never ask customers to share OTPs."
    },
    {
        "dialogue_text": "Click here to watch the exclusive video: www.faceb00k-login.com. Log in with your Facebook account to continue.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Reject",
        "explanation": "The misspelled domain is a strong sign of a fake website."
    },
    {
        "dialogue_text": "Your manager asks you to review a document from the company's official shared drive.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Accept",
        "explanation": "A document from a verified company source can normally be opened."
    },
    {
        "dialogue_text": "You receive an email asking you to urgently reset your password through an unfamiliar link.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Reject",
        "explanation": "Urgent password-reset links from unknown sources may lead to fake login pages."
    },
    {
        "dialogue_text": "A colleague sends you a file through the company's verified internal messaging system.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Accept",
        "explanation": "Files received through a trusted internal channel are generally safer to access."
    },
    {
        "dialogue_text": "You receive a message saying your package is delayed and asking for your credit card details through a shortened URL.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Reject",
        "explanation": "Unexpected requests for card details through shortened links are suspicious."
    },
    {
        "dialogue_text": "Your university sends an announcement through its official student portal.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Accept",
        "explanation": "Messages received through a verified university portal are generally trustworthy."
    },
    {
        "dialogue_text": "An unknown person emails you asking for your company login credentials to verify your account.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Reject",
        "explanation": "You should never share login credentials with unknown people."
    },
    {
        "dialogue_text": "A website asks you to download a browser extension before allowing you to view a free video.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Reject",
        "explanation": "Unexpected browser extensions can contain malicious software."
    },
    {
        "dialogue_text": "Your bank's official mobile application displays a notification about your recent transaction.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Accept",
        "explanation": "Notifications inside the official banking application can be trusted."
    },
    {
        "dialogue_text": "You receive an email from an unknown sender containing an unexpected ZIP file.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Reject",
        "explanation": "Unexpected attachments from unknown senders may contain malware."
    },
    {
        "dialogue_text": "A verified company administrator asks you to attend a meeting through the organization's official calendar.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Accept",
        "explanation": "A meeting invitation from a verified organizational account is normally safe."
    },
    {
        "dialogue_text": "A message claims your social media account will be permanently deleted unless you provide your password immediately.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Reject",
        "explanation": "Threats combined with requests for passwords are common phishing tactics."
    },
    {
        "dialogue_text": "You receive a suspicious QR code asking you to scan it to receive a cash reward.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Reject",
        "explanation": "Unknown QR codes can redirect users to malicious websites."
    },
    {
        "dialogue_text": "Your company security team sends a password-security reminder through the official internal portal.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Accept",
        "explanation": "Security announcements from verified internal systems are legitimate."
    },
    {
        "dialogue_text": "An unknown caller says they are from your bank and asks for your OTP to cancel a fraudulent transaction.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Reject",
        "explanation": "Never share OTPs over phone calls, even if the caller claims to be from your bank."
    },
    {
        "dialogue_text": "You receive an email containing a link to an unknown website claiming you have been selected for a job.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Reject",
        "explanation": "Unexpected job offers from unknown sources should be verified before clicking links."
    },
    {
        "dialogue_text": "You access your university results by manually typing the official university website address into your browser.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Accept",
        "explanation": "Manually entering a known official website reduces the risk of visiting a fake link."
    },
    {
        "dialogue_text": "A pop-up says your computer has five viruses and asks you to call an unknown phone number immediately.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Reject",
        "explanation": "Fake virus alerts often try to trick users into contacting scammers."
    },
    {
        "dialogue_text": "Your teammate sends you a project file that you were expecting through the company's official email.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Accept",
        "explanation": "An expected file from a known teammate through an official channel is reasonable to open."
    },
    {
        "dialogue_text": "An email asks you to send your Aadhaar number and bank details to receive a surprise refund.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Reject",
        "explanation": "Unexpected requests for sensitive personal and financial information are suspicious."
    },
    {
        "dialogue_text": "A website address changes from amazon.com to amaz0n-security.com and asks you to sign in.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Reject",
        "explanation": "Lookalike domains using altered characters are commonly used for phishing."
    },
    {
        "dialogue_text": "Your company's official HR portal asks you to complete your annual employee information update.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Accept",
        "explanation": "Requests through an authenticated official HR portal are generally legitimate."
    },
    {
        "dialogue_text": "A stranger sends you a message asking you to install AnyDesk so they can fix your computer remotely.",
        "option_accept": "Accept",
        "option_decline": "Reject",
        "correct_answer": "Reject",
        "explanation": "Giving unknown people remote access to your computer can expose your files and accounts."
    }
]

db = SessionLocal()

try:
    db.query(Dialogue).delete()

    for item in dialogues:
        db.add(Dialogue(**item))

    db.commit()
    print(f"Successfully inserted {len(dialogues)} dialogues.")

finally:
    db.close()