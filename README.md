Dashboard will show:

Distribution of movies vs TV shows
Content added by year
Top 10 genres
Rating distribution
Average duration by type

Instructions:

Install dependencies

pip install -r requirements.txt

upload data to your AWS bucket

aws s3 cp netflix_titles.csv s3://bucket_name/

Build docker image

docker build -t netflix-dashboard

Run the container

docker run -p 8050:8050 netflix-dashboard

Access dashboard

http://localhost:8050


Optional: AWS Elastic Beanstalk Deployment

Install EB CLI

pip install awsebcli

Initialize the project:

eb init -p docker netflix-dashboard
eb create netflix-dashboard-env# Netflix-Dashboard
