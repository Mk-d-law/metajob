# Job Portal XML Feed META INTEGRATION 

This project generates an XML job feed for integration with Meta Jobs.

## Requirements

- Python 3.10+
- Django 3.x
- lxml
- requests

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/mk-d-law/metajob.git
    cd jobportal
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Django Settings:**
    - Set up your `settings.py` file for your Django project.
    - Ensure you have `ALLOWED_HOSTS` configured properly:
      ```python
      ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'your-domain.com']
      ```

## Usage

1. **Run Database Migrations:**
    ```bash
    python manage.py migrate
    ```

2. **Create a Superuser:**
    ```bash
    python manage.py createsuperuser
    ```

3. **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```

4. **Access the Admin Interface:**
    - Navigate to `http://127.0.0.1:8000/admin/`
    - Log in with the superuser credentials you created.
    - Add job entries via the admin interface.

5. **Generate and Download the XML Feed:**
    - Access the job feed URL for URL or it will be auto generated inside media folder.
      ```bash
      http://127.0.0.1:8000/jobs/job_feed
      ```

## Validation

To validate the XML file generated against the Meta Jobs schema, follow these steps:

1. **Install xmllint:**
    - On MacOS and many Linux distributions, xmllint is pre-installed. For Windows, use the following commands in the Windows Subsystem for Linux (WSL) or Git Bash:
      ```bash
      sudo apt-get update
      sudo apt-get install libxml2-utils
      ```

2. **Download the XSD Schema:**
    ```bash
    curl -LsS "https://fb.me/jobs_feed_validator.xsd" > "jobs_feed_validator.xsd"
    ```

3. **Save the XML File Locally:**
    - Download your generated XML file from the URL provided in the usage step and save it as `example_job_feed.xml`.

4. **Validate the XML File:**
    ```bash
    xmllint --schema "jobs_feed_validator.xsd" --noout "example_job_feed.xml"
    ```

    - If everything is correct, you will see:
      ```
      example_job_feed.xml validates
      ```
    - Otherwise, you will see validation errors with line numbers.

