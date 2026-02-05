const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

const API_URL = '/chat';

async function addMessage(text, isUser = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;

    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    if (isUser) {
        avatar.innerHTML = '<i class="fas fa-user"></i>';
    } else {
        avatar.innerHTML = '<img src="logo.png" style="width:100%; height:100%; object-fit:contain; border-radius:inherit;" onerror="this.outerHTML=\'<i class=\\\'fas fa-robot\\\'></i>\'">';
    }

    const textDiv = document.createElement('div');
    textDiv.className = 'text';

    // Help function to format links, emails and newlines
    function formatMessage(msg) {
        let formatted = msg
            // Format Bold (**text**)
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            // Format Emails
            .replace(/([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})/g, '<a href="mailto:$1" class="chat-link">$1</a>')
            // Format URLs (excluding those already in href)
            .replace(/(?<!href=")(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank" class="chat-link">$1</a>')
            // Format Newlines
            .replace(/\n/g, '<br>');
        return formatted;
    }

    messageDiv.appendChild(avatar);
    messageDiv.appendChild(textDiv);
    chatBox.appendChild(messageDiv);

    if (isUser) {
        textDiv.textContent = text;
    } else {
        // Typewriter effect for AI feel
        const formattedText = formatMessage(text);
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = formattedText;
        const plainText = tempDiv.textContent;

        let i = 0;
        textDiv.innerHTML = ""; // Clear initial

        // If it's short, just show it. Otherwise, type it.
        if (text.length < 20) {
            textDiv.innerHTML = formattedText;
        } else {
            return new Promise((resolve) => {
                const interval = setInterval(() => {
                    textDiv.innerHTML = formatMessage(text.substring(0, i));
                    i += 2; // Type 2 chars at a time for speed
                    chatBox.scrollTop = chatBox.scrollHeight;
                    if (i >= text.length) {
                        textDiv.innerHTML = formattedText;
                        clearInterval(interval);
                        resolve();
                    }
                }, 15);
            });
        }
    }

    // Scroll to bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}

function addTypingIndicator() {
    const indicator = document.createElement('div');
    indicator.className = 'message bot-message typing-container';
    indicator.id = 'typing-indicator';
    indicator.innerHTML = `
        <div class="avatar">
            <img src="logo.png" style="width:100%; height:100%; object-fit:contain; border-radius:inherit;" onerror="this.outerHTML='<i class=\'fas fa-robot\'></i>'">
        </div>
        <div class="typing-indicator">
            <span></span>
            <span></span>
            <span></span>
        </div>
    `;
    chatBox.appendChild(indicator);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function removeTypingIndicator() {
    const indicator = document.getElementById('typing-indicator');
    if (indicator) {
        indicator.remove();
    }
}

async function handleSendMessage(specificMessage = null) {
    const message = specificMessage || userInput.value.trim();
    if (!message) return;

    // Show user message
    addMessage(message, true);
    if (!specificMessage) userInput.value = '';

    // Show typing indicator
    addTypingIndicator();

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        // Remove indicator and show bot response
        removeTypingIndicator();
        if (data.response) {
            await addMessage(data.response);
        } else {
            await addMessage("Sorry, I'm having trouble connecting to the server.");
        }
    } catch (error) {
        console.error('Error:', error);
        removeTypingIndicator();
        addMessage("Connecting to knowledge base... Please make sure the backend server is running.");
    }
}

function sendQuickMessage(text) {
    handleSendMessage(text);
}

sendBtn.addEventListener('click', () => handleSendMessage());

userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleSendMessage();
    }
});
