import time
import math
import matplotlib.pyplot as plt


def factorize_bruteforce(n):
    """
    Factorize n using trial division.
    The loop tries divisors from 2 to sqrt(n).
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return None, None


def measure_average_attack_time(n, repetitions=1000):
    """
    Measure the average brute-force attack time.
    Repeating the test reduces random timing errors.
    """
    total_time = 0

    for _ in range(repetitions):
        start = time.perf_counter()
        p, q = factorize_bruteforce(n)
        end = time.perf_counter()

        total_time += end - start

    average_time = total_time / repetitions
    return p, q, average_time


print("=" * 70)
print("RSA BRUTE FORCE COMPLEXITY ANALYSIS")
print("=" * 70)

cases = [
    {"bits": 8, "p": 13, "q": 17},
    {"bits": 16, "p": 251, "q": 257},
    {"bits": 32, "p": 65521, "q": 65537},
]

results = []

for case in cases:
    bits = case["bits"]
    p_original = case["p"]
    q_original = case["q"]
    n = p_original * q_original

    print(f"\nTesting {bits}-bit RSA")
    print("-" * 70)
    print(f"Original p = {p_original}")
    print(f"Original q = {q_original}")
    print(f"n = p × q = {n}")

    recovered_p, recovered_q, avg_time = measure_average_attack_time(n)

    print(f"Recovered p = {recovered_p}")
    print(f"Recovered q = {recovered_q}")
    print(f"Average attack time = {avg_time:.10f} seconds")

    results.append({
        "bits": bits,
        "n": n,
        "p": recovered_p,
        "q": recovered_q,
        "time": avg_time
    })


print("\n" + "=" * 70)
print("SUMMARY TABLE")
print("=" * 70)
print(f"{'Key Size':<15}{'n':<20}{'Average Time (s)':<20}")
print("-" * 70)

for r in results:
    print(f"{r['bits']:<15}{r['n']:<20}{r['time']:<20.10f}")


# Graph
bits_list = [r["bits"] for r in results]
time_list = [r["time"] for r in results]

plt.figure()
plt.plot(bits_list, time_list, marker="o")
plt.title("RSA Brute Force Attack Time vs Key Size")
plt.xlabel("Key Size (bits)")
plt.ylabel("Average Attack Time (seconds)")
plt.grid(True)

plt.savefig("complexity_graph.png")
plt.show()

print("\nGraph saved as complexity_graph.png")