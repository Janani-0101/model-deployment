Model Deployment – Sentiment Analysis API

This project demonstrates how a trained machine learning model can be deployed
as a REST API using FastAPI and Docker. The API accepts text input and returns
the predicted sentiment as either Positive or Negative.

The application loads a pretrained sentiment analysis model and exposes
endpoints for health checking and prediction. Docker is used to containerize
the application so it can be run consistently across different environments.

API Endpoints

GET /
This endpoint is used to check whether the API is running.

POST /predict
This endpoint accepts a JSON request containing text and returns the predicted
sentiment.

Example request body:
{
  "text": "This movie was amazing"
}

Example response:
{
  "text": "This movie was amazing",
  "sentiment": "Positive"
}

Running the application locally

Install the required dependencies using pip.
Run the FastAPI application using uvicorn.
The API will be available at http://127.0.0.1:8000

Running the application using Docker

Build the Docker image using the Dockerfile.
Run the Docker container and map port 8000.
The API will be accessible at http://localhost:8000

Conclusion

This project shows a complete workflow for deploying a machine learning model
as a web service. By using FastAPI and Docker, the model can be easily tested,
shared, and deployed in a scalable and portable way.
