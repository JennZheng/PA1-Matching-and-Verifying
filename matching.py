# Necessary imports
import sys

# Matching algorithm
# Inputs are number of hospitals and students and each with a list of preferences
def matching(n, hospitals, students):
    
    # Base Case
    if n == 0:
        return []

    # Compute how students rank each hospital
    student_rank = [[0] * n for _ in range(n)]
    for s in range(n):
        for rank, h in enumerate(students[s]):
            student_rank[s][h] = rank

    # Keep track of which index in preference list for each hospital
    next = [0] * n

    # Matches
    hospital_match = [-1] * n 
    student_match = [-1] * n

    # Start with all hospitals free and seek a match
    free = list(range(n))

    # Loop through until all hospitals propose
    while free:
        # Remove once proposed
        h = free.pop()
        
        # Hospital cannot be matches if it approached everyone
        if next[h] >= n:
            continue

        # h proposes to next student on its list
        s = hospitals[h][next[h]]
        next[h] += 1

        # If student is free, accept
        current = student_match[s]
        if current== -1:
            student_match[s] = h
            hospital_match[h] = s
        else:
            # If student has a tentative match
            if student_rank[s][h] < student_rank[s][current]:
                # Based on the preference, make a decision
                student_match[s] = h
                hospital_match[h] = s
                hospital_match[current] = -1
                
                # The rejected hospital is free 
                if next[current] < n:
                    free.append(current)
            else:
                # IF current is preferred, reject
                if next[h] < n:
                    free.append(h)

    return hospital_match


def read_input():
   # Read input 
    data = sys.stdin.read().strip().split()
    
    # Base Case
    if not data:
        return

    # 0 based index
    idx = 0

    try:
        n = int(data[idx])
        idx += 1
    except (ValueError, IndexError):
        return None
    
    if n < 0:
        return None
    
    if n == 0:
        return (0, [], [])
    
    # Read each hospital preferences
    hospitals = []
    for _ in range(n):
        if idx + n > len(data):
            return None
        prefs = [int(x) - 1 for x in data[idx:idx + n]]
        idx += n
        # Validate
        if sorted(prefs) != list(range(n)):
            return None
        hospitals.append(prefs)
    
    # Read student preferences
    students = []
    for _ in range(n):
        if idx + n > len(data):
            return None
        prefs = [int(x) - 1 for x in data[idx:idx + n]]
        idx += n
        # Validate
        if sorted(prefs) != list(range(n)):
            return None
        students.append(prefs)
    
    return (n, hospitals, students)


def main():
    result = read_input()
    
    if result is None:
        return
    
    n, hospitals, students = result
    
    if n == 0:
        return
    
    hospital_match = matching(n, hospitals, students)
    
    for h in range(n):
        s = hospital_match[h]
        print(f"{h + 1} {s + 1}")


if __name__ == "__main__":
    main()
