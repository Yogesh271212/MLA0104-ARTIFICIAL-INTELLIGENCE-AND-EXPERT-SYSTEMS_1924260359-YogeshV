citizens = [
    {'name': 'Arun Kumar', 'dob': '1998-05-14', 'city': 'Chennai'},
    {'name': 'Priya Sharma', 'dob': '2001-11-23', 'city': 'Coimbatore'},
    {'name': 'Karthik Raja', 'dob': '1995-02-10', 'city': 'Madurai'},
    {'name': 'Divya Nair', 'dob': '2001-08-19', 'city': 'Trichy'}
]

def find_by_dob(dob):
    return [c for c in citizens if c['dob'] == dob]

def find_by_birth_year(year):
    return [c['name'] for c in citizens if c['dob'].startswith(str(year))]

def get_dob_by_name(name):
    for c in citizens:
        if c['name'].lower() == name.lower():
            return c['dob']
    return "Record not found"

print("Citizen born on 1998-05-14:", find_by_dob('1998-05-14'))
print("Citizens born in 2001:", find_by_birth_year(2001))
print("DOB of Karthik Raja:", get_dob_by_name('Karthik Raja'))
