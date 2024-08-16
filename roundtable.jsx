import React, { useState, useEffect } from 'react';

function Avatar({ name, color }) {
  return (
    <div className="avatar">
      <div className="avatar-circle" style={{ backgroundColor: color }}></div>
      <div className="avatar-name">{name}</div>
    </div>
  );
}

function ChatMessage({ sender, message }) {
  return (
    <div className="chat-message">
      <span className="sender">{sender}: </span>
      <span className="message">{message}</span>
    </div>
  );
}

function ChatWindow({ messages }) {
  return (
    <div className="chat-window">
      {messages.map((message, index) => (
        <ChatMessage key={index} sender={message.sender} message={message.message} />
      ))}
    </div>
  );
}

function Roundtable() {
  const [avatars, setAvatars] = useState([]);
  const [messages, setMessages] = useState([]);
  const [agendaInput, setAgendaInput] = useState('');
  const [meetingStarted, setMeetingStarted] = useState(false);

  useEffect(() => {
    // Fetch avatars from the backend
    fetch('/avatars')
      .then(response => response.json())
      .then(data => setAvatars(data))
      .catch(error => console.error('Error fetching avatars:', error));
  }, []);

  useEffect(() => {
    if (meetingStarted) {
      // Fetch chat messages from the backend
      fetch('/messages')
        .then(response => response.json())
        .then(data => setMessages(data))
        .catch(error => console.error('Error fetching messages:', error));
    }
  }, [meetingStarted]);

  const handleAgendaSubmit = () => {
    // Send the agenda to the backend to start the meeting
    fetch('/meeting', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ agenda: agendaInput })
    })
      .then(response => response.json())
      .then(data => {
        setMeetingStarted(true);
        // Optionally, you can fetch the latest messages immediately after the meeting starts
        fetch('/messages')
          .then(response => response.json())
          .then(data => setMessages(data))
          .catch(error => console.error('Error fetching messages:', error));
      })
      .catch(error => console.error('Error starting meeting:', error));
  };

  return (
    <div className="roundtable">
      {!meetingStarted ? (
        <div className="agenda-input">
          <h2>What is the meeting agenda?</h2>
          <input
            type="text"
            value={agendaInput}
            onChange={e => setAgendaInput(e.target.value)}
            placeholder="Enter meeting agenda here"
          />
          <button onClick={handleAgendaSubmit}>Start Meeting</button>
        </div>
      ) : (
        <div>
          <ChatWindow messages={messages} />
          <div className="avatars">
            {avatars.map(avatar => (
              <Avatar key={avatar.id} name={avatar.name} color={avatar.color} />
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default Roundtable;
