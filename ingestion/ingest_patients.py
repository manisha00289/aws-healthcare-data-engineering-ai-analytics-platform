

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "patients.json"
ERROR_FILE = PROJECT_ROOT / "data" / "invalid_patients.json"
PROCESSED_FILE = (
    PROJECT_ROOT / "data" / "processed" / "validated_patients.json"
)
REQUIRED_FIELDS = {
    "patient_id",
    "age",
    "department",
    "visit_cost",
    "insurance_provider",
}


def load_patient_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        records = json.load(file)

    if not isinstance(records, list):
        raise ValueError("Expected a list of patient records.")

    return records


def validate_patient_record(record):
    if not isinstance(record, dict):
        return False, "Record must be a dictionary."

    missing_fields = REQUIRED_FIELDS - record.keys()

    if missing_fields:
        return False, f"Missing fields: {sorted(missing_fields)}"

    if not isinstance(record["patient_id"], str):
        return False, "patient_id must be a string."

    if not isinstance(record["age"], int) or isinstance(record["age"], bool):
        return False, "age must be an integer."

    if not 0 < record["age"] <= 120:
        return False, "age must be between 1 and 120."

    if not isinstance(record["visit_cost"], (int, float)):
        return False, "visit_cost must be numeric."

    if record["visit_cost"] < 0:
        return False, "visit_cost cannot be negative."

    return True, None


def process_patient_records(records):
    valid_records = []
    invalid_records = []

    for record in records:
        is_valid, error_message = validate_patient_record(record)

        if is_valid:
            valid_records.append(record)
        else:
            invalid_records.append({
                "record": record,
                "error": error_message,
            })

    return valid_records, invalid_records


def save_json(file_path, data):
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def main():
    records = load_patient_data(INPUT_FILE)

    valid_records, invalid_records = process_patient_records(records)
    save_json(PROCESSED_FILE, valid_records)

    save_json(ERROR_FILE, invalid_records)
    print(f"Records loaded: {len(records)}")
    print(f"Valid records: {len(valid_records)}")
    print(f"Invalid records: {len(invalid_records)}")


if __name__ == "__main__":
    main()

     