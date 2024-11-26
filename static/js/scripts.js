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

        if (selectedAnswer === questionData.correct_answer) {
            score += 10;
        }

        currentQuestionIndex++;
        if (currentQuestionIndex < questions.length) {
            showQuestion(currentQuestionIndex);
        } else {
            // Show results
            const finalScore = score * multiplier;
            scoreSpan.textContent = finalScore.toFixed(0)
            questionContainer.style.display = 'none';
            resultsContainer.style.display = 'block';
            buttonsContainer.style.display = 'block';
        }
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
