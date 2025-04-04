#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

print("Content-Type: text/html\n")

items = [
    ("Cake", 20),
    ("Balloons", 21),
    ("Music System", 10),
    ("Lights", 5),
    ("Catering Service", 8),
    ("DJ", 3),
    ("Photo Booth", 15),
    ("Tables", 7),
    ("Chairs", 12),
    ("Drinks", 6),
    ("Party Hats", 9),
    ("Streamers", 18),
    ("Invitation Cards", 4),
    ("Party Games", 2),
    ("Cleaning Service", 11)
]

form = cgi.FieldStorage()
selected_indices = form.getlist("items")

selected_names = []
values = []

for idx in selected_indices:
    try:
        i = int(idx)
        selected_names.append(items[i][0])
        values.append(items[i][1])
    except (ValueError, IndexError):
        continue

if values:
    base_code = values[0]
    for val in values[1:]:
        base_code &= val

    message = ""
    final_code = base_code

    if base_code == 0:
        final_code += 5
        message = "Epic Party Incoming!"
    elif base_code > 5:
        final_code -= 2
        message = "Let's keep it classy!"
    else:
        message = "Chill vibes only!"
else:
    base_code = "N/A"
    final_code = "N/A"
    message = "No items selected."

print(f"""
<html>
<head><title>Digital Party Planner Result</title></head>
<body>
    <h1>🎉 Digital Party Planner 🎉</h1>
    <p><strong>Selected Items:</strong> {', '.join(selected_names)}</p>
    <p><strong>Final Party Code:</strong> {final_code}</p>
    <p><strong>Message:</strong> {message}</p>
    <br><a href="/party_form.php">Back to Form</a>
</body>
</html>
""")
