# Opens the preference input file and checks it is valid
def checkInput(inputFile):
    # try to open the file
    try:
        with open(inputFile, 'r') as f:
            # get the first line and remove the spaces/newlines
            firstLine = f.readline().strip()
            if firstLine == "":
                return None, "INVALID: Input file is empty"
            #ensure the first line is a positive integer
            try:
                n = int(firstLine)
            except ValueError:
                return None, "INVALID: First line must be an integer"
            
            if n< 0:
                return None, f"INVALID: {n} is not a non-negative number"
            
            # read the hospital preferences
            hospital_prefs = []
            for i in range(n):
                line = f.readline().strip()
                if not line:
                    return None, f"INVALID: Incomplete hospital preferences at line {i+2}"
                try:
                    # Convert the preferences into integers
                    prefs = [int(x) - 1 for x in line.split()]
                except ValueError:
                    return None, f"INVALID: Non-integer at line {i +2}"
                # make sure there are exactly n entries with no duplicates
                if len(prefs) != n or set(prefs) != set(range(n)):
                    return None
                hospital_prefs.append(prefs)
            
            #read the student preferences
            student_prefs = []
            for i in range(n):
                line = f.readline().strip()
                if not line:
                    return None, f"INVALID: Incomplete student preferences at line {i + 2 + n}"
                
                try:
                    prefs = [int(x) - 1 for x in line.split()]
                except ValueError:
                    return None, f"INVALID: Non-integer in student preferences at line {i + 2 + n}"
                if len(prefs) != n or set(prefs) != set(range(n)):
                    return None
                
                student_prefs.append(prefs)
            return (n, hospital_prefs, student_prefs), None
    # Handles missing file
    except FileNotFoundError:
        return None, "INVALID: Cannot open input file"

def parse_matching(matchedFile, n):
    # initialize tracking arrays for both student and hospital match
    hospital_match = [-1] * n
    student_match = [-1] * n
    count = 0

    # try to open matching file
    try:
        with open(matchedFile, 'r') as f:
            for line in f: # read each line
                line = line.strip()
                if not line:
                    continue

                # Check line format
                parts = line.split()
                if len(parts) != 2:
                    return None, None, f"INVALID: Bad matching line '{line}'"

                # try to convert to integers
                try:
                    h = int(parts[0]) - 1
                    s = int(parts[1]) - 1
                except ValueError:
                    return None, None, f"INVALID: Non-integer in matching line '{line}'"

                if not (0 <= h < n and 0 <= s < n):
                    return None, None, f"INVALID: ID out of range in matching line '{line}'"

                # Check for duplicates
                if hospital_match[h] != -1:
                    return None, None, f"INVALID: Hospital {h + 1} matched more than once"

                if student_match[s] != -1:
                    return None, None, f"INVALID: Student {s + 1} matched more than once"

                hospital_match[h] = s
                student_match[s] = h
                count += 1

        if count != n:
            return None, None, f"INVALID: Expected {n} matches, found {count}"

        return hospital_match, student_match, None

    except FileNotFoundError:
        return None, None, f"INVALID: Cannot open matching file '{matchedFile}'"


def checkStability(n, hospital_prefs, student_prefs, hospital_match, student_match):
    # student ranking table
    student_rank = [[0] * n for _ in range(n)]
    for s in range(n):
        for rank, h in enumerate(student_prefs[s]):
            student_rank[s][h] = rank
    
    # Check for blocking pairs
    for h in range(n):
        current_student = hospital_match[h]
        for s in hospital_prefs[h]:
            if s == current_student:
                break

            current_hospital = student_match[s]
            # student prefers h' over current h
            if student_rank[s][h] < student_rank[s][current_hospital]:
                return f"UNSTABLE: Blocking pair found: Hospital {h + 1} and Student {s + 1}"
    return None

def main():
    input_file = input("Give the input file name: ")
    matched_file = input("Give the matched file name: ")

    parsed, error = checkInput(input_file)
    if error:
        print(error)
        return

    n, hospital_prefs, student_prefs = parsed

    hospital_match, student_match, error = parse_matching(matched_file, n)
    if error:
        print(error)
        return

    error = checkStability(n, hospital_prefs, student_prefs, hospital_match, student_match)
    if error:
        print(error)
        return

    print("VALID STABLE")

if __name__ == "__main__":
    main()