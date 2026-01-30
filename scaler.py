import time
import random
import os
import subprocess
import csv
import matplotlib.pyplot as plt

# this is for task C
def generatePrefList(n):
    prefs = list(range(1, n+1))
    random.shuffle(prefs)
    return prefs

def generateInstance(n, path):
    with open(path, "w") as f:
        # write n
        f.write(str(n) + "\n")
    
        # Hospital preference
        for _ in range(n):
            prefs = generatePrefList(n)
            f.write(" ".join(map(str, prefs)) + "\n")
    
        # Student preference
        for _ in range(n):
            prefs = generatePrefList(n)
            f.write(" ".join(map(str, prefs)) + "\n")

if __name__ == "__main__":
    if not os.path.exists("test"):
        os.makedirs("test")

    ns = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    
    matcher_times = []
    verifier_times = []

    for n in ns:
        in_files = f"test/n{n}.in"
        out_files = f"test/n{n}.out"

        generateInstance(n, in_files)

        # Time the matching enginer
        start = time.perf_counter()
        with open(in_files) as f_in, open(out_files, "w") as f_out:
            subprocess.run(["python", "matching.py"], stdin=f_in, stdout=f_out)
        matcher_times.append((n, time.perf_counter() - start))

        # Time the verfier
        start = time.perf_counter()
        subprocess.run(["python", "verifier.py"], input=f"{in_files}\n{out_files}\n", text=True)
        verifier_times.append((n, time.perf_counter() - start))
    
    # Write the time results to the results file
    if not os.path.exists("results"):
        os.makedirs("results")

    with open("results/matcher_times.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "time_seconds"])
        writer.writerows(matcher_times)
    
    with open("results/verifier_times.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "time_seconds"])
        writer.writerows(verifier_times)
    
    print("\n Time results are saved in results file")
    
    # Create the graph
    ns_matcher = [x[0] for x in matcher_times]
    times_matcher = [x[1] for x in matcher_times]

    ns_verifier = [x[0] for x in verifier_times]
    times_verifier = [x[1] for x in verifier_times]

    plt.figure()
    plt.plot(ns_matcher, times_matcher, marker='o', label="Matcher")
    plt.plot(ns_verifier, times_verifier, marker='o', label="Verifier")

    plt.xlabel("n (number of hospitals/students)")
    plt.ylabel("Time (seconds)")
    plt.title("Gale-Shapley Scalability")
    plt.grid(True)
    plt.savefig("results/scalability.png")
    print("Graph is saved in results file")
    plt.show()