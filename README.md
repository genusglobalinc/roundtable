# roundtable
Simulates a company roundtable meeting with AI powered, role-based avatars.

This project simulates a corporate business meeting where digital avatars, representing various roles, interact based on a user-defined agenda. The front-end is built with React, and the back-end is powered by Flask, with responses generated using OpenAI's GPT.

****Prerequisites
Before you begin, ensure you have the following installed:

Node.js and npm (or yarn).

Python 3.x.

OpenAI API Key (for generating avatar responses).


****Setup Instructions
1. Install Node.js and npm (or yarn)
Ensure that Node.js and npm (or yarn) are installed on your system. You can download and install Node.js from here. npm is included with Node.js. If you prefer yarn, you can install it here.

2. Create a New React Project
Open your terminal or command prompt and run the following commands to create a new React project:

npx create-react-app my-avatar-app

cd my-avatar-app

3. Create a New Python Environment
It's recommended to run the Flask server in a virtual environment to keep dependencies isolated. Run the following commands:

For Linux/macOS:


python3 -m venv my_env

source my_env/bin/activate

For Windows:


python3 -m venv my_env

my_env\Scripts\activate

4. Install Flask
With the virtual environment activated, install Flask by running:

pip install Flask

5. Install OpenAI Python Client
You'll need to install the OpenAI Python client to generate avatar responses:

pip install openai

6. Set Up Your OpenAI API Key
In your project directory, create a file named .env and add your OpenAI API key:

OPENAI_API_KEY=your-api-key

7. Place the Front-End and Back-End Code
Front-End: Replace the contents of the src folder in your React project with the provided Roundtable.jsx and associated files (e.g., CSS).

Back-End: Create a new file called app.py in your project root directory and paste the provided Flask code into it.

8. Run the Flask Server
Ensure your virtual environment is activated, then start the Flask server with:

python3 app.py

The Flask server will typically run on http://localhost:5000.

9. Run the React Development Server
Navigate to your React project directory and start the development server:

cd my-avatar-app

npm start

The React development server will typically run on http://localhost:3000.

10. Access the Application
Open your browser and go to http://localhost:3000 to access the application. You should see the prompt asking for the meeting agenda, and once entered, the avatars will respond according to their roles and responsibilities.

Troubleshooting
Port Conflicts: If http://localhost:3000 or http://localhost:5000 are already in use, the servers may start on different ports. The terminal will indicate the correct URL to access the application.

CORS Issues: If you encounter cross-origin resource sharing (CORS) issues, you may need to configure Flask to allow requests from the React server. You can do this by installing the flask-cors package:

pip install flask-cors

Then, add the following lines to app.py:

from flask_cors import CORS

CORS(app)

Additional Notes
Deployment: For production deployment, consider using gunicorn for Flask and a service like Vercel or Netlify for React.
Environment Variables: Store sensitive keys like the OpenAI API key in environment variables or secret management services for production environments.
