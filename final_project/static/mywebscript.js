let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                let response = JSON.parse(this.responseText); // Parse JSON response
                // Construct the result display string
                let result = `<p><strong>Anger:</strong> ${response.anger}</p>
                              <p><strong>Disgust:</strong> ${response.disgust}</p>
                              <p><strong>Fear:</strong> ${response.fear}</p>
                              <p><strong>Joy:</strong> ${response.joy}</p>
                              <p><strong>Sadness:</strong> ${response.sadness}</p>
                              <p><strong>Dominant Emotion:</strong> ${response.dominant_emotion}</p>`;
                document.getElementById("system_response").innerHTML = result; // Display result
            } else {
                document.getElementById("system_response").innerHTML = `<p style="color:red;">Error: ${this.status}</p>`;
            }
        }
    };
    xhttp.open("POST", "/emotionDetector", true); // Change to POST
    xhttp.setRequestHeader("Content-Type", "application/json"); // Set content type for JSON
    xhttp.send(JSON.stringify({ textToAnalyze: textToAnalyze })); // Send JSON data
}
