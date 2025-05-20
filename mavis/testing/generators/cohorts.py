import csv
from datetime import date
import pathlib

from faker import Faker
from nhs_number import generate as generate_nhs_number

from .utils import parse_datatable


FIELD_NAMES = [
    "CHILD_NHS_NUMBER",
    "CHILD_FIRST_NAME",
    "CHILD_LAST_NAME",
    "CHILD_PREFERRED_FIRST_NAME",
    "CHILD_PREFERRED_LAST_NAME",
    "CHILD_DATE_OF_BIRTH",
    "CHILD_YEAR_GROUP",
    "CHILD_ADDRESS_LINE_1",
    "CHILD_ADDRESS_LINE_2",
    "CHILD_TOWN",
    "CHILD_POSTCODE",
    "CHILD_SCHOOL_URN",
]


class CohortGenerator:
    def __init__(self, datatable: [[str]], faker: Faker):
        self.rows = parse_datatable(datatable)
        self.faker = faker

    def save(self, path: pathlib.Path):
        with path.open("w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)

            writer.writeheader()

            for row in self.rows:
                writer.writerow(self.generate_row(row))

    def generate_row(self, row: dict):
        nhs_number = row.get("nhs_number") or generate_nhs_number()[0]
        given_name = row["given_name"]
        family_name = row["family_name"]
        preferred_given_name = row.get("preferred_given_name", "")
        preferred_family_name = row.get("preferred_family_name", "")

        year_group = row.get("year_group")
        date_of_birth = row.get("date_of_birth")

        if year_group is None and date_of_birth is None:
            date_of_birth = self.faker.date()
        elif date_of_birth is None:
            academic_year = date.today().year - int(year_group) - 6
            start_date = date(academic_year, 9, 1)
            end_date = date(academic_year + 1, 8, 31)
            date_of_birth = self.faker.date_between(start_date, end_date)
            year_group = None

        address_line_1 = row.get("address_line_1") or self.faker.street_address()
        address_line_2 = row.get("address_line_2") or self.faker.street_address()
        address_town = row.get("address_town") or self.faker.city()
        address_postcode = row.get("address_postcode") or self.faker.postcode()
        school_urn = row.get("school_urn", "131413")

        return {
            "CHILD_NHS_NUMBER": nhs_number,
            "CHILD_FIRST_NAME": given_name,
            "CHILD_LAST_NAME": family_name,
            "CHILD_PREFERRED_FIRST_NAME": preferred_given_name,
            "CHILD_PREFERRED_LAST_NAME": preferred_family_name,
            "CHILD_DATE_OF_BIRTH": date_of_birth,
            "CHILD_YEAR_GROUP": year_group,
            "CHILD_ADDRESS_LINE_1": address_line_1,
            "CHILD_ADDRESS_LINE_2": address_line_2,
            "CHILD_TOWN": address_town,
            "CHILD_POSTCODE": address_postcode,
            "CHILD_SCHOOL_URN": school_urn,
        }
