def recommend_diet(age, bmi, condition):
    if condition.lower() == "diabetes":
        return "Low-glycemic diet: Whole grains, leafy greens, lean proteins, avoid refined sugar."
    elif condition.lower() == "hypertension":
        return "DASH diet: Low sodium, fruits, vegetables, low-fat dairy."
    elif bmi < 18.5:
        return "High-calorie nutrient-rich diet: Nuts, dairy, lean meat, complex carbs."
    elif 18.5 <= bmi < 25:
        return "Balanced maintenance diet: Fresh fruits, vegetables, whole grains, hydration."
    else:
        if age > 50:
            return "Low-calorie joint-friendly diet: Omega-3 rich fish, fiber, portion control."
        return "Calorie-deficit diet: High protein, high fiber, low saturated fat."

patients = [
    (28, 22.0, "None"),
    (55, 29.5, "Diabetes"),
    (42, 27.8, "Hypertension"),
    (19, 17.2, "None")
]

for age, bmi, cond in patients:
    print(f"Age: {age}, BMI: {bmi}, Condition: {cond}")
    print("Recommended Plan:", recommend_diet(age, bmi, cond))
    print("-" * 50)
