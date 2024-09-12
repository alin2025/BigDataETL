import boto3
import zipfile
from io import BytesIO

# Initialize MinIO client using boto3 with your MinIO settings
s3 = boto3.client(
    "s3",
    endpoint_url="http://minio:9000",  # Replace with your MinIO server URL
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin",
    region_name="us-east-1"  # Optional, adjust if necessary
)

# Define source and destination buckets
source_bucket = "my-amadeus"  # Replace with your source bucket name
destination_bucket = "zip"  # The bucket where the zip file will be uploaded
zip_file_name = "zipped_data.zip"  # Name of the zip file

# Create a BytesIO object to store the zip file in memory
zip_buffer = BytesIO()

try:
    # Initialize a ZipFile object in write mode
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # List all objects in the source bucket
        response = s3.list_objects_v2(Bucket=source_bucket)
        if 'Contents' in response:
            for obj in response['Contents']:
                file_key = obj['Key']
                # Download each file from the source bucket
                file_response = s3.get_object(Bucket=source_bucket, Key=file_key)
                file_data = file_response['Body'].read()
                # Add the file to the zip archive
                zip_file.writestr(file_key, file_data)
                print(f"Added {file_key} to zip archive.")

    # Seek to the beginning of the BytesIO buffer
    zip_buffer.seek(0)

    # Upload the zip file to the destination bucket
    s3.put_object(Bucket=destination_bucket, Key=zip_file_name, Body=zip_buffer.getvalue())
    print(f"Zipped data uploaded to {destination_bucket}/{zip_file_name}")

    # Delete the original files from the source bucket
    if 'Contents' in response:
        for obj in response['Contents']:
            file_key = obj['Key']
            try:
                s3.delete_object(Bucket=source_bucket, Key=file_key)
                print(f"Deleted {file_key} from {source_bucket}")
            except Exception as e:
                print(f"Error deleting {file_key}: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
