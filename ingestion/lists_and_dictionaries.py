
# Healthcare Data Engineering
# Python Lists

patient_ids = ["P1001", "P1002", "P1003"]

# Print the complete list
print(patient_ids)

# Access individual elements
print(patient_ids[0])
print(patient_ids[1])
print(patient_ids[2])

# Count the number of records
print(len(patient_ids))

patient = {
    "patient_id": "P1001",
    "age": 45,
    "department": "Cardiology",
    "visit_cost": 350.50,
    "insurance_provider": "Blue Cross"
}

print(patient["insurance_provider"])
