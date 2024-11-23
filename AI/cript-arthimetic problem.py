from itertools import permutations
def solve_crypto_arithmetic():
    letters = 'SENDMORY'
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue
        send = 1000 * mapping['S'] + 100 * mapping['E'] + 10 * mapping['N'] + mapping['D']
        more = 1000 * mapping['M'] + 100 * mapping['O'] + 10 * mapping['R'] + mapping['E']
        money = 10000 * mapping['M'] + 1000 * mapping['O'] + 100 * mapping['N'] + 10 * mapping['E'] + mapping['Y']
        if send + more == money:
            print("Solution found:")
            print(f"SEND = {send}")
            print(f"MORE = {more}")
            print(f"MONEY = {money}")
            print(f"Mapping: {mapping}")
            return
    print("No solution found.")
solve_crypto_arithmetic()
