import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create figure
fig, ax = plt.subplots(figsize=(12, 8))

# Title
ax.set_title("College Exam Portal – Role-Based Flow", fontsize=16, fontweight="bold")

# Hide axes
ax.axis("off")

# Define positions for roles
positions = {
    "HOD": (0.1, 0.7),
    "Faculty": (0.1, 0.4),
    "Student": (0.1, 0.1),
    "User Management": (0.5, 0.8),
    "Exam Management": (0.5, 0.6),
    "Materials Management": (0.5, 0.4),
    "News & Announcements": (0.5, 0.2),
    "Reports": (0.8, 0.7),
    "Quiz Attempt": (0.8, 0.4),
    "View Results": (0.8, 0.2)
}

# Draw role boxes
role_boxes = ["HOD", "Faculty", "Student"]
for role in role_boxes:
    x, y = positions[role]
    ax.add_patch(mpatches.FancyBboxPatch((x, y), 0.15, 0.1, boxstyle="round,pad=0.05", 
                                         edgecolor="black", facecolor="#ffcccb"))
    ax.text(x + 0.075, y + 0.05, role, ha="center", va="center", fontsize=12, fontweight="bold")

# Draw feature boxes
features = [k for k in positions.keys() if k not in role_boxes]
for feat in features:
    x, y = positions[feat]
    ax.add_patch(mpatches.FancyBboxPatch((x, y), 0.2, 0.1, boxstyle="round,pad=0.05", 
                                         edgecolor="black", facecolor="#cce5ff"))
    ax.text(x + 0.1, y + 0.05, feat, ha="center", va="center", fontsize=11)

# Arrows mapping roles to features
connections = [
    ("HOD", "User Management"),
    ("HOD", "Exam Management"),
    ("HOD", "Materials Management"),
    ("HOD", "News & Announcements"),
    ("HOD", "Reports"),
    ("Faculty", "Exam Management"),
    ("Faculty", "Materials Management"),
    ("Faculty", "News & Announcements"),
    ("Faculty", "View Results"),
    ("Student", "Quiz Attempt"),
    ("Student", "View Results"),
    ("Student", "Materials Management"),
    ("Student", "News & Announcements")
]

for start, end in connections:
    x1, y1 = positions[start]
    x2, y2 = positions[end]
    ax.annotate("", xy=(x2, y2+0.05), xytext=(x1+0.15, y1+0.05),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="black"))

plt.show()
