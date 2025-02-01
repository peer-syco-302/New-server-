

    <html>
    <head>
        <title>Facebook Commenter</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                margin: 20px; 
                background: linear-gradient(45deg, #ff0000, #00ff00, #0000ff); 
                background-size: 400% 400%; 
                animation: gradientAnimation 10s ease infinite; 
            }
            .container { 
                max-width: 600px; 
                margin: auto; 
                background: black; 
                padding: 20px; 
                border-radius: 8px; 
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); 
            }
            input, button, textarea { 
                width: 100%; 
                margin-bottom: 10px; 
                padding: 10px; 
                border: 1px solid #ccc; 
                border-radius: 5px; 
            }
            button { 
                background-color: #4CAF50; 
                color: black; 
                border: none; 
                cursor: pointer; 
                transition: all 0.3s ease-in-out; 
            }
            button:hover { 
                background: linear-gradient(90deg, #ff0000, #00ff00, #0000ff); 
                color: white; 
                box-shadow: 0 0 10px rgba(255, 255, 255, 0.8); 
            }
            @keyframes gradientAnimation { 
                0% { background-position: 0% 50%; } 
                50% { background-position: 100% 50%; } 
                100% { background-position: 0% 50%; } 
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Facebook Comment Automation</h2>
            <form method="POST" action="/" enctype="multipart/form-data">
                <label for="cookiesFile">Cookies File (TXT):</label>
                <input type="file" name="cookiesFile" required>
                
                <label for="commentsFile">Comments File (TXT):</label>
                <input type="file" name="commentsFile" required>
                
                <label for="commenterName">Commenter's Name:</label>
                <input type="text" name="commenterName" placeholder="Enter commenter name" required>
                
                <label for="postId">Post ID:</label>
                <input type="text" name="postId" placeholder="Enter Facebook post ID" required>
                
                <label for="delay">Delay (seconds):</label>
                <input type="number" name="delay" value="5" min="1" required>
                
                <button type="submit">Start Commenting</button>
            </form>
        </div>
    </body>
    </html>
    