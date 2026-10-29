# ===========================================
#errors.py --- "Break on purpose."

# ---- Warm-Up: a program that works ----
# print("Hello, World!")

# ---- Experiment 1: SYNTAX ERROR (translation-time) ----
# print("Hello, World!)

# ---- Experiment 2: SYNTAX ERROR ----
# print(Hello, World!)

# ---- Experiment 3: NAME ERROR ----
# Print("Hello, World!")

# ---- Experiment 4: INDENTATION ERROR ----
# print("Hello")
#    print("World!")

# ---- Experiment 5: Logic Error (ZeroDivisionError) ----
# print("About to divide")
# print(1 / 0)

# ---- Experiment 6: Logic Error with numbers ----
# We want the AVERAGE of three test scores.
# Expected: (90 + 80 + 70) / 3 = 80.0
score1 = 90
score2 = 80
score3 = 70

average = (score1 + score2 + score3) / 3

print("Average: ", average)