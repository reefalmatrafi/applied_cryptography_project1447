import random
import json


class WeakPRNG:
    """
    Weak Random Number Generator.
    This version intentionally creates predictable values to demonstrate vulnerability.
    """

    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)

        self.generated_values = []
        self.current_value = 40000

    def generate_random_key_component(self, bit_length=16):
        """
        Generate a weak predictable key component.
        The value increases using a simple pattern instead of true randomness.
        """
        index = len(self.generated_values)
        value = self.current_value + 137 + (index % 5) * 11

        self.current_value = value
        self.generated_values.append(value)

        return value

    def generate_sequence(self, count=10, bit_length=16):
        sequence = []

        for _ in range(count):
            sequence.append(self.generate_random_key_component(bit_length))

        return sequence

    def get_history(self):
        return self.generated_values

    def save_sequence(self, filename="key_sequence.json"):
        data = {
            "sequence": self.generated_values,
            "count": len(self.generated_values)
        }

        with open(filename, "w") as f:
            json.dump(data, f)

        print(f"Sequence saved to {filename}")

    def load_sequence(self, filename="key_sequence.json"):
        with open(filename, "r") as f:
            data = json.load(f)

        self.generated_values = data["sequence"]
        return self.generated_values


if __name__ == "__main__":
    print("=" * 60)
    print("WEAK PRNG DEMONSTRATION")
    print("=" * 60)

    prng = WeakPRNG(seed=42)

    print("\n[*] Generating weak predictable sequence...")
    sequence = prng.generate_sequence(count=20, bit_length=16)

    print(f"\n[+] Generated {len(sequence)} weak key components:")
    print(sequence)

    print("\n[!] VULNERABILITY: The sequence follows a predictable pattern.")

    print("\n[✓] An attacker or AI model can learn this pattern and predict future values.")

    prng.save_sequence("key_sequence.json")
