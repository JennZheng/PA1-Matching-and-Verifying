def matching(n, hospital_prefs, student_prefs):
    
    # Base Case
    if n == 0:
        return []

    # Compute student rankings
    student_rank = [[0] * n for _ in range(n)]
    for s in range(n):
        for rank, h in enumerate(student_prefs[s]):
            student_rank[s][h] = rank

    # Track next hospital to propose to each student
    next_proposal_index = [0] * n

    # Place to hold index
    hospital_match = [-1] * n 
    student_match = [-1] * n

    # Start with all hospitals free
    free_hospitals = list(range(n))

    while free_hospitals:
        h = free_hospitals.pop()
        
        # Skip if h has exhausted all proposals
        if next_proposal_index[h] >= n:
            continue

        # h proposes to next student on its list
        s = hospital_prefs[h][next_proposal_index[h]]
        next_proposal_index[h] += 1

        current_h = student_match[s]

        if current_h == -1:
            # Student s is free: accept h
            student_match[s] = h
            hospital_match[h] = s
        else:
            # s is tentatively matched; decide: h or current_h?
            if student_rank[s][h] < student_rank[s][current_h]:
                # s prefers h: accept and reject current_h
                student_match[s] = h
                hospital_match[h] = s
                hospital_match[current_h] = -1
                
                # current_h becomes free again
                if next_proposal_index[current_h] < n:
                    free_hospitals.append(current_h)
            else:
                # s prefers current_h: reject h
                if next_proposal_index[h] < n:
                    free_hospitals.append(h)

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
    
    # Read hospital preferences
    hospital_prefs = []
    for _ in range(n):
        if idx + n > len(data):
            return None
        prefs = [int(x) - 1 for x in data[idx:idx + n]]
        idx += n
        # Validate permutation
        if sorted(prefs) != list(range(n)):
            return None
        hospital_prefs.append(prefs)
    
    # Read student preferences
    student_prefs = []
    for _ in range(n):
        if idx + n > len(data):
            return None
        prefs = [int(x) - 1 for x in data[idx:idx + n]]
        idx += n
        # Validate permutation
        if sorted(prefs) != list(range(n)):
            return None
        student_prefs.append(prefs)
    
    return (n, hospital_prefs, student_prefs)


def main():
    result = read_input()
    
    if result is None:
        return
    
    n, hospital_prefs, student_prefs = result
    
    if n == 0:
        return
    
    hospital_match = matching(n, hospital_prefs, student_prefs)
    
    # Output: 1-based indices
    for h in range(n):
        s = hospital_match[h]
        print(f"{h + 1} {s + 1}")


if __name__ == "__main__":
    main()
