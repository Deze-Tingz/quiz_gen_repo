async function generateQuiz(event) {
    event.preventDefault(); // Prevent form submission

    const prompt = document.getElementById("promptInput").value;
    const numQuestions = document.getElementById("numQuestions").value;
    const difficulty = document.getElementById("difficulty").value;

    // OpenAI API endpoint
    const apiEndpoint = "https://api.openai.com/v1/completions";
    const apiKey = "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"; // Replace with your actual API key, but don't leave it in client-side code for production

    // Request payload for OpenAI API
    const payload = {
        model: "text-davinci-003",
        prompt: `Create ${numQuestions} ${difficulty} questions based on "${prompt}". Format as Q&A for each question.`,
        max_tokens: 100 * parseInt(numQuestions, 10), // Ensure numQuestions is an integer
        temperature: 0.7,
        n: 1 // Number of responses
    };

    try {
        const response = await fetch(apiEndpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${apiKey}`
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) throw new Error(`Failed to generate quiz. Status: ${response.status}`);

        const data = await response.json();

        if (data.choices && data.choices[0] && data.choices[0].text) {
            const quizQuestions = data.choices[0].text.trim().split("\n").filter(line => line);

            // Store quiz data to local storage to access in quiz.html
            localStorage.setItem("quizQuestions", JSON.stringify(quizQuestions));

            // Redirect to quiz page
            window.location.href = "./quiz.html";
        } else {
            throw new Error("Unexpected response format from the API.");
        }
    } catch (error) {
        console.error("Error generating quiz:", error);
        alert("Error generating quiz. Please try again.");
    }
}