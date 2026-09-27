patients = [
    {
        "patient_id": "P1001",
        "age": 45,
        "department": "Cardiology",
        "visit_cost": 350.50,
        "insurance_provider": "Blue Cross"
    },
    {
        "patient_id": "P1002",
        "age": 62,
        "department": "Neurology",
        "visit_cost": 420.00,
        "insurance_provider": "Aetna"
    },
    {
        "patient_id": "P1003",
        "age": 37,
        "department": "Orthopedics",
        "visit_cost": 275.75,
        "insurance_provider": "UnitedHealthcare"
    },
    {
            "patient_id": "P1004",
            "age": 51,
            "department": "Oncology",
            "visit_cost": 500.00,
            "insurance_provider": "Cigna"
        },
]

for patient in patients:
    print(
        patient["patient_id"],
        patient["department"],
        patient["visit_cost"]
    )


total_visit_cost = sum(
    patient["visit_cost"] for patient in patients
)

print("Total visit cost:", total_visit_cost)


import json

with open("data/patients.json", "w") as file:
    json.dump(patients, file, indent=4)