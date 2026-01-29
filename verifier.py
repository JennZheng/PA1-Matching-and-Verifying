# Opens the preference input file and checks it is valid
def checkInput(inputFile):
    # try to open the file
    try:
        with open(inputFile, 'r') as f:
            # get the first line and remove the spaces/newlines
            firstLine = f.readline().strip()
            if firstLine == "":
                return None, "Error: Input file is empty"
            #ensure the first line is a positive integer
            n = int(firstLine)
            if n< 0:
                return None, "Error: n must be a non-negative number"
            
            # read the hospital preferences
            hospital_prefs = []
            for i in range(n):
                line = f.readline().strip()
                if not line:
                    return None, "Error: Incomplete hospital preferences"
                try:
                    # Convert the preferences into integers
                    prefs = [int(x) - 1 for x in line.split()]
                except ValueError:
                    return None, f"Error: None-integer at line {i +2}"
                # make sure there are exactly n entries with no duplicates
                if len(prefs) != n or set(prefs) != set(range(n)):
                    return None
                hospital_prefs.append(prefs)
            
            #read the student preferences
            student_prefs = []
            for i in range(n):
                line = f.readline().strip()
                if not line:
                    return None, "Error: Incomplete student preferences"
                
                try:
                    prefs = [int(x) - 1 for x in line.split()]
                except ValueError:
                    return None
                if len(prefs) != n or set(prefs) != set(range(n)):
                    return None
                
                student_prefs.append(prefs)
            return (n, hospital_prefs, student_prefs), None
    # Handles missing file
    except FileNotFoundError:
        return None, "Error: Cannot open input file"

def checkMatched(matchFile, n):
    return

def checkStability():
    return

def main():
    input_file = input("Enter the input file: ")
