import json
import os
import random
from datetime import datetime

# TETSuper30 + PraxisUSA Auto Quiz Generator

QUIZ_TEMPLATES = {
    "tetsuper30": [
        {
            "subject": "Child Development & Pedagogy",
            "q": "According to Piaget, in which stage does abstract thinking develop?",
            "options": ["Sensorimotor", "Pre-operational", "Concrete Operational", "Formal Operational"],
            "answer": "Formal Operational",
            "explanation": "Formal Operational stage (11+ years) is where abstract and logical thinking develops."
        },
        {
            "subject": "EVS",
            "q": "Which gas is most abundant in Earth's atmosphere?",
            "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
            "answer": "Nitrogen",
            "explanation": "Nitrogen is ~78% of atmosphere."
        },
        {
            "subject": "Maths",
            "q": "What is the LCM of 12 and 18?",
            "options": ["36", "24", "18", "72"],
            "answer": "36",
            "explanation": "LCM of 12 and 18 is 36."
        }
    ],
    "praxisusa": [
        {
            "subject": "Praxis Core Reading",
            "q": "What is the main idea of a passage primarily determined by?",
            "options": ["First sentence only", "Supporting details and overall theme", "Last sentence", "Number of paragraphs"],
            "answer": "Supporting details and overall theme",
            "explanation": "Main idea is inferred from supporting details and theme."
        },
        {
            "subject": "Praxis Math",
            "q": "If 3x + 5 = 20, what is x?",
            "options": ["3", "5", "10", "15"],
            "answer": "5",
            "explanation": "3x = 15, so x = 5."
        }
    ]
}

def generate_daily_quiz():
    today = datetime.now().strftime("%Y-%m-%d")
    os.makedirs("quizzes/tetsuper30", exist_ok=True)
    os.makedirs("quizzes/praxisusa", exist_ok=True)

    for brand in ["tetsuper30", "praxisusa"]:
        questions = QUIZ_TEMPLATES[brand]
        random.shuffle(questions)
        quiz = {
            "brand": brand,
            "date": today,
            "title": f"{brand.upper()} Daily Quiz - {today}",
            "questions": questions[:5],
            "total_questions": len(questions[:5])
        }

        # Save JSON
        path = f"quizzes/{brand}/{today}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(quiz, f, indent=2, ensure_ascii=False)

        print(f"Generated: {path}")

    print("All quizzes generated successfully!")

if __name__ == "__main__":
    generate_daily_quiz()