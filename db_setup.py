# db_setup.py
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["smart_quiz_db"]

questions_col = db["questions"]
results_col   = db["results"]

print("✅ Connected to MongoDB successfully!")

questions_col.delete_many({})
print("🗑️  Old questions cleared.")

questions = [

    # ── SCIENCE (10 questions) ────────────────────────────────────────────

    {
        "stream": "Science",
        "question": "What is the chemical formula for water?",
        "options": ["H2O", "CO2", "NaCl", "O2"],
        "answer": "H2O",
        "marks": 1
    },
    {
        "stream": "Science",
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars",
        "marks": 1
    },
    {
        "stream": "Science",
        "question": "What is the powerhouse of the cell?",
        "options": ["Nucleus", "Ribosome", "Mitochondria", "Vacuole"],
        "answer": "Mitochondria",
        "marks": 1
    },
    {
        "stream": "Science",
        "question": "What is Newton's second law of motion?",
        "options": ["F = ma", "E = mc2", "V = IR", "P = mv"],
        "answer": "F = ma",
        "marks": 2
    },
    {
        "stream": "Science",
        "question": "Which part of the cell contains genetic information?",
        "options": ["Mitochondria", "Nucleus", "Ribosome", "Cell membrane"],
        "answer": "Nucleus",
        "marks": 2
    },
    {
        "stream": "Science",
        "question": "What is the atomic number of Carbon?",
        "options": ["6", "8", "12", "14"],
        "answer": "6",
        "marks": 2
    },
    {
        "stream": "Science",
        "question": "Which gas do plants absorb during photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Carbon Dioxide",
        "marks": 2
    },
    {
        "stream": "Science",
        "question": "What is the speed of light in vacuum (approx)?",
        "options": ["3x10^8 m/s", "3x10^6 m/s", "3x10^10 m/s", "3x10^5 m/s"],
        "answer": "3x10^8 m/s",
        "marks": 3
    },
    {
        "stream": "Science",
        "question": "Which law states that energy can neither be created nor destroyed?",
        "options": ["Newton's First Law", "Law of Conservation of Energy",
                    "Ohm's Law", "Boyle's Law"],
        "answer": "Law of Conservation of Energy",
        "marks": 3
    },
    {
        "stream": "Science",
        "question": "What is the SI unit of electric resistance?",
        "options": ["Ampere", "Volt", "Ohm", "Watt"],
        "answer": "Ohm",
        "marks": 3
    },

    # ── COMMERCE (10 questions) ───────────────────────────────────────────

    {
        "stream": "Commerce",
        "question": "What does GDP stand for?",
        "options": ["Gross Domestic Product", "General Data Protocol",
                    "Global Development Plan", "Gross Demand Price"],
        "answer": "Gross Domestic Product",
        "marks": 1
    },
    {
        "stream": "Commerce",
        "question": "Which financial statement shows profit or loss?",
        "options": ["Balance Sheet", "Income Statement",
                    "Cash Flow Statement", "Trial Balance"],
        "answer": "Income Statement",
        "marks": 1
    },
    {
        "stream": "Commerce",
        "question": "What does ATM stand for in banking?",
        "options": ["Automated Teller Machine", "Automatic Transfer Mode",
                    "Authorized Transaction Method", "Annual Transfer Money"],
        "answer": "Automated Teller Machine",
        "marks": 1
    },
    {
        "stream": "Commerce",
        "question": "What is the full form of GST?",
        "options": ["General Sales Tax", "Goods and Services Tax",
                    "Government Service Tax", "Global Supply Tax"],
        "answer": "Goods and Services Tax",
        "marks": 2
    },
    {
        "stream": "Commerce",
        "question": "Which market structure has only one seller?",
        "options": ["Oligopoly", "Perfect Competition", "Monopoly", "Duopoly"],
        "answer": "Monopoly",
        "marks": 2
    },
    {
        "stream": "Commerce",
        "question": "What is the full form of EMI?",
        "options": ["Equated Monthly Installment", "Equal Money Index",
                    "Electronic Money Interface", "Extra Monthly Income"],
        "answer": "Equated Monthly Installment",
        "marks": 2
    },
    {
        "stream": "Commerce",
        "question": "Which of these is a direct tax?",
        "options": ["GST", "VAT", "Income Tax", "Excise Duty"],
        "answer": "Income Tax",
        "marks": 2
    },
    {
        "stream": "Commerce",
        "question": "What does the Sensex measure?",
        "options": ["GDP of India", "Performance of 30 BSE stocks",
                    "India's export value", "Inflation rate"],
        "answer": "Performance of 30 BSE stocks",
        "marks": 3
    },
    {
        "stream": "Commerce",
        "question": "What is 'depreciation' in accounting?",
        "options": ["Increase in asset value", "Reduction in asset value over time",
                    "Monthly business expense", "Tax on profit"],
        "answer": "Reduction in asset value over time",
        "marks": 3
    },
    {
        "stream": "Commerce",
        "question": "Which organization regulates the stock market in India?",
        "options": ["RBI", "SEBI", "NABARD", "SIDBI"],
        "answer": "SEBI",
        "marks": 3
    },

    # ── HUMANITIES (10 questions) ─────────────────────────────────────────

    {
        "stream": "Humanities",
        "question": "Who wrote the Indian national anthem?",
        "options": ["Rabindranath Tagore", "Bankim Chandra",
                    "Mahatma Gandhi", "Jawaharlal Nehru"],
        "answer": "Rabindranath Tagore",
        "marks": 1
    },
    {
        "stream": "Humanities",
        "question": "In which year did India gain independence?",
        "options": ["1945", "1947", "1950", "1942"],
        "answer": "1947",
        "marks": 1
    },
    {
        "stream": "Humanities",
        "question": "Who is known as the Father of the Indian Constitution?",
        "options": ["Mahatma Gandhi", "Jawaharlal Nehru",
                    "B.R. Ambedkar", "Sardar Patel"],
        "answer": "B.R. Ambedkar",
        "marks": 1
    },
    {
        "stream": "Humanities",
        "question": "What is the study of human societies and cultures called?",
        "options": ["Psychology", "Anthropology", "Sociology", "Philosophy"],
        "answer": "Anthropology",
        "marks": 2
    },
    {
        "stream": "Humanities",
        "question": "Who proposed the theory of social contract?",
        "options": ["Marx", "Locke", "Freud", "Darwin"],
        "answer": "Locke",
        "marks": 2
    },
    {
        "stream": "Humanities",
        "question": "Which article of the Indian Constitution abolishes untouchability?",
        "options": ["Article 14", "Article 17", "Article 21", "Article 32"],
        "answer": "Article 17",
        "marks": 2
    },
    {
        "stream": "Humanities",
        "question": "The Renaissance movement originated in which country?",
        "options": ["France", "England", "Italy", "Germany"],
        "answer": "Italy",
        "marks": 2
    },
    {
        "stream": "Humanities",
        "question": "Which of these is a fundamental right in India?",
        "options": ["Right to Property", "Right to Education",
                    "Right to Job", "Right to Vote"],
        "answer": "Right to Education",
        "marks": 3
    },
    {
        "stream": "Humanities",
        "question": "Who wrote 'The Republic'?",
        "options": ["Aristotle", "Socrates", "Plato", "Kant"],
        "answer": "Plato",
        "marks": 3
    },
    {
        "stream": "Humanities",
        "question": "What does the term 'Secularism' mean in the Indian context?",
        "options": ["State has its own religion", "State treats all religions equally",
                    "Religion is banned", "Only Hinduism is recognized"],
        "answer": "State treats all religions equally",
        "marks": 3
    },
]

# Insert into MongoDB
questions_col.insert_many(questions)
print(f"✅ {len(questions)} questions inserted into MongoDB!")

# Verify
print("\n📋 Questions stored in DB:\n")
for q in questions_col.find({}, {"_id": 0, "question": 1, "stream": 1, "marks": 1}):
    print(f"  [{q['stream']}] (Marks: {q['marks']}) {q['question']}")

client.close()
print("\n🔒 MongoDB connection closed.")
