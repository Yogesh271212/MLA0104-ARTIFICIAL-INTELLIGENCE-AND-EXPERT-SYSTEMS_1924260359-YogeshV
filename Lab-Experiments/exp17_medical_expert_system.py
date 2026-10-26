rules = {
    'Flu': {'fever', 'cough', 'body_ache', 'fatigue'},
    'Common Cold': {'sneezing', 'runny_nose', 'sore_throat'},
    'Malaria': {'fever', 'chills', 'sweating', 'headache'},
    'Typhoid': {'prolonged_fever', 'abdominal_pain', 'weakness'},
    'Measles': {'fever', 'skin_rash', 'red_eyes', 'cough'}
}

def diagnose(symptoms):
    symptom_set = set(symptoms)
    best_match = None
    max_overlap = 0

    for disease, req_symptoms in rules.items():
        overlap = len(symptom_set.intersection(req_symptoms))
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = disease

    return best_match if max_overlap > 0 else "No matching disease found"

patient_symptoms = ['fever', 'chills', 'sweating', 'headache']
print("Patient Symptoms:", patient_symptoms)
print("Diagnosed Disease:", diagnose(patient_symptoms))
