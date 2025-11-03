import pandas as pd
import os

# Load the data from the CSV file
model_data = pd.read_csv("data/keywords_final.csv")

# Sort by Rating (descending) and PublishYear (descending)
rating_ranking = model_data[['Name', 'Rating', 'Id']].sort_values(by='Rating', ascending=False)
publish_year_ranking = model_data[['Name', 'PublishYear', 'Id']].sort_values(by='PublishYear', ascending=False)

# Create the HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Rankings</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #333; }}
        .rankings {{ display: flex; justify-content: space-between; }}
        .ranking {{ width: 45%; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>Book Rankings</h1>

    <div class="rankings">
        <div class="ranking">
            <h2>Rating Ranking</h2>
            <table>
                <tr>
                    <th>Book Name</th>
                    <th>Rating</th>
                </tr>
"""

# Add Rating Ranking data to HTML with hyperlinks
for index, row in rating_ranking.iterrows():
    book_link = f'<a href="page/{row["Id"]}.html">{row["Name"]}</a>'
    html_content += f"""
                <tr>
                    <td>{book_link}</td>
                    <td>{row['Rating']}</td>
                </tr>
"""

html_content += """
            </table>
        </div>

        <div class="ranking">
            <h2>Publish Year Ranking</h2>
            <table>
                <tr>
                    <th>Book Name</th>
                    <th>Publish Year</th>
                </tr>
"""

# Add Publish Year Ranking data to HTML with hyperlinks
for index, row in publish_year_ranking.iterrows():
    book_link = f'<a href="page/{row["Id"]}.html">{row["Name"]}</a>'
    html_content += f"""
                <tr>
                    <td>{book_link}</td>
                    <td>{row['PublishYear']}</td>
                </tr>
"""

html_content += """
            </table>
        </div>
    </div>
</body>
</html>
"""

# Save the HTML content to a file
output_file_path = "index.html"
with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"Generated main page: {output_file_path}")