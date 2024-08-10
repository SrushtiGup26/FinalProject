# FinalProject

# SMS/IM Spam Filtering System

## Overview

The SMS/IM Spam Filtering System is a web-based application designed to detect and filter out spam messages from incoming SMS or instant messaging (IM) content. Built using Flask, this application leverages a machine learning-based approach to classify messages as either "spam" or "not spam."

## Objectives

- **User Interface:** Provide an intuitive web interface for users to input and analyze messages.
- **Machine Learning Integration:** Incorporate a pre-trained model for accurate spam classification.
- **Backend System:** Implement a robust backend with MySQL database integration for data storage and analysis.
- **CI/CD Pipeline:** Automate testing and deployment processes using CI/CD pipelines.
- **Monitoring:** Ensure application reliability and performance with a monitoring system.

## Installation

### Prerequisites

- Python 3.8+
- MySQL

### Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/SrushtiGup26/TestingProject.git
    cd TestingProject
    ```

2. **Install Dependencies:**

    ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

3. **Configure the Database:**

   Set up your MySQL database and update the database configuration in `config.py`.

4. **Run the Application:**

    ```bash
    python app.py
    ```

   The application will be accessible at `http://localhost:5000`.

## CI/CD Pipeline

The project uses GitHub Actions for CI/CD. The pipeline is defined in `.github/workflows/ci-cd.yml` and includes:

- **Continuous Integration (CI):** Automatically runs tests on each push or pull request to the `main` branch.
- **Continuous Deployment (CD):** Deploys the application to Heroku after successful tests.

## Testing

The application includes automated tests for critical functionality. Tests are executed as part of the CI pipeline using `unittest`. To run tests locally:

```bash
python -m unittest discover
```

## Deployment

The application is deployed to Heroku. The deployment is automated via the CI/CD pipeline and is triggered by successful tests. For manual deployment, follow these steps:

1. **Add Heroku Remote:**

    ```bash
    git remote add heroku https://git.heroku.com/your-heroku-app-name.git
    ```

2. **Push to Heroku:**

    ```bash
    git push heroku main
    ```

## User Interface

The UI is developed using HTML, CSS, and Flask’s templating engine. Users can input messages and receive instant feedback on whether the message is classified as spam or not.

## Database Integration

The system uses MySQL for storing historical message data and their classifications. Ensure the MySQL server is running and accessible.

## Monitoring

The application includes a monitoring system to track reliability and performance in production. Alerts and metrics are configured to notify developers of any production issues.

## Final Output

- **GitHub Repository:** [GitHub URL](https://github.com/SrushtiGup26/TestingProject/tree/main)
- **Heroku App:** [Live Application](https://finalproject-aienterprise-5855c53bcc68.herokuapp.com/)

## Conclusion

The SMS/IM Spam Filtering System effectively addresses spam detection with a user-friendly interface, robust backend processing, and modern CI/CD practices. It is ready for deployment and use in real-world environments.
