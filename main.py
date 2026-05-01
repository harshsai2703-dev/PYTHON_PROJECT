import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from pymongo import MongoClient
import random

client = MongoClient("mongodb://localhost:27017/")
db = client["smart_quiz_db"]
questions_col = db["questions"]
results_col   = db["results"]

TIPS = {
    "Science":    [(80,"Pursue Engineering or Medicine."),(60,"Try BSc, Pharmacy or Biotech."),(40,"Explore IT or Agriculture."),(0,"Build your Science basics first.")],
    "Commerce":   [(80,"Aim for CA, MBA or Economics."),(60,"Try BBA, Banking or Analytics."),(40,"Explore B.Com or Insurance."),(0,"Strengthen Accounts & Economics.")],
    "Humanities": [(80,"Consider UPSC, Law or Journalism."),(60,"Try Psychology or Social Work."),(40,"Try Hotel Mgmt or Mass Comm."),(0,"Build reading & general knowledge.")],
}

def get_tip(stream, pct):
    for cutoff, tip in TIPS[stream]:
        if pct >= cutoff:
            return tip

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Quiz & Career Analyzer")
        self.geometry("600x500")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")
        self.name    = tk.StringVar()
        self.stream  = tk.StringVar(value="Science")
        self.selected = tk.StringVar()
        self.questions, self.index, self.score, self.total_marks = [], 0, 0, 0
        self.show_login()

    def clear(self):
        for w in self.winfo_children():
            w.destroy()

    def show_login(self):
        self.clear()
        tk.Label(self, text="Smart Quiz & Career Analyzer", font=("Helvetica", 17, "bold"), bg="#f0f0f0").pack(pady=(30, 4))
        tk.Label(self, text="Test your knowledge. Find your career path.", font=("Helvetica", 10), bg="#f0f0f0", fg="gray").pack()

        form = tk.Frame(self, bg="white", padx=30, pady=20, relief="groove", bd=1)
        form.pack(pady=20, ipadx=10)

        tk.Label(form, text="Your Name", font=("Helvetica", 11, "bold"), bg="white").grid(row=0, column=0, sticky="w")
        e = tk.Entry(form, textvariable=self.name, font=("Helvetica", 11), width=26, relief="solid", bd=1)
        e.grid(row=1, column=0, ipady=5, pady=(4, 14))
        e.focus()

        tk.Label(form, text="Select Stream", font=("Helvetica", 11, "bold"), bg="white").grid(row=2, column=0, sticky="w")
        f = tk.Frame(form, bg="white")
        f.grid(row=3, column=0, sticky="w", pady=(4, 18))
        for s in ["Science", "Commerce", "Humanities"]:
            tk.Radiobutton(f, text=s, variable=self.stream, value=s, font=("Helvetica", 11), bg="white").pack(side="left", padx=6)

        bf = tk.Frame(form, bg="white")
        bf.grid(row=4, column=0)
        tk.Button(bf, text="Start Quiz", font=("Helvetica", 12, "bold"), bg="#4a90e2", fg="white",
                  relief="flat", padx=18, pady=7, cursor="hand2", command=self.start).pack(side="left", padx=(0, 10))
        tk.Button(bf, text="Leaderboard", font=("Helvetica", 12, "bold"), bg="#888", fg="white",
                  relief="flat", padx=14, pady=7, cursor="hand2", command=self.show_leaderboard).pack(side="left")

    def start(self):
        if len(self.name.get().strip()) < 2:
            messagebox.showwarning("Name Required", "Enter your name (at least 2 characters).")
            return
        qs = list(questions_col.find({"stream": self.stream.get()}, {"_id": 0}))
        if not qs:
            messagebox.showerror("No Questions", "Run db_setup.py first.")
            return
        self.questions   = random.sample(qs, min(10, len(qs)))
        self.index       = 0
        self.score       = 0
        self.total_marks = sum(q["marks"] for q in self.questions)
        self.show_question()

    def show_question(self):
        self.clear()
        q, num, total = self.questions[self.index], self.index + 1, len(self.questions)

        c = tk.Canvas(self, width=560, height=7, bg="#ddd", bd=0, highlightthickness=0)
        c.pack(pady=(18, 4))
        c.create_rectangle(0, 0, int((num / total) * 560), 7, fill="#4a90e2", outline="")

        tk.Label(self, text=f"Q{num} of {total}  |  {self.stream.get()}  |  {q['marks']} mark(s)",
                 font=("Helvetica", 9), fg="gray", bg="#f0f0f0").pack()
        tk.Label(self, text=q["question"], font=("Helvetica", 13, "bold"),
                 bg="#f0f0f0", wraplength=540, justify="left").pack(pady=(16, 10), padx=30, anchor="w")

        self.selected.set("")
        f = tk.Frame(self, bg="#f0f0f0")
        f.pack(padx=30, anchor="w")
        for opt in q["options"]:
            tk.Radiobutton(f, text=opt, variable=self.selected, value=opt,
                           font=("Helvetica", 11), bg="#f0f0f0", anchor="w").pack(fill="x", pady=3)

        tk.Button(self, text="Next ▶" if num < total else "Finish ✔",
                  font=("Helvetica", 12, "bold"), bg="#5cb85c", fg="white",
                  relief="flat", padx=18, pady=7, cursor="hand2",
                  command=self.submit).pack(pady=22)

    def submit(self):
        if not self.selected.get():
            messagebox.showwarning("No Answer", "Please select an option.")
            return
        q = self.questions[self.index]
        if self.selected.get() == q["answer"]:
            self.score += q["marks"]
        self.index += 1
        if self.index < len(self.questions):
            self.show_question()
        else:
            pct = round((self.score / self.total_marks) * 100, 2)
            results_col.insert_one({"name": self.name.get().strip(), "stream": self.stream.get(),
                                    "score": self.score, "total": self.total_marks, "percentage": pct})
            self.show_result()

    def show_result(self):
        self.clear()
        pct = round((self.score / self.total_marks) * 100, 2)

        tk.Label(self, text="Quiz Complete!", font=("Helvetica", 17, "bold"), bg="#f0f0f0").pack(pady=(25, 4))
        tk.Label(self, text=f"Well done, {self.name.get().strip()}!", font=("Helvetica", 11), fg="gray", bg="#f0f0f0").pack()

        card = tk.Frame(self, bg="white", padx=24, pady=14, relief="groove", bd=1)
        card.pack(pady=14, ipadx=10)
        for label, value, color in [
            ("Stream",     self.stream.get(),                    "black"),
            ("Score",      f"{self.score} / {self.total_marks}", "black"),
            ("Percentage", f"{pct}%",                            "#4a90e2"),
        ]:
            r = tk.Frame(card, bg="white")
            r.pack(fill="x", pady=2)
            tk.Label(r, text=label, font=("Helvetica", 10), bg="white", fg="gray", width=14, anchor="w").pack(side="left")
            tk.Label(r, text=value, font=("Helvetica", 10, "bold"), bg="white", fg=color).pack(side="left")

        tk.Label(self, text="Career Tip", font=("Helvetica", 11, "bold"), bg="#f0f0f0").pack(pady=(10, 2))
        tk.Label(self, text=get_tip(self.stream.get(), pct), font=("Helvetica", 10), bg="#f0f0f0", wraplength=520).pack()

        bf = tk.Frame(self, bg="#f0f0f0")
        bf.pack(pady=18)
        for txt, bg, cmd in [
            ("View Graph",   "#f0ad4e", self.show_graph),
            ("Leaderboard",  "#888",    self.show_leaderboard),
            ("Play Again",   "#4a90e2", self.show_login),
        ]:
            tk.Button(bf, text=txt, font=("Helvetica", 11, "bold"), bg=bg, fg="white",
                      relief="flat", padx=12, pady=6, cursor="hand2",
                      command=cmd).pack(side="left", padx=6)

    def show_leaderboard(self):
        self.clear()
        tk.Label(self, text="Leaderboard", font=("Helvetica", 17, "bold"), bg="#f0f0f0").pack(pady=(25, 4))
        tk.Label(self, text="All players ranked by percentage", font=("Helvetica", 10), fg="gray", bg="#f0f0f0").pack()

        all_results = list(results_col.find({}, {"_id": 0}).sort("percentage", -1))

        frame = tk.Frame(self, bg="white", relief="groove", bd=1)
        frame.pack(pady=16, padx=30, fill="x")

        medals = {0: "🥇", 1: "🥈", 2: "🥉"}

        header = tk.Frame(frame, bg="#4a90e2")
        header.pack(fill="x")
        for txt, w in [("Rank", 6), ("Name", 18), ("Stream", 12), ("Score", 10), ("%", 8)]:
            tk.Label(header, text=txt, font=("Helvetica", 10, "bold"), bg="#4a90e2", fg="white",
                     width=w, anchor="w").pack(side="left", padx=4, pady=6)

        if not all_results:
            tk.Label(frame, text="No results yet. Play the quiz first!",
                     font=("Helvetica", 10), bg="white", fg="gray").pack(pady=20)
        else:
            for i, r in enumerate(all_results):
                bg = "#f9f9f9" if i % 2 == 0 else "white"
                row = tk.Frame(frame, bg=bg)
                row.pack(fill="x")
                rank_txt = medals.get(i, str(i + 1))
                for txt, w in [
                    (rank_txt,              6),
                    (r["name"],            18),
                    (r["stream"],          12),
                    (f"{r['score']}/{r['total']}", 10),
                    (f"{r['percentage']}%", 8),
                ]:
                    tk.Label(row, text=txt, font=("Helvetica", 10), bg=bg,
                             width=w, anchor="w").pack(side="left", padx=4, pady=5)

        tk.Button(self, text="Back", font=("Helvetica", 11, "bold"), bg="#888", fg="white",
                  relief="flat", padx=16, pady=6, cursor="hand2",
                  command=self.show_login).pack(pady=10)

    def show_graph(self):
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(["Marks Earned", "Marks Missed"], [self.score, self.total_marks - self.score],
               color=["#5cb85c", "#d9534f"], width=0.4, edgecolor="none")
        for i, v in enumerate([self.score, self.total_marks - self.score]):
            ax.text(i, v + 0.15, str(v), ha="center", fontsize=11, fontweight="bold")
        ax.set_title(f"Result — {self.name.get().strip()}", fontsize=13)
        ax.set_ylabel("Marks")
        ax.set_ylim(0, self.total_marks + 3)
        ax.spines[["top", "right"]].set_visible(False)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    QuizApp().mainloop()
