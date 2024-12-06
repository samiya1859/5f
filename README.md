# Flask project

## Project Overview

The 5F Project is a Python-based web application designed to help users manage their login credentials and perform CRUD (Create, Read, Update, Delete) operations on destinations. Built using Flask, this application provides a secure login system with role-based access control (admin and regular users). Admin users are authorized to manage destinations, while regular users can view them. The application also supports seamless interactions with a backend database to store and retrieve destination data.


## Features

- **User Authentication:** Secure login and registration system, including role-based access control (admin and user roles).
- **Destination Management:** Admin users can add, update, and delete destinations, while regular users can view and search destinations.
- **RESTful API:** A set of REST APIs for CRUD operations on destinations and user management, designed for seamless integration with other services or front-end clients.
- **Session Management:** A system for managing user sessions, including authentication tokens to ensure secure access to the application’s features.
- **Role-based Access Control:** Only admin users can perform authorized operations on destinations (such as adding, updating, and deleting), while regular users are limited to viewing destinations.

## Installation

Follow these steps to get your development environment set up:

### 1. Clone the Repository

```bash
git clone https://github.com/samiya1859/5f.git
cd 5f
```
### 2. Set Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies. If you don't have virtualenv installed, install it first:
```bash
pip install virtualenv
```
or
```bash
python3 -m venv .venv
```
Now, create and activate the virtual environment:
```bash
virtualenv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```
### 3. Install Dependencies
Once the virtual environment is activated, install the required dependencies from requirements.txt:
```bash
pip install -r requirements.txt
```
### 4. Run the Application
Now that everything is set up, run the application using the following command:
```bash
flask run
```
This will start the Flask development server, and you can access the application at http://localhost:5000

##API Documentation
The 5F Project provides a RESTful API for interacting with its resources. Below is an overview of the main API endpoints:

### 1. Authentication Endpoints
POST /register: Register a new user (admin or regular).
POST /login: Login to the application and retrieve an authentication token.
### 2. User Profile
GET /profile: Retrieve the current logged-in user's profile information.
PUT /profile: Update the logged-in user's profile information. Requires name, email, and password.
DELETE /profile: Delete the logged-in user's profile.
### 3. Admin Control
GET /users: Admins can retrieve a list of all users.

### 4. Destination Endpoints
GET /destinations: Retrieve all destinations.
GET /destinations/{id}: Retrieve a specific destination by ID.
POST /destinations: Add a new destination (Admin only).
PUT /destinations/{id}: Update an existing destination (Admin only).
DELETE /destinations/{id}: Delete a destination (Admin only).

### 5. Error Handling
The API provides standardized error responses with appropriate HTTP status codes. Examples include:

404 Not Found: When a resource is not found.
403 Forbidden: When an unauthorized action is attempted.

## Testing
To ensure the application works correctly, we have written tests using pytest.

### 1. Run Tests
To run all the tests in the project, use the following command:
```bash
pytest
```
### 2. Run Tests for Specific Features
If you only want to test specific parts of the application (e.g., destination routes), use:

```bash
pytest tests/test_destination_routes.py
```
## Contributing
We welcome contributions to the 5F Project! If you would like to contribute, please follow these steps:

Fork the repository.
Create a new branch for your feature or bugfix.
Commit your changes.
Push your branch and open a pull request.
Please ensure that your code passes tests and follows the project’s coding standards before submitting a pull request.

## License
The 5F Project is licensed under the MIT License. See the LICENSE file for more details.

## Summary
This README now fully describes the 5F Project, including its features such as user authentication, destination management with CRUD operations, and role-based access control. Make sure to replace placeholders with actual values for your project and customize the instructions as needed.
