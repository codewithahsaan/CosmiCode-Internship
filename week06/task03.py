import json

# Sample data (dictionary) to write into JSON
data = {
    "name": "Ali",
    "age": 22,
    "skills": ["Python", "Machine Learning", "Data Analysis"],
    "is_student": True
}

# --- Writing JSON to a file ---
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
print("✅ Data written to data.json successfully.")

# --- Reading JSON from the file ---
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)

print("\n📂 Data read from JSON file:")
print(loaded_data)

# Accessing specific values
print("\n🔎 Name:", loaded_data["name"])
print("🔎 Skills:", loaded_data["skills"])
