# ------------------ Data Structures ------------------
from datetime import datetime

class JournalEntry:
    def __init__(self, date, text, mood_score, focus_score, energy_score):
        self.date = date
        self.text = text
        self.scores = [mood_score, focus_score, energy_score]  # Array
        
        self.next = None  # Linked list pointer

class Journal:
    def __init__(self):
        self.head = None
        self.tag_index = {}  # Hash table
        self.undo_stack = []  # Stack
        self.redo_stack = []  # Stack
        self.weekly_scores = [[0, 0, 0] for _ in range(7)]  # 2D array

    def add_entry(self, entry, day_index):
        # Linked list insertion
        entry.next = self.head
        self.head = entry

        # Update weekly scores
        self.weekly_scores[day_index] = entry.scores

       

        # Push to undo stack
        self.undo_stack.append(entry)
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            entry = self.undo_stack.pop()
            self.redo_stack.append(entry)
            self.head = entry.next
            print(f"Undo: Removed entry from {entry.date}")
        else:
            print("Undo stack is empty.")

    def redo(self):
        if self.redo_stack:
            entry = self.redo_stack.pop()
            self.add_entry(entry, 0)  # Re-add to day 0 for simplicity
            print(f"Redo: Re-added entry from {entry.date}")
        else:
            print("Redo stack is empty.")

    

    def display_weekly_scores(self):
        print("\n📊 Weekly Score Grid (Mood, Focus, Energy):")
        for i, scores in enumerate(self.weekly_scores):
            print(f"Day {i+1}: {scores}")

# ------------------ Sample Usage ------------------

journal = Journal()
today = datetime.now().strftime("%Y-%m-%d")

comment = input("How Was your Day? ")
# Add entries
entry1 = JournalEntry(f"{today}", comment , mood, focus, energy, ["#focus", "#work"])


journal.add_entry(entry1, 0)


journal.display_weekly_scores()

# Search by tag
results = journal.search_by_tag("#relax")
print("\n🔍 Entries with #relax:")
for e in results:
    print(f"{e.date}: {e.text}")

# Undo and Redo
journal.undo()
journal.redo()
