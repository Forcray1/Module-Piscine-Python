from datetime import datetime
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(description="Date et heure de l'event")
    location: str = Field(min_length=3, max_length=100)
    contact_type: Literal["radio", "visual", "physical", "telepathic"]
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(min_length=0, max_length=500)
    is_verified: bool = False


def main() -> None:
    print("Alien Contact Log Validation\n")
    print("======================================")
    alien_contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 1, 1),
        location="Area 51, Nevada",
        contact_type="radio",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True
    )
    print(f"ID: {alien_contact.contact_id}")
    print(f"Type: {alien_contact.contact_type}")
    print(f"Location: {alien_contact.location}")
    print(f"Signal: {alien_contact.signal_strength}")
    print(f"Duration: {alien_contact.duration_minutes}")
    print(f"Witnesses: {alien_contact.witness_count}")
    print(f"Message: {alien_contact.message_received}")
    print("======================================")
    print("Expected validation error:")
    print("Telepathic contact requires at least 3 witnesses")


if __name__ == "__main__":
    main()
