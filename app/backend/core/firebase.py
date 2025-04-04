import firebase_admin
from firebase_admin import auth, credentials
from fastapi import HTTPException

# Load Firebase credentials
cred = credentials.Certificate("core/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


def create_user(name: str, email: str, password: str):
    """
    Creates a new user in Firebase Authentication.
    Firebase automatically hashes the password.
    """
    try:
        user_record = auth.create_user(
            email=email,
            password=password,  # Firebase securely hashes it internally
            display_name=name
        )
        return {"uid": user_record.uid, "email": user_record.email, "name": name}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Firebase Error: {str(e)}")


def verify_firebase_token(token: str):
    """
    Verifies a Firebase authentication token.
    Returns user information if valid.
    """
    try:
        decoded_token = auth.verify_id_token(token)
        return {"uid": decoded_token["uid"], "email": decoded_token["email"]}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid or expired token")