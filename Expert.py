def diagnose(symptoms):
    diseases = {
        "Common Cold": {"cough", "sneezing", "sore throat"},
        "Flu": {"fever", "headache", "cough", "body pain"},
        "Malaria": {"fever", "chills", "sweating"},
        "Typhoid": {"fever", "abdominal pain", "headache"},
        "COVID-19": {"fever", "cough", "breathing difficulty", "loss of taste", "loss of smell"}
    }
    possible_diseases = []

    for disease, disease_symptoms in diseases.items():
        match_count = len(disease_symptoms.intersection(symptoms))
        if match_count >= len(disease_symptoms) / 2:  # at least 50% symptoms match
            possible_diseases.append(disease)

    return possible_diseases
print("Welcome to the Medical Diagnosis Expert System")
print("Please enter your symptoms separated by commas:")
user_input = input("Symptoms: ").lower().split(",")
user_symptoms = set([s.strip() for s in user_input])
result = diagnose(user_symptoms)
if result:
    print("\nBased on your symptoms, you may have:")
    for disease in result:
        print(f"- {disease}")
else:
    print("\nNo matching disease found. Please consult a doctor for accurate diagnosis.")
