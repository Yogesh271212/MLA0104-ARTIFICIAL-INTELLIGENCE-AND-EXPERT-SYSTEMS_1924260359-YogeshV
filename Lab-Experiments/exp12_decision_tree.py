from sklearn.tree import DecisionTreeClassifier

X = [
    [25, 30000, 600],
    [35, 60000, 750],
    [45, 80000, 800],
    [20, 15000, 500],
    [30, 40000, 650],
    [50, 90000, 780]
]
y = ['Rejected', 'Approved', 'Approved', 'Rejected', 'Rejected', 'Approved']

clf = DecisionTreeClassifier()
clf.fit(X, y)

new_applicant = [[32, 55000, 720]]
prediction = clf.predict(new_applicant)
print("Applicant Details (Age, Income, CreditScore):", new_applicant[0])
print("Loan Status Prediction:", prediction[0])
