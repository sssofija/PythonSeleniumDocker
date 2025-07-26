# Python + Selenium + Docker + Allure

This project demonstrates how to run automated tests written in Python using Selenium within Docker containers. After test execution, an Allure report is generated.

##  Technologies Used

- Python 3.11  
- Selenium WebDriver  
- Docker 
- Allure Framework  

---

##  Containerization

The project uses the following files to work with Docker:

- `Dockerfile` — defines the environment for running tests  
- `docker-compose.yml` — sets up the services (Selenium + test runner) and their interaction  

These files allow for quick setup and isolated execution of tests in a containerized environment.

---

##  How to Run

### 1. Build and start the project:
   ```bash
   docker-compose up --build
   
````

### 2. After the tests finish, an `allure-results` directory will be created.

### 3. To view the test report:

   ```bash
   allure serve allure-results

   ```

> ⚠️ Make sure [Allure Commandline](https://docs.qameta.io/allure/#_installing_a_commandline) is installed on your system.

---

