document.addEventListener('DOMContentLoaded', function () {
    console.log(questions); // Pass questions from Django context
    let currentQuestionIndex = 0;
    let score = 0;
    const difficulty = document.getElementById('data-container').dataset.difficulty; // Get difficulty
    const multiplier = parseFloat(document.getElementById('data-container').dataset.multiplier);
    const questionContainer = document.getElementById('question-container');
    const answersContainer = document.getElementById('answers-container');
    const nextButton = document.getElementById('next-button');
    const resultsContainer = document.getElementById('results-container');
    const scoreSpan = document.getElementById('score');
    const replayButton = document.getElementById('replay-button');
    const buttonsContainer = document.getElementById('game-buttons-container');


    function showQuestion(index) {
        const questionData = questions[index];
        const questionDiv = document.querySelector('.question');

        questionDiv.innerHTML = questionData.question;

        answersContainer.innerHTML = '';

        questionData.shuffled_answers.forEach(answer => {
            const button = document.createElement('button');
            button.className = 'answer-button';
            button.textContent = answer;
            button.addEventListener('click', () => handleAnswerClick(answer));
            answersContainer.appendChild(button);
        });

        nextButton.style.display = 'none'; // Hide the next button initially
    }

   function handleAnswerClick(selectedAnswer) {
    const questionData = questions[currentQuestionIndex];
    const answerButtons = document.querySelectorAll('.answer-button');
    const correctAnswer = questionData.correct_answer;

    // Find the button the user clicked
    const selectedButton = Array.from(answerButtons).find(button => button.textContent === selectedAnswer);

    // Disable all buttons to prevent multiple clicks
    answerButtons.forEach(button => button.disabled = true);

    // Highlight selected answer based on correctness
    if (selectedAnswer === correctAnswer) {
        selectedButton.classList.add('btn-success');
        score += 10; // Increment score only if the answer is correct
    } else {
        selectedButton.classList.add('btn-danger');
        // Highlight the correct answer in green
        const correctButton = Array.from(answerButtons).find(button => button.textContent === correctAnswer);
        correctButton.classList.add('btn-success');
    }

    selectedButton.offsetHeight;

    // Delay before moving to the next question or showing results
    setTimeout(() => {
        currentQuestionIndex++;
        if (currentQuestionIndex < questions.length) {
            showQuestion(currentQuestionIndex);
        } else {
            // Show final results
            const finalScore = score * multiplier;
            scoreSpan.textContent = finalScore.toFixed(0);
            questionContainer.style.display = 'none';
            resultsContainer.style.display = 'block';
            buttonsContainer.style.display = 'block';

            // Save the score to the database
            saveScoreToDatabase(finalScore);
        }
    }, 1500); //
}

    replayButton.addEventListener('click', () => {
        currentQuestionIndex = 0;
        score = 0;
        questionContainer.style.display = 'block';
        resultsContainer.style.display = 'none';
        buttonsContainer.style.display = 'none'; // Hide replay and home buttons
        showQuestion(currentQuestionIndex);
    });

    // Show the first question initially
    showQuestion(currentQuestionIndex);
});
function saveScoreToDatabase(finalScore) {
    const dataContainer = document.getElementById('data-container');
    const category = dataContainer.dataset.category;  // Fetch category
    const difficulty = dataContainer.dataset.difficulty;  // Fetch difficulty

    fetch('/save-score/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(), // Include CSRF token
        },
        body: JSON.stringify({
            score: finalScore,
            category: category,
            difficulty: difficulty,
        })
    })
    .then(response => {
    console.log('Response status:', response.status);
    return response.json();
})
.then(data => {
    console.log('Response data:', data);
})
.catch(error => {
    console.error('Error:', error);
});
}

// Helper function to get the CSRF token
function getCSRFToken() {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
        const [name, value] = cookie.trim().split('=');
        if (name === 'csrftoken') {
            return value;
        }
    }
    return '';
}

