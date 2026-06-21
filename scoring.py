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

def skill_score(skill_text):
    score = 0

    for skill in AI_SKILLS:
        if skill.lower() in skill_text.lower():
            score += 10

    return min(score, 100)


def experience_score(exp):
    if 5 <= exp <= 9:
        return 100
    elif 3 <= exp < 5:
        return 80
    elif 9 < exp <= 12:
        return 80
    else:
        return 50


def recruiter_score(response, completion, github):
    return (
        response * 40 +
        completion * 40 +
        github * 2
    )