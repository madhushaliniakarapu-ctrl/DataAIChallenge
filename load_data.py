import json

count = 0

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        count += 1

print("Total Candidates:", count)

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    first_candidate = json.loads(next(f))

print("\nFirst Candidate Keys:")
print(first_candidate.keys())