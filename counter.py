import sys

DEFAULT = 100
has_args = len(sys.argv) > 1
total = int(sys.argv[1]) if has_args else DEFAULT

print("=" * 40)
print("🚀 JOB STARTING")
print(f"   Default total : {DEFAULT}")
print(f"   Args provided : {'YES 🎛️' if has_args else 'NO 😴'}")
print(f"   Total to use  : {total} {'(overridden!)' if has_args else '(using default)'}")
print("=" * 40)
print()

jokes = [
    "still waking up ☕",
    "finding my keys 🔑",
    "questioning my life choices 🤔",
    "pretending to be busy 💼",
    "totally not slacking 🦥",
    "peak performance 💪",
    "on a roll! 🎲",
    "vibing hard 🎧",
    "no thoughts, just counting 🧠",
    "almost forgot what I was doing 😵",
]

for i in range(1, total + 1):
    joke = jokes[(i - 1) % len(jokes)]
    print(f"{i} — {joke}")
