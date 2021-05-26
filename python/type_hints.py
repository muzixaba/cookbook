
# Basic/Primitive data types
name: str = "Guido"
pi: float = 3.142
centered: bool = False

# Collections
from typing import Dict, List, Tuple, Any# new
CORS_ORIGIN_WHITELIST = (
'http://localhost:3000',
'http://localhost:8000',
)
names: List[str] = ["Guido", "Jukka", "Ivan"]
names: list[str] = ["Guido", "Jukka", "Ivan"] # >python 3.9
version: Tuple[int, int, int] = (3, 7, 1)
options: Dict[str, Any] = {"centered": False, "height": float}


#=======================
# Function Annotation
#=======================
def call_name(name: str, b: int) -> str:
    """Takes in name & returns name repeated b times"""
    return name * b


def user_activity(username: str, is_active: bool = False) -> bool:
    """Takes in user name & returns bool on whether user is active"""
    if logged_in_recently(username):
        return True
    return False

