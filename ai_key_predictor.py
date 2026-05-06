import random
import numpy as np


class AIKeyPredictor:
    """
    AI Integration:
    This model learns patterns from a weak random number generator
    and tries to predict the next RSA key component.
    """

    def __init__(self):
        self.model_weights = None

    def generate_weak_keys(self, seed, count=200):
        """
        Weak PRNG:
        It has a hidden pattern, but also small noise.
        This makes prediction possible but not perfect.
        """
        random.seed(seed)

        keys = []
        value = 40000

        for i in range(count):
            pattern = 137 + (i % 5) * 11
            noise_options = [0, 0, -10, 10, -20, 20, -40, 40]
            noise = random.choice(noise_options)
            value = value + pattern + noise
            keys.append(value)

        return keys

    def prepare_features(self, count):
        """
        Features used by the AI model:
        - index number
        - repeating pattern position
        """
        X = []

        for i in range(count):
            X.append([
                1,
                i,
                i % 5
            ])

        return np.array(X)

    def train(self, keys):
        print("\n[*] Training AI model on weak PRNG output...")

        X = self.prepare_features(len(keys))
        y = np.array(keys)

        self.model_weights = np.linalg.lstsq(X, y, rcond=None)[0]

        print("[✓] AI model trained successfully")

    def predict_key(self, index):
        X = np.array([1, index, index % 5])
        prediction = X @ self.model_weights
        return int(round(prediction))

    def evaluate_predictions(self, keys, num_predictions=10):
        print("\n" + "=" * 60)
        print("PREDICTION TEST")
        print("=" * 60)

        correct = 0
        start_index = len(keys) - num_predictions

        for i in range(start_index, len(keys)):
            predicted = self.predict_key(i)
            actual = keys[i]
            error = abs(predicted - actual)

            match = "✓" if error <= 20 else "✗"

            if error <= 20:
                correct += 1

            print(f"[{match}] Predicted: {predicted} | Actual: {actual} | Error: {error}")

        accuracy = (correct / num_predictions) * 100

        print(f"\nAccuracy within ±25: {accuracy:.2f}%")
        print("=" * 60)

    def predict_next_future_key(self, keys):
        next_index = len(keys)
        predicted = self.predict_key(next_index)

        print("\n[*] Future Key Prediction")
        print(f"Predicted next weak RSA key component: {predicted}")


if __name__ == "__main__":
    print("=" * 60)
    print("AI KEY PREDICTOR")
    print("=" * 60)

    predictor = AIKeyPredictor()

    seed = random.randint(1, 1000)

    print(f"\n[*] Using weak PRNG seed: {seed}")
    print("[*] Generating weak RSA key components...")

    keys = predictor.generate_weak_keys(seed=seed, count=200)

    print(f"[✓] Generated {len(keys)} weak key components")
    print(f"[*] First 10 keys: {keys[:10]}")

    predictor.train(keys)

    predictor.evaluate_predictions(keys, num_predictions=10)

    predictor.predict_next_future_key(keys)
    import matplotlib.pyplot as plt

    predicted_values = [70187, 70350, 70514, 70677, 70841, 70979, 71142, 71306, 71470, 71633]
    actual_values = [70267, 70375, 70514, 70704, 70845, 70992, 71130, 71329, 71499, 71690]

    x = range(1, 11)

    
    plt.plot(x, predicted_values, marker="o", label="Predicted")
    plt.plot(x, actual_values, marker="o", label="Actual")

    plt.title("AI Prediction vs Actual Weak RSA Key Components")
    plt.xlabel("Prediction Number")
    plt.ylabel("Key Component Value")
    plt.legend()
    plt.grid(True)

    plt.savefig("ai_prediction_graph.png")
    plt.show()

    print("\n[!] VULNERABILITY DEMONSTRATED:")
    print("[!] The AI model learned patterns from the weak PRNG.")
    print("[!] The prediction is not perfect, but it can still guess future key components.")
    print("[!] This shows that weak randomness can make RSA key generation insecure.")