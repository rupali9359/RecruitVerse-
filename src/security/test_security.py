from jwt_handler import create_token, verify_token
from permissions import has_permission
from audit_logger import log_action

# test token
token = create_token("admin")
print("TOKEN:", token)

decoded = verify_token(token)
print("DECODED:", decoded)

# test permissions
print(has_permission("recruiter", "upload_resume"))  # True

# audit log
log_action("admin", "created campaign")