# Post Office Finder Web Application

### Installing Python (Windows)

1. Download the latest Python installer from [python.org](https://www.python.org/downloads/windows/)
2. Run the installer
3. **Important:** Check the box that says "Add Python to PATH"
4. Click "Install Now"
5. Verify installation by opening Command Prompt and typing:
   ```bash
   python --version
   ```
   You should see the Python version number

### Installing Git (Windows)

1. Download Git for Windows from [git-scm.com](https://git-scm.com/download/win)
2. Run the installer with default options (or customize as needed)
3. Verify installation by opening Command Prompt and typing:
   ```bash
   git --version
   ```
   You should see the Git version number

## Setup Instructions

1. Folder with Web app using this git repo.

2. Log in to your Google Cloud account: [https://console.cloud.google.com/](https://console.cloud.google.com/)

2. Install Google Cloud SDK: [https://cloud.google.com/sdk/docs/install-sdk#windows](https://cloud.google.com/sdk/docs/install-sdk#windows)

3. Create a new project in Google Cloud Console(Optional).

4. Initialize Gcloud SDK:
   ```bash
   gcloud init
   ```
5. Follow the prompts to:
   - Select your Google account
   - Select the created project or create a new one

6. Ensure your account has the "Storage Admin" role for the project:
   - Go to the IAM & Admin section in the Google Cloud Console
   - Find your account and assign the "Storage Admin" role
7. cd into the web app directory and deploy

   ```bash
   gcloud app deploy
   ```

   ```bash
   gcloud app browse
   ``` 


This will open your default browser and navigate to your application's URL.


## To run the application locally:
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Other Useful Commands

```bash
gcloud auth login                      # Authenticates your Google Cloud account in the CLI
gcloud auth list                      # Lists all credentialed accounts
gcloud config set project PROJECT_ID  # Sets the active Google Cloud project
gcloud config list                    # Displays current configuration settings
gcloud config configurations list     # Lists all available configurations


gcloud components update                     # Updates all Cloud SDK components
gcloud components list                       # Lists all components and their status
gcloud components install COMPONENT_NAME     # Installs a specific component
gcloud components remove COMPONENT_NAME      # Removes a specific component


gcloud app deploy                                      # Deploys the app to App Engine
gcloud app deploy --project PROJECT_ID                # Deploys to a specific project
gcloud app deploy --version VERSION_ID                # Deploys with a specific version
gcloud app deploy --no-promote                        # Deploys without routing traffic
gcloud app browse                                     # Opens the deployed app in browser
gcloud app browse --project=PROJECT_ID               # Opens a specific project’s app


python -m venv venv                          # Creates a virtual environment
source venv/bin/activate                    # Activates virtual env (Linux/Mac)
venv\Scripts\activate                       # Activates virtual env (Windows)
pip install -r requirements.txt             # Installs required packages
python main.py                              # Runs the app locally

