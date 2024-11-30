
# 🌟 Welcome to Know_It_All 🎮✨
We’re thrilled to introduce Know_It_All, the ultimate trivia game that challenges your brain, 
sparks your curiosity, and ignites your competitive spirit! 

Designed with passion and teamwork, this project is the result of collaboration among four creative minds: Tõnis, Victoria, Rauno, and Sirli. 

This is more than just a game—it’s our first collaborative project, where we combined our diverse skills and passion to create something meaningful.

We hope you’ll enjoy playing as much as we enjoyed making it!

Dive in and put your knowledge to the test!

### 🌟 Features 
What Makes Know_It_All Special?

Here’s why we think you’ll love it:

💡 Engaging Trivia Questions: Explore categories from Entertainment and Celebrities to Science and Geography—there’s something for everyone! 
Test your knowledge across diverse categories.

⚖️ Dynamic Scoring: Each question’s difficulty level makes scoring a strategic challenge and make the game more exciting.

✨ Sleek Design: Enjoy an intuitive, visually appealing, clean and user-friendly design for seamless gameplay. 

🔒 Data Privacy First: Your data stays safe and secure because we take privacy seriously.

👨‍👩‍👧‍👦 Built for Fun: Designed with friends and family in mind—challenge each other and share the fun!

## 🚀 Getting Started
Here’s how to bring Know_It_All to life on your local device. 

Follow all these steps :
### Prerequisites
1. Python 3.11+ installed on your system.
2. Familiarity with basic Django commands (don’t worry, we’ll guide you).

### Installation
1. Clone the Repository:
git clone https://github.com/TonisJoosep/Know_It_All
2. Set Up the Environment:
Create a virtual environment and activate it: 

   python -m venv env

   source env/bin/activate  # On Windows: env\Scripts\activate 

3. Install Dependencies:

   Install the necessary Python packages using:
   
   pip install -r requirements.txt
4. Database

Use MySQL or PostgreSQL (recommended for Mac users) as database. 

You need to create .env file with these values:

    SECRET_KEY="" # You need to create your own Django key

    DEBUG="True"

    DB_ENGINE="" # Choose your database

    DB_USER="" # Your database user name

    DB_PASSWORD="" # Your database password

    DB_PORT="" # Choose your database port

    DB_HOST="" # Choose your database host

    DB_NAME="" # Choose your database name

5. Create schema with same name as database (DB_NAME) name
6. Run Database Migrations:

   python manage.py makemigrations

   python manage.py migrate
7. Run the Development Server: 

   Start the Django server:

   python manage.py runserver
8. Launch the Server:

   Open your browser and go to: 'http://127.0.0.1:8000'
9. Create user account 
10. Start Playing!

### How to Play the Trivia Game 🎮
1. Create account or login if you have registered yet
2. Choose a Topic: Begin by selecting a topic that interests you the most—be it science, history, entertainment, or more!
3. Choose a Sub-Category 
4. Choose a Difficulty level - easy, medium or hard
5. Choose a Number of Questions - 1, 5, 10 or 15
6. Answer the Questions

   Each question comes with multiple-choice answers.

   Take your time to read the question carefully and click on the answer you think is correct.

   Once you select an answer, you are moved automatically to the next question.
7. Difficulty Multiplier

   The difficulty level you choose at the start affects your final score. 

   The harder the questions, the bigger the score multiplier!
8. Score and Results
   After completing the quiz, your total score will be displayed along with a breakdown:

   Your correct answers

   The difficulty multiplier

   Your final score
9. Replay, explore another topic or Challenge Friends

   Love the experience? Hit the Replay button to improve your score, or invite friends to test their knowledge too!

   It’s more fun with a little friendly competition!

🎲 Ready? Let the trivia showdown begin and see if you can beat the high score! 🏆

### 📷 Screenshots
Here’s a sneak peek of the game in action:

🖥️ Home Page

![]() (./demo.png)


📊 Results Page

![demo image] (./demo2.png)

![demo image] (./demo3.png)


❓ Question Interface

![demo image] (./demo4.png)

### 🤝 Meet the Team
We’re a small but mighty team, united by a shared passion for creativity, coding, and making people smile.

Tõnis: The strategist who kept us on track and glued all the project together

Victoria: The artistic eye behind the sleek design.

Rauno: Our tech wizard who turned ideas into reality.

Sirli: The cheerleader and motivator, a person who also dived into the backend, exploring its intricacies and contributing valuable insights that elevated the project.

We all learned something new while building Know_It_All, and we couldn’t be prouder of the result!

### 📧 Contact Us
Have questions or feedback? 

Feel free to reach out:

📩 Email: `knowitalltriviagame@gmail.com`

### 🌟 Acknowledgments
This project is powered by the creativity, skills, and enthusiasm of a dedicated team. 

It all wouldn’t have been possible without:
Endless cups of coffee ☕, huge amounts of canned food🥫, cookies🍪 and fresh fruits🍏

Countless brainstorming sessions 🤯

The unwavering support of our trainer Vladislavs and our families!

To everyone who believed in us and tested the game—thank you! 

You’re part of what makes this special.

### 🌟 Final Thoughts
Know_It_All is more than a trivia game; it’s a symbol of teamwork, growth, and creativity. 

Whether you're here to learn, compete, or just have fun, we’re glad you’ve joined us on this journey.

We hope you’ll enjoy playing as much as we enjoyed creating it. 

Let the games begin! 🎲✨
