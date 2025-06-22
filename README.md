# Experimental Cloud Run LLM Classifier

This example shows a simple Python application that runs on Google Cloud Run and
uses a very small language model to classify a description into one of several
predefined automotive categories.

The model is implemented locally with simple keyword matching so the service has
no heavy dependencies and starts quickly.

## Quick Deploy

1. Build the Docker image:
2. 
   ```sh
   pip install -r requirements.txt
   ```
y4l9gz-codex/colaboración-para-proyectos-en-la-nube-y-ai
2. Start the service:

   ```sh
   python app.py
   ```
3. Send a request:

   ```sh
   curl -X POST http://localhost:8080/classify \
       -H 'Content-Type: application/json' \
       -d '{"description": "Se ha roto el sistema electrico del coche"}'
   ```

## Running the test suite

Execute the included tests to validate the behaviour of the classifier:

```sh
pip install -r requirements.txt pytest
pytest -q
```

## Deploying to Cloud Run

Ensure the Google Cloud SDK is installed and authenticated. Replace `PROJECT_ID` and `REGION` with your values.

1. Build the image:
   ```sh
   docker build -t gcr.io/PROJECT_ID/cloud-run-llm .
   ```
2. Push to Container Registry:
   ```sh
   docker push gcr.io/PROJECT_ID/cloud-run-llm
   ```
3. Deploy:
   ```sh
   gcloud run deploy cloud-run-llm \
       --image gcr.io/PROJECT_ID/cloud-run-llm \
       --platform managed \
       --region REGION \
       --allow-unauthenticated
   ```

Once deployed, the service responds to `POST` requests on `/classify` with a JSON object containing the predicted category.

## Extending the classifier

`classifier.py` defines the list of `CATEGORIES` and the associated `KEYWORDS`. Adjust these mappings or replace the implementation with a more sophisticated model as needed. Keep in mind that the current approach is intentionally simple for easier testing and experimentation.

## License

This repository is provided for educational purposes. Use at your own risk.
