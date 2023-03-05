# Hikeable Backend Server

This is the **Hikeable** backend server built using Django, a popular Python web framework. The server provides RESTful APIs that can be used by client applications to interact with the server.

## What is Hikeable?

Introducing **Hikeable**: Hiking in Japan. Simplified.

Whether you're a seasoned hiker or just starting out, **Hikeable** is your go-to English resource for all things hiking in Japan. With our web app **Hikeable**, you can connect with other hikers by leaving geolocated messages, discover new trails, and share your hiking experiences with the community.

## Getting Started
To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using pip. You can find the required dependencies in the `requirements.txt` file.
3. Set up a local database using PostgreSQL or any other database of your choice.
4. Run database migrations to create the necessary tables and columns.
5. Start the Django development server using the following command:
`python manage.py runserver`

You should now be able to access the server at `http://localhost:8000/`.

## Environment Variables

Django requires a secret key to secure its cryptographic signing, so it's important to generate a unique and strong secret key for any Django project.

Please follow the steps [here](https://www.educative.io/answers/how-to-generate-a-django-secretkey) to generate a secret key. Once you are done, create a local `.env` file at the root level of the project, and add your secret key as an environment variable labelled `SECRET_KEY`.

## API Documentation
The server provides the following RESTful API Endpoints:

- `api/trails` Returns a list of all hiking trails
- `api/trails/<id>` Returns the details of a specific trail
- `api/trails/comments` Returns a list of all comments
- `api/trails/<id>/comments` Returns the comments for a specific trail
- `api/trails/likes` Returns a list of all like records
- `api/trails/<id>/likes` Returns the like records for a specific trail
- `api/trails/completions` Returns a list of all completion records
- `api/trails/<id>/completions` Returns the completion records for a specific trail
- `api/trails/messages` Returns a list of all geolocated messages
- `api/trails/<id>/messages` Returns the geolocated messages for a specific trail
- `api/trails/messages/likes` Returns a list of all like records for all geolocated messages
- `api/trails/messages/<id>/likes` Returns the like records for a specific geolocated message

You can use any API client, such as `Postman`, to interact with these APIs.

## Contributing
If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
