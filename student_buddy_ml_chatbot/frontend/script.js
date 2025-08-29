async function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");
  const message = input.value.trim();
  if (!message) return;

  chatBox.innerHTML += `<div><strong>You:</strong> ${message}</div>`;

  const res = await fetch("http://localhost:5000/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question: message })
  });

  const data = await res.json();
  chatBox.innerHTML += `<div><strong>Bot:</strong><pre>${data.response}</pre></div>`;
  chatBox.scrollTop = chatBox.scrollHeight;
  input.value = "";
}
