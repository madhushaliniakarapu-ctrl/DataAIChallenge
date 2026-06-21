import json
from pprint import pprint

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    candidate = json.loads(next(f))

print("\nPROFILE")
pprint(candidate["profile"])

print("\nCAREER HISTORY")
pprint(candidate["career_history"][:2])

print("\nEDUCATION")
pprint(candidate["education"][:2])

print("\nSKILLS")
pprint(candidate["skills"][:10])

print("\nREDROB SIGNALS")
pprint(candidate["redrob_signals"])