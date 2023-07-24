
## Run Locally

Get Python

```bash
  Install python3 
```

Get Gcloud cli

```bash
  Install Gcloud Cli
```

Run Gcloud init

```bash
./google-cloud-sdk/bin/gcloud init
```

Create your credential file

```bash
gcloud auth application-default login
```

Make sure your user account has the correct credentials (service account needed for production)

```bash
Storage Admin (roles/storage.admin) - https://cloud.google.com/storage/docs/access-control/iam-roles#standard-roles
```

Clone the project

```bash
  git clone 
```

Install dependencies

```bash
  pip3 install -r requirements.txt
```

Run

```bash
  python3 pythonapp.py
```

If running locally or on a vm access app here: http://localhost:5000
    
Quit
```bash
  Ctrl + C
```

