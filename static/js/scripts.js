document.addEventListener('DOMContentLoaded', function () {
    console.log(questions); // Pass questions from Django context
    let currentQuestionIndex = 0;
    let score = 0;

    const questionContainer = document.getElementById('question-container');
    const nextButton = document.getElementById('next-button');
    const resultsContainer = document.getElementById('results-container');
    const scoreSpan = document.getElementById('score');
    const replayButton = document.getElementById('replay-button');
    const buttonsContainer = document.getElementById('game-buttons-container');

    function showQuestion(index) {
        const questionData = questions[index];
        const questionDiv = document.querySelector('.question');

        let questionHtml = `<h3>${questionData.question}</h3><ul>`;
        const answers = questionData.shuffled_answers;

        answers.forEach(answer => {
            questionHtml += `<li><input type='radio' name='answer' value="${answer}"> ${answer}</li>`;
        });
        questionHtml += '</ul>';
        questionDiv.innerHTML = questionHtml;

        nextButton.style.display = 'block';
    }

    nextButton.addEventListener('click', () => {
        const selectedAnswer = document.querySelector('input[name="answer"]:checked');
        if (selectedAnswer) {
            if (selectedAnswer.value === questions[currentQuestionIndex].correct_answer) {
                score++;
            }
            currentQuestionIndex++;
            if (currentQuestionIndex < questions.length) {
                showQuestion(currentQuestionIndex);
            } else {
                // Show results
                scoreSpan.textContent = score;
                questionContainer.style.display = 'none';
                resultsContainer.style.display = 'block';
                buttonsContainer.style.display = 'block';
            }
        } else {
            // Handle case where no answer is selected
            alert('Please select an answer.');
        }
    });

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
