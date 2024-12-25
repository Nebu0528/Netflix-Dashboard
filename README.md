# Data Pipeline and Dashboard Setup

This guide provides a step-by-step process to set up a data pipeline and dashboard.

---

## Initial Setup

1. **Create a new directory for your project**
2. **Install Python 3.9 or later**
3. **Install AWS CLI**
4. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```
5. **Activate the virtual environment:**

    - **MacOS:**
      ```bash
      source venv/bin/activate
      ```

---

## Download Dataset

1. Go to Kaggle and download the "Netflix Shows and Movies" dataset.
2. Create an AWS account if you don't have one.
3. Create an S3 bucket to store the dataset.

---

## AWS Configuration

1. Create an IAM user with appropriate permissions (S3 access).
2. Save the access key and secret key.
3. Place the following content in the `.env` file:
    ```env
    AWS_ACCESS_KEY_ID=your_access_key
    AWS_SECRET_ACCESS_KEY=your_secret_key
    AWS_REGION=your_region
    ```

---

## Install Dependencies

1. Copy the contents of `requirements.txt` from the artifact.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Upload Data to AWS

Upload the dataset to your S3 bucket:
```bash
aws s3 cp netflix_titles.csv s3://your-bucket-name/
```

---

## Deploy the Application

### Build the Docker Image
```bash
docker build -t netflix-dashboard .
```

### Run the Container
```bash
docker run -p 8050:8050 netflix-dashboard
```

---

## AWS Elastic Beanstalk Deployment

1. Install the EB CLI:
    ```bash
    pip install awsebcli
    ```
2. Initialize the EB project:
    ```bash
    eb init -p docker netflix-dashboard
    ```
3. Create an Elastic Beanstalk environment:
    ```bash
    eb create netflix-dashboard-env
    ```

---

## Access the Dashboard

- **Local:** Visit [http://localhost:8050](http://localhost:8050)
- **After EB deployment:** Use the provided EB URL

---

## Dashboard Features

The dashboard will display:

- Distribution of movies vs TV shows
- Content added by year
- Top 10 genres
- Rating distribution
- Average duration by type

---

