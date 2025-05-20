import csv
from datetime import date, datetime

from faker import Faker
from nhs_number import generate as generate_nhs_number

from .utils import parse_datatable


FIELD_NAMES = [
    "ORGANISATION_CODE",
    "NHS_NUMBER",
    "PERSON_FORENAME",
    "PERSON_SURNAME",
    "PERSON_DOB",
    "PERSON_GENDER_CODE",
    "PERSON_POSTCODE",
    "DATE_OF_VACCINATION",
    "CARE_SETTING",
    "SCHOOL_URN",
    "PROGRAMME",
    "VACCINE_GIVEN",
    "BATCH_NUMBER",
    "BATCH_EXPIRY_DATE",
    "DOSE_SEQUENCE",
    "ANATOMICAL_SITE",
]


class VaccinationsGenerator:
    def __init__(self, kind: str, datatable: [[str]], faker: Faker):
        self.kind = kind
        self.rows = parse_datatable(datatable)
        self.faker = faker

    def save(self, path):
        with path.open("w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)

            writer.writeheader()

            for row in self.rows:
                writer.writerow(self.generate_row(row))

    def generate_row(self, row: dict):
        organisation_code = "R1L"
        nhs_number = row.get("nhs_number") or generate_nhs_number()[0]
        given_name = row["given_name"]
        family_name = row["family_name"]
        gender_code = row.get("gender_code", "not known")

        year_group = row.get("year_group")
        date_of_birth = row.get("date_of_birth")

        if year_group is None and date_of_birth is None:
            date_of_birth = self.faker.date()
        elif date_of_birth is None:
            academic_year = date.today().year - int(year_group) - 6
            start_date = date(academic_year, 9, 1)
            end_date = date(academic_year + 1, 8, 31)
            date_of_birth = self.faker.date_between(start_date, end_date)

        address_postcode = row.get("address_postcode") or self.faker.postcode()

        date_of_vaccination = row.get("date_of_vaccination") or self.faker.date_between(
            date_of_birth, date.today()
        )
        care_setting = "1"
        school_urn = row.get("school_urn", "131413")

        programme = row.get("programme", "HPV")
        vaccine = row.get("vaccine", "Cervarix")
        batch_name = row.get("batch_name") or self.faker.pyint(
            min_value=10_000, max_value=99_999
        )
        batch_expiry_date = self.faker.date_between(date_of_vaccination, date.today())
        dose_sequence = row.get("dose_sequence")
        anatomical_site = row.get("anatomical_site", "left upper arm")

        return {
            "ORGANISATION_CODE": organisation_code,
            "NHS_NUMBER": nhs_number,
            "PERSON_FORENAME": given_name,
            "PERSON_SURNAME": family_name,
            "PERSON_DOB": date_of_birth,
            "PERSON_GENDER_CODE": gender_code,
            "PERSON_POSTCODE": address_postcode,
            "DATE_OF_VACCINATION": date_of_vaccination,
            "CARE_SETTING": care_setting,
            "SCHOOL_URN": school_urn,
            "PROGRAMME": programme,
            "VACCINE_GIVEN": vaccine,
            "BATCH_NUMBER": batch_name,
            "BATCH_EXPIRY_DATE": batch_expiry_date,
            "DOSE_SEQUENCE": dose_sequence,
            "ANATOMICAL_SITE": anatomical_site,
        }
