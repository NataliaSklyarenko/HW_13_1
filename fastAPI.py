from fastapi import FastAPI, HTTPException, Depends
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
import secrets

app = FastAPI()

conf = ConnectionConfig(
    MAIL_USERNAME="your_email@gmail.com",
    MAIL_PASSWORD="your_password",
    MAIL_FROM="your_email@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com"
)

fm = FastMail(conf)

users = {}

@app.post("/register/")
async def register_user(email: str):
    if email in users:
        raise HTTPException(status_code=400, detail="Email already registered")
    verification_code = secrets.token_hex(16)
    users[email] = verification_code

    message = MessageSchema(
        subject="Email Verification",
        recipients=[email],
        body=f"Please click on the following link to verify your email: http://yourdomain.com/verify?code={verification_code}"
    )
    await fm.send_message(message)
    return {"message": "Email sent for verification"}

@app.get("/verify/")
async def verify_email(code: str, email: str):
    if email not in users or users[email] != code:
        raise HTTPException(status_code=400, detail="Invalid verification code")
    # Ваш код для підтвердження електронної пошти
    return {"message": "Email verified successfully"}
