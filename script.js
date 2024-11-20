document.getElementById('quizForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    const params = new URLSearchParams({
        prompt: formData.get('prompt'),
        num_questions: formData.get('num_questions'),
        difficulty: formData.get('difficulty')
    });

    try {
        const response = await fetch(`http://localhost:5000/generate-quiz?${params}`);
        if (!response.ok) throw new Error('Network response was not ok');
        
        const data = await response.json();
        console.log('Quiz data received:', data);
        
        localStorage.setItem('currentQuiz', data.quiz);
        window.location.href = './quiz.html';
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to generate quiz. Please try again.');
    }
}); 