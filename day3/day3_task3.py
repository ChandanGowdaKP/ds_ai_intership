# Screen resolution setting (immutable)
screen_res = (1920, 1080)

# Print current resolution
print(f"Current Resolution: {screen_res[0]}x{screen_res[1]}")

# ❌ Experiment: This line will cause a TypeError
#screen_res[0] = 1280

# ✅ Fix: Explain immutability
print("Tuples cannot be modified!")
