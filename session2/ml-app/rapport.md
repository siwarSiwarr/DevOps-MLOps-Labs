#  DevOps CI/CD Pipeline Report for Iris Classifier

## Author: CHEMLALI Siwar
## Date: 16/11/2025



## 1. Task 1: Project Preparation

**Description**: The Machine Learning project repository was successfully forked, cloned, and the required directory structure was verified before starting development.

Step1:
 **Repository Fork**  Forked the original repository to my public GitHub account.
 ![alt text](Images/Fork.PNG)


Stp2 :
**Local Structure** Cloned the repository and verified the project folder structure in VS Code, confirming the presence of `session2/ml-app`.
![alt text](Images/vs.PNG)
Step3:

**Requirements Check** |Confirmed the presence of the critical `requirements.txt` file for dependency management. get the files that end with .txt:

![alt text](Images/ReqTxt.PNG)

## 2. Task 2: Running the App Locally

**Description**: The local Python environment was set up, dependencies were installed, and the core ML application scripts (`train.py` and application server) were successfully executed.


|**Environment Setup**  Created and activated a virtual environment (`.venv`). Dependencies were installed using `pip install -r requirements.txt`.

![alt text](Images/VENV.PNG)

**Model Training** Ran `python src/train.py` to load the  dataset, train the Logistic Regression model, and evaluate it. pkl`.
![alt text](Images/trainpyy.PNG)

and Testing  the Tets_model:
![alt text](Images/model-test.PNG)



## 3. Task 3: Unit Tests

**Description**: Comprehensive unit tests were implemented using `pytest` to ensure code functionality and model reliability across various aspects (data loading, model training, prediction, and evaluation).


| **Core Tests** | Executed 6 core tests covering model initialization, training, prediction, evaluation, saving, and data loading (`test_model.py`).
![alt text](Images/model-test.PNG)
| **Additional Tests** | Executed 3 additional tests (`test_additional.py`) to verify prediction format, model accuracy threshold, and prediction range. 
![alt text](Images/task3.PNG)


| **Overall Result** | All 9 unit tests passed successfully in 20.49s. | ![All 9 tests passed]
![alt text](Images/tousTests.PNG)
---

## 4. Task 4: Linting & Formatting





| **Configuration File** | Created the `.flake8` configuration file 

To Make sure it's created successfully:
![alt text](Images/flak.PNG)

| **Detailed Output** | Ran the linter with `--statistics` to verify that no errors or warnings were found (`0` count)

## Task 5: GitHub Actions CI Workflow



**Description**: Created automated CI pipeline using GitHub Actions.



**Triggers**:

- Push to main/master branch

- Pull requests to main/master branch



**CI File location**: `.github/workflows/ci.yml`
**CI File Creation** | Created the `ci.yml` file inside the `.github/workflows/` directory.


![alt text](Images/task5.PNG)

![alt text](Images/githuuuuub.PNG)

**Git Push** | Successfully pushed all local changes, including the CI workflow file, to the remote GitHub repository

![alt text](Images/push.PNG)




**Pull Request** | Created and reviewed a Pull Request, where the CI workflow was triggered and passed successfully before merging.


![alt text](Images/testerGitHub.PNG)


**Workflow Success** | The final merge commit successfully triggered and passed the CI/CD Pipeline on the `main` branch.
![alt text](Images/mrge.PNG)





https://github.com/siwarSiwarr/DevOps-MLOps-Labs.git.


## Task 6: Containerization



**Description**: Dockerized the ML application.



**Dockerfile specifications**:

- Base image: python:3.12-slim

- Working directory: /app

- Exposes port: 5000

- Default command: Train model



**Commands used**:

(.venv) PS C:\...\ml-app> docker build -t ml-app-siwar .



![alt text](Images/dockerBuild.PNG)

![alt text](Images/Docker.PNG)



**2. Execute Training in the Container**


(.venv) PS C:\...\ml-app> docker run ml-app-siwar python src/train.py


![alt text](Images/DockR1.PNG)

![alt text](Images/dockR2.PNG)

![alt text](Images/DockR3.PNG)

Training Start and Evaluation: Shows the initial output, including the successful loading of the Iris dataset, training set sizes, and the resulting classification report and model accuracy (**0.9667**).Model Evaluation Details: Provides detailed precision, recall, and f1-score metrics for each class. It confirms that the training completed successfully and the model was saved to models/iris_classifier.pkl.Final Training Confirmation: A slightly expanded view of the final evaluation and model saving steps, reinforcing the successful completion of the training job inside the isolated Docker container.


**Docker Desktop Verification: Confirms that the ml-app-siwar image is present in the local Docker environment and is ready to be run as a container**

(.venv) PS C:\...\ml-app> docker run -p 5000:5000 ml-app-siwar

