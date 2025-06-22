# Cloud Run LLM Classifier

This example shows a simple Python application that runs on Google Cloud Run and
uses a very small language model to classify a description into one of several
predefined automotive categories.

The model is implemented locally with simple keyword matching so the service has
no heavy dependencies and starts quickly.

## Quick Deploy

1. Build the Docker image:
   ```sh
   docker build -t gcr.io/PROJECT_ID/cloud-run-llm .
   ```
2. Push to Google Container Registry:
   ```sh
   docker push gcr.io/PROJECT_ID/cloud-run-llm
   ```
3. Deploy to Cloud Run:
   ```sh
   gcloud run deploy cloud-run-llm \
     --image gcr.io/PROJECT_ID/cloud-run-llm \
     --platform managed \
     --region REGION \
     --allow-unauthenticated
   ```

The application exposes the `/classify` endpoint, which expects JSON input:

```json
{
  "description": "Necesito cambiar las pastillas de freno de mi coche"
}
```

and returns the estimated category:

```json
{
  "category": "Frenos"
}
```

## Local Testing

The `tests/` directory contains unit tests with example conversations. Run them
using:

```sh
pip install -r requirements.txt pytest
pytest
```
