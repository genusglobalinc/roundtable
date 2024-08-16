import openai
from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize OpenAI API key (Replace 'your-api-key' with your actual OpenAI API key)
openai.api_key = 'your-api-key'

# Sample data representing different business roles
avatars = [
    {
        'id': 1,
        'name': 'Owner',
        'role': 'CEO',
        'color': 'gold',
        'responsibilities': ['Set Agenda', 'Define Goals', 'Oversee Operations'],
        'priorities': ['High', 'High'],
        'skills': ['Leadership', 'Strategy'],
        'resources': ['Company Vision', 'Decision-Making Power'],
        'status': 'idle'
    },
    {
        'id': 2,
        'name': 'Dev',
        'role': 'Developer',
        'color': 'blue',
        'responsibilities': ['Develop Features', 'Fix Bugs'],
        'priorities': ['High', 'Medium'],
        'skills': ['Programming', 'Problem-Solving'],
        'resources': ['Development Tools', 'Technical Documentation'],
        'status': 'idle'
    },
    {
        'id': 3,
        'name': 'Sales',
        'role': 'Sales Representative',
        'color': 'green',
        'responsibilities': ['Client Meetings', 'Close Deals'],
        'priorities': ['High', 'High'],
        'skills': ['Negotiation', 'Communication'],
        'resources': ['CRM Software', 'Sales Decks'],
        'status': 'idle'
    },
    {
        'id': 4,
        'name': 'Creative',
        'role': 'Graphic Designer',
        'color': 'purple',
        'responsibilities': ['Create Visual Content', 'Design Marketing Material'],
        'priorities': ['Medium', 'High'],
        'skills': ['Design', 'Creativity'],
        'resources': ['Design Tools', 'Brand Guidelines'],
        'status': 'idle'
    }
]

# Sample data for the meeting agenda and goals
meeting_info = {
    'agenda': '',
    'goals': '',
    'status': 'Not Started'
}

# Sample chat messages for the live chat interface
messages = []

@app.route('/avatars', methods=['GET'])
def get_avatars():
    """Endpoint to fetch all avatars with their attributes."""
    return jsonify(avatars)

@app.route('/meeting', methods=['GET', 'POST'])
def meeting_endpoint():
    """Endpoint to get or set the meeting agenda and goals."""
    if request.method == 'GET':
        return jsonify(meeting_info)
    elif request.method == 'POST':
        agenda_input = request.json.get('agenda')
        meeting_info['agenda'] = agenda_input
        meeting_info['goals'] = 'Discuss and align on the key points for the agenda: ' + agenda_input
        meeting_info['status'] = 'In Progress'

        # Generate responses from each avatar based on their role and the agenda
        for avatar in avatars:
            prompt = f"As the {avatar['role']} named {avatar['name']}, how would you contribute to the meeting with the agenda '{agenda_input}' considering your responsibilities {avatar['responsibilities']} and priorities {avatar['priorities']}?"
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=100,
                n=1,
                stop=None,
                temperature=0.7
            )
            avatar_message = {
                'sender': avatar['name'],
                'message': response.choices[0].text.strip()
            }
            messages.append(avatar_message)

        return jsonify({'message': 'Meeting agenda and goals set'})

@app.route('/messages', methods=['GET', 'POST'])
def messages_endpoint():
    """Endpoint to get all chat messages or post a new message."""
    if request.method == 'GET':
        return jsonify(messages)
    elif request.method == 'POST':
        message = request.json
        messages.append(message)
        return jsonify({'message': 'Message received'})

@app.route('/avatar/<int:avatar_id>', methods=['PATCH'])
def update_avatar_status(avatar_id):
    """Endpoint to update the status of a specific avatar."""
    updated_status = request.json.get('status')
    for avatar in avatars:
        if avatar['id'] == avatar_id:
            avatar['status'] = updated_status
            return jsonify({'message': f"Avatar {avatar['name']}'s status updated to {updated_status}"}), 200
    return jsonify({'error': 'Avatar not found'}), 404

@app.route('/end_meeting', methods=['POST'])
def end_meeting():
    """Endpoint to end the meeting and reset the state."""
    meeting_info['status'] = 'Completed'
    meeting_info['agenda'] = ''
    meeting_info['goals'] = ''
    messages.clear()
    for avatar in avatars:
        avatar['status'] = 'idle'
    return jsonify({'message': 'Meeting ended and reset'})

if __name__ == '__main__':
    app.run(debug=True)
