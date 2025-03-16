
# Implementation of Personal Fitness Tracker using Python 

##  Project Overview

Health-Mantra is a comprehensive health and fitness tracking application designed to help users monitor their fitness progress, predict calorie burn, and visualize health metrics. The project integrates a Django-based web application with a FastAPI backend for machine learning predictions, leveraging MongoDB Cloud for data storage and management.
## Key Achievements

- **AI-Powered Calorie Prediction**: Predict calories burned based on user input using a trained machine learning model.
- **Interactive Dashboard**: Visualize fitness data with dynamic charts powered by Chart.js.
- **User Authentication**: Secure login and logout functionality using Django AllAuth.
- **Prediction History**: Track and view past predictions stored in MongoDB Cloud.
- **Data Analysis**: Perform exploratory data analysis (EDA) using Jupyter Notebooks.
- **Scalable Architecture**: Modular design with separate components for backend, frontend, and machine learning pipelines.
## Architecture

- **Frontend**: A Django web application with Bootstrap for responsive design and Chart.js for data visualization.
- **Backend**: A FastAPI service for handling machine learning predictions.
- **Database**: MongoDB Cloud for storing user data and prediction history.
- **Machine Learning**: A pipeline built with Scikit-learn, ZenML, and MLflow for training and managing models.
## Setup

1. Clone the Repository
Clone the project repository to your local machine:

```bash 
git clone https://github.com/your-repo/health-mantra.git
cd health-mantra
```

2. Set Up the Backend (FastAPI)
- Navigate to the calories-tracker directory:

```bash
cd calories-tracker
```

- Install the required dependencies:

```bash
pip install -r requirements.txt
```

- Configure the .env file with your MongoDB Cloud connection string:
```
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<database>?retryWrites=true&w=majority
```

- Run the FastAPI server

```bash
uvicorn app.main:app --reload
```
The backend will be available at http://127.0.0.1:5000.

3. Set Up the Frontend (Django)

- Navigate to the webapp directory

```bash
cd ../webapp
```

- Install the required dependencies:

```bash
pip install -r requirements.txt
```

- Apply database migrations:
```bash
python manage.py migrate
```
- Start the Django development server

```bash
python manage.py runserver
```

4. Access the Application

- Open your browser and navigate to http://127.0.0.1:8000/. To access the functionality signup / login to your account.
- Use the calorie predictor and dashboard to view analytics.

5. Using Docker
    1. Build and Start the Services Use the docker-compose.yaml file to build and start the services:

```bash
docker-compose up --build
```

This will:

- Build the Django service (webapp) and expose it on port 8000.
- Build the FastAPI service (calories-tracker) and expose it on port 5000.
Verify the Setup

- Open your browser and navigate to http://127.0.0.1:8000 to access the Django web application.
- The FastAPI service will be available at http://127.0.0.1:5000.

2. Stop the Services To stop the running containers, press Ctrl+C or run:

```bash 
docker-compose down
```
## Technology Used

- **Frontend**: Django, Bootstrap, Chart.js
- **Backend**: FastAPI, Scikit-learn, MLflow
- **Database**: MongoDB Cloud
- **Other Tools**: ZenML, DVC, Docker
## Conclusion

Health-Mantra is a powerful and user-friendly platform designed to help individuals track their fitness progress, predict calorie burn, and visualize health metrics. By combining modern web technologies like Django and Bootstrap with machine learning capabilities powered by FastAPI and Scikit-learn, the project delivers a seamless and interactive user experience.

With MongoDB Cloud as the backbone for data storage, the application ensures scalability and reliability for managing user data and prediction history. The modular architecture also makes it easy to extend and enhance the platform with additional features in the future.

Whether you're a fitness enthusiast or a developer looking to explore the integration of machine learning with web applications, Health-Mantra serves as a practical and insightful project. Contributions and feedback are always welcome to make this platform even better!