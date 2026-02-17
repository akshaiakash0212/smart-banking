function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value;

    let chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += "<b>You:</b> " + message + "<br>";

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += "<b>Bot:</b> " + data.reply + "<br>";
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    input.value = "";
}
