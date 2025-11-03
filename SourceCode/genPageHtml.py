import pandas as pd
import os

# Load the data from the CSV file
model_data = pd.read_csv("data/keywords_last_with_renamed_images.csv")

model_data['html_path'] = ''
# Create the output directory if it doesn't exist
output_dir = "page"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate HTML files for each book
for index, row in model_data.iterrows():
    book_id = row['Id']
    name = row['Name']
    authors = row['Authors']
    publish_year = row['PublishYear']
    publisher = row['Publisher']
    description = row['Description']
    rating = row['Rating']
    recommended_ids = eval(row['recommended_ids'])  # Convert string representation of list to actual list
    image_path = f"../{row['image_path']}"

    # Create HTML content
    recommended_books = ''.join(
        [f'<div style="margin: 5px;">'
         f'<a href="{id}.html">'  # Add hyperlink here
         f'<img src="../cover/{id}.jpg" alt="Book Cover" style="width:100px;height:150px;margin:5px; border: 1px solid gray;">'
         f'</a>'
         f'<p>{model_data.loc[model_data["Id"] == id, "Name"].values[0]}</p>'
         f'</div>' for id in recommended_ids]
    )

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{name}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #333; }}
            .book-info {{ display: flex; align-items: flex-start; margin-bottom: 20px; }}
            .book-details {{ flex: 1; }}
            .book-cover {{ margin-left: 20px; }}
            .recommended {{ margin-top: 40px; }}
            .recommended img {{ width: 100px; height: 150px; border: 1px solid gray; margin: 5px; }}
        </style>
    </head>
    <body>
        <div class="book-info">
            <div class="book-details">
                <h1>{name}</h1>
                <p><strong>Authors:</strong> {authors}</p>
                <p><strong>Publish Year:</strong> {publish_year}</p>
                <p><strong>Publisher:</strong> {publisher}</p>
                <p><strong>Rating:</strong> {rating}</p>
                <p><strong>Description:</strong> {description}</p>
            </div>
            <div class="book-cover">
                <img src="{image_path}" alt="{name} Cover" style="width:200px;height:300px; border: 1px solid gray;">
            </div>
        </div>
        <div class="recommended">
            <h2>Recommended Books:</h2>
            {recommended_books}
        </div>
    </body>
    </html>
    """

    # Save the HTML content to a file
    html_file_path = os.path.join(output_dir, f"{book_id}.html")
    model_data.at[index, 'html_path'] = html_file_path
    with open(html_file_path, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"Generated HTML file: {html_file_path}")