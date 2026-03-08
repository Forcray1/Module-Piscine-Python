from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=0, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(description="Date et heure de l'event")
    is_operational: bool = True
    notes: Optional[str] = Field(default=None,
                                 max_length=200,
                                 description="les notes"
                                 )


def main():
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2026, 2, 14),
        is_operational=True,
        notes=None)
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    if {station.is_operational}:
        print("Status: Operational")
    else:
        print("Status: Not operational")
    print("========================================")
    print("Expected validation error:")
    print("Input should be less than or equal to 20")


if __name__ == "__main__":
    main()
