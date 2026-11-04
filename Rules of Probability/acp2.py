# ================================
# CLUB DAY PROBABILITY CHECKER
# ================================

# ---------- SETUP ----------
all_students = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
chess = {1, 2, 3, 4}
robotics = {3, 4, 5, 6, 7}
drama = {8, 9, 10}

# ---------- PART 1: union and intersection ----------
print("PART 1: Union and intersection")
in_either = chess.union(robotics)
in_both = chess.intersection(robotics)
print("Chess or robotics:", in_either)
print("Chess and robotics:", in_both)

# ---------- PART 2: the addition rule ----------
print("\nPART 2: Addition rule")
p_chess = len(chess) / len(all_students)
p_robotics = len(robotics) / len(all_students)
p_both = len(in_both) / len(all_students)
p_either = p_chess + p_robotics - p_both
print("P(chess or robotics) =", p_either)

p_counted = len(in_either) / len(all_students)
print("Counted from the union =", p_counted)
print("Match?", p_either == p_counted)

# ---------- PART 3: mutually exclusive events ----------
print("\nPART 3: Mutually exclusive events")
chess_and_drama = chess.intersection(drama)
print("Chess and drama:", chess_and_drama)

p_drama = len(drama) / len(all_students)
print("P(chess or drama) =", p_chess + p_drama)

# ---------- PART 4: independent or dependent ----------
print("\nPART 4: Independent or dependent")
winning = 2
total = 5

p_put_back = winning / total
print("Ticket put back:", p_put_back, "-> independent")

p_kept_out = (winning - 1) / (total - 1)
print("Ticket kept out, first was a win:", p_kept_out, "-> dependent")