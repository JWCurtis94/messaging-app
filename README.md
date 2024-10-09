# Messaging App

This project is a simple messaging system built with Django, where users can connect with friends, send friend requests, and exchange messages. The app allows users to manage their friend lists and communicate in real-time with their connections.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Secure registration, login, and logout functionality.
- **Friendship System**: Send, accept, or reject friend requests.
- **Real-time Messaging**: Exchange messages with friends in real-time.
- **Friend List**: View and manage your list of friends.
- **Message Notifications**: Get notified when you receive a new message.
- **User Profiles**: View other users' profiles and send friend requests.

## Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (for development) / PostgreSQL (for production)
- **Frontend**: HTML, CSS (Bootstrap), JavaScript (for real-time messaging)
- **Other Tools**: 
  - Git for version control
  - Django ORM for database management
  - GitHub and Gitpod for development

## Installation

Follow these steps to get the project up and running on your local machine:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/messaging-app.git
    cd messaging-app
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the app at `http://127.0.0.1:8000/`.

## Usage

1. **Register a new user**: Sign up with an email and password.
2. **Friendship management**: Search for users, send friend requests, accept/reject requests.
3. **Messaging**: Start a chat with any friend by going to your friends list, select the friend and send a message.

## Future Enhancements

- **Group Chat**: Allow users to create group chats and message multiple people at once.
- **Message Reactions**: Add emoji reactions to messages.
- **Profile Pictures**: Enable users to upload profile pictures.
- **Search Functionality**: Implement a search feature to quickly find messages or friends.
- **Push Notifications**: Add push notifications for real-time messaging alerts.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
