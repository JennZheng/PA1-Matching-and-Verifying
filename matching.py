def matching(n, hospitals, students):
    # Base case
    if n == 0:
        return []

    # Build ranking tables
    student_rank = [[0] * n for _ in range(n)]
    for s in range(n):
        for rank, h in enumerate(students[s]):
            student_rank[s][h] = rank


    return hospital_match

# Main Function
def main():
    # Read input 
    data = sys.stdin.read().strip().split()

    # Base Case
    if not data:
        return

    # 0 based index
    idx = 0
    n = int(data[idx])
    idx += 1


if __name__ == "__main__":
    main()
