import hashlib
import requests
from typing import Tuple

class HIBPChecker:
    """
    Compromised password checker using the Have I Been Pwned API.
    Uses the k-anonymity method to protect privacy.
    """
    
    API_URL = "https://api.pwnedpasswords.com/range/"
    HEADERS = {"User-Agent": "Python-Password-Checker"}

    @staticmethod
    def _hash_password(password: str) -> Tuple[str, str]:
        """Converts password to SHA-1 and hashes into prefix/suffix."""
        sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
        return sha1_hash[:5], sha1_hash[5:]

    @staticmethod
    def _check_hibp(prefix: str, suffix: str) -> int:
        """Query the API and return the number of leaks found."""
        try:
            response = requests.get(
                f"{HIBPChecker.API_URL}{prefix}",
                headers=HIBPChecker.HEADERS,
                timeout=10  # We increase the timeout
            )
            response.raise_for_status()
            
            for line in response.text.splitlines():
                hibp_suffix, count = line.split(":")
                if hibp_suffix == suffix:
                    return int(count)
            return 0
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error connecting to HIBP: {str(e)}")
            return -1  # Error code

    @classmethod
    def check_password(cls, password: str) -> Tuple[int, str]:
        """
        Verifies a password in HIBP.

        Returns:
            Tuple[int, str]: (Number of leaks, Result message)
        """
        prefix, suffix = cls._hash_password(password)
        count = cls._check_hibp(prefix, suffix)
        
        if count == -1:
            return (0, "Connection error. Please try again.")
        elif count > 0:
            return (count, f"🔴 PASWORD ENGAGED! Appears in {count} leaks.")
        else:
            return (0, "✅ Not found in known leaks.")

# Example of independent use
if __name__ == "__main__":
    print("🔍 HIBP Password Checker (Autonomous Mode)")
    password = input("Enter password to verify: ")
    
    count, message = HIBPChecker.check_password(password)
    print("\nResult:")
    print(f"- Password: {'*' * len(password)}")
    print(f"- State: {message}")
    if count > 0:
        print(f"- 🔴 Recommendation: Change this password immediately.")