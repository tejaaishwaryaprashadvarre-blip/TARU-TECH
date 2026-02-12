function answerQuestion() {
    var question = document.getElementById("question").value.toLowerCase();
    var response = document.getElementById("response");

    if (question === "") {
        response.innerText = "Please enter a question.";
        return;
    }

    response.innerText = "Analyzing your query...";

    setTimeout(function () {

        if (question.includes("rice")) {
            response.innerText = "Recommended for rice: Use nitrogen-rich fertilizer and maintain proper irrigation.";
        } 
        else if (question.includes("pest")) {
            response.innerText = "Suggested pest control: Neem oil spray and crop rotation techniques.";
        } 
        else if (question.includes("fertilizer")) {
            response.innerText = "Organic fertilizers improve soil health and long-term yield.";
        } 
        else {
            response.innerText = "AI Advisory: Based on your query, consult local agricultural experts for best results.";
        }

    }, 2000);
}