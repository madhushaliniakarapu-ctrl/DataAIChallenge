import json
import pandas as pd

rows = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        c = json.loads(line)

        skills = [
            skill["name"]
            for skill in c["skills"]
        ]

        rows.append({
            "candidate_id": c["candidate_id"],
            "headline": c["profile"]["headline"],
            "summary": c["profile"]["summary"],
            "current_title": c["profile"]["current_title"],
            "experience": c["profile"]["years_of_experience"],
            "skills": ", ".join(skills),

            "github_score":
            c["redrob_signals"]["github_activity_score"],

            "recruiter_response":
            c["redrob_signals"]["recruiter_response_rate"],

            "completion_rate":
            c["redrob_signals"]["interview_completion_rate"]
        })

df = pd.DataFrame(rows)

print(df.head())

print("\nShape:")
print(df.shape)