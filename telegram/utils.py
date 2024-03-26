from datetime import datetime

def generate_html(meme_data):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Meme Data</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                padding: 20px;
            }}
            .container {{
                max-width: 800px;
                margin: auto;
            }}
            .meme-card {{
                background-color: #fff;
                margin-bottom: 20px;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            h2 {{
                color: #333;
            }}
            .meme-info {{
                margin-bottom: 20px;
            }}
            .meme-info p {{
                margin: 5px 0;
            }}
            .meme-info img {{
                max-width: 100%;
                height: auto;
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Meme Data</h1>
    """

    # Loop through each meme object and generate HTML for it
    for meme in meme_data:
        html_content += f"""
            <div class="meme-card">
                <h2>{meme['title']}</h2>
                <div class="meme-info">
                    <p><strong>ID:</strong> {meme['id']}</p>
                    <p><strong>Score:</strong> {meme['score']}</p>
                    <p><strong>URL:</strong> <a href="{meme['url']}">{meme['url']}</a></p>
                    <p><strong>Created at:</strong> {datetime.utcfromtimestamp(meme['created_utc']).strftime('%Y-%m-%d %H:%M:%S')}</p>
                    <p><strong>Author:</strong> {meme['author']}</p>
                    <p><strong>Author ID:</strong> {meme['author_id']}</p>
                    <img src="{meme['url']}" alt="Meme">
                </div>
            </div>
        """

    html_content += """
        </div>
    </body>
    </html>
    """
    return html_content
