import json
import pandas as pd

AI_SKILLS = [
    "NLP",
    "Fine-tuning LLMs",
    "LoRA",
    "Transformers",
    "PyTorch",
    "TensorFlow",
    "Machine Learning",
    "Deep Learning",
    "LLM",
    "RAG",
    "Computer Vision",
    "Generative AI"
]

rows = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        c = json.loads(line)

        skills = ", ".join([s["name"] for s in c["skills"]])

        ai_skill_count = 0
        for skill in AI_SKILLS:
            if skill.lower() in skills.lower():
                ai_skill_count += 1

        experience = c["profile"]["years_of_experience"]
        response_rate = c["redrob_signals"]["recruiter_response_rate"]
        github_score = c["redrob_signals"]["github_activity_score"]

        score = (
            ai_skill_count * 10
            + experience * 2
            + response_rate * 20
            + github_score
        )

        reasoning = (
            f"{c['profile']['current_title']} with "
            f"{experience:.1f} yrs; "
            f"{ai_skill_count} AI core skills; "
            f"response rate {response_rate:.2f}"
        )

        rows.append({
            "candidate_id": c["candidate_id"],
            "score": round(score, 4),
            "reasoning": reasoning
        })

df = pd.DataFrame(rows)

df = df.sort_values(
    by=["score", "candidate_id"],
    ascending=[False, True]
)

df = df.head(100)

df["rank"] = range(1, 101)

df = df[
    [
        "candidate_id",
        "rank",
        "score",
        "reasoning"
    ]
]

df.to_csv(
    "output/ranked_candidates.csv",
    index=False
)

print("Submission file generated successfully!")
print(df.head())