import itertools

def solve_cryptarithmetic():
    letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
    digits = range(10)

    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
        if sol['S'] == 0 or sol['M'] == 0:
            continue

        send = 1000 * sol['S'] + 100 * sol['E'] + 10 * sol['N'] + sol['D']
        more = 1000 * sol['M'] + 100 * sol['O'] + 10 * sol['R'] + sol['E']
        money = 10000 * sol['M'] + 1000 * sol['O'] + 100 * sol['N'] + 10 * sol['E'] + sol['Y']

        if send + more == money:
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
            print("Digit Assignments:", sol)
            return

solve_cryptarithmetic()
