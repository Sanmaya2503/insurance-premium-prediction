from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated


class user_input(BaseModel):

    age: Annotated[
        int,
        Field(
            ...,
            description="Age of the client",
            gt=0,
            lt=120,
            example=54
        )
    ]

    weight: Annotated[
        float,
        Field(
            ...,
            description="Weight of the client",
            gt=0,
            le=120
        )
    ]

    height: Annotated[
        float,
        Field(
            ...,
            description="Height of the client in meters",
            gt=0,
            le=2.5
        )
    ]

    income_lpa: Annotated[
        float,
        Field(
            ...,
            description="Income of client in LPA",
            gt=0
        )
    ]

    smoker: Annotated[
        bool,
        Field(
            ...,
            description="Client smoking status"
        )
    ]

    city: Annotated[
        str,
        Field(
            ...,
            description="Client living city"
        )
    ]

    occupation: Annotated[
        Literal[
            'retired',
            'freelancer',
            'student',
            'government_job',
            'business_owner',
            'unemployed',
            'private_job'
        ],
        Field(
            ...,
            description="Occupation of the client"
        )
    ]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)

    @computed_field
    @property
    def life_style_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "High Risk"
        elif self.smoker or self.bmi > 27:
            return "Medium"
        else:
            return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "Young"
        elif self.age < 45:
            return "addult"
        elif self.age < 60:
            return "middle aged"
        else:
            return "senior"

    @computed_field
    @property
    def city_tyre(self) -> int:

        tier_1_city = [
            "Chennai",
            "Mumbai",
            "Delhi",
            "Kolkata",
            "Bangalore",
            "Pune",
            "Hyderabad"
        ]

        tier_2_city = [
            "Jaipur",
            "Indore",
            "Kota",
            "Lucknow"
        ]

        if self.city in tier_1_city:
            return 1
        elif self.city in tier_2_city:
            return 2
        else:
            return 3

    @field_validator('city')
    @classmethod
    def normalize_city(cls, v: str) -> str:
        return v.strip().title()