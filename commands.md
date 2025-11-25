## Deploy Agent to ADK

adk deploy agent_engine \
    --project=qwiklabs-gcp-04-25e0f6d2c669 \
    --region=us-central1 \
    --staging_bucket=gs://BUCKET_ID \
    --display_name="Paint Agent" \
    paint_agent
