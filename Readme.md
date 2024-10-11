## Task Management App with Flask and SQLite

This project is a simple task management app built with Flask, SQLite, and Python. It provides REST APIs to create, retrieve, update, and delete tasks, with future support for user management. This guide will walk you through setting up the project, running the app, and running the test suite.

---

### **1. Prerequisites**

#### **1.1 Install Git**

You need Git to clone the repository and manage version control.

- **Mac**: Git comes pre-installed. If not, install it using Homebrew:
```
brew install git
```

- **Linux**: Install Git with the following command:
```
sudo apt-get install git
```

- **Windows**: Download and install Git from [Git for Windows](https://git-scm.com/download/win).

Once installed, verify the installation:
```
git --version
```

#### **1.2 Install Conda**

We recommend using **Anaconda** or **Miniconda** to manage Python environments. Follow these steps to install Conda:

- **Mac/Linux**:
  1. Download the latest version of **Miniconda** from [here](https://docs.conda.io/en/latest/miniconda.html).
  2. Open a terminal and run the installation script:
```
bash Miniconda3-latest-MacOSX-x86_64.sh  # For Mac
bash Miniconda3-latest-Linux-x86_64.sh   # For Linux
```
  3. Follow the prompts and restart your terminal once the installation completes.

- **Windows**:
  1. Download the installer from [here](https://docs.conda.io/en/latest/miniconda.html).
  2. Run the installer and follow the instructions.
  3. Once installed, search for **Anaconda Prompt** and open it.

Verify the installation by checking the version:
```
conda --version
```

---

### **2. Setting Up the Project**

#### **2.1 Clone the Repository**

Use Git to clone the repository:
```
git clone https://github.com/Agyey/task-manager-flask.git
cd task-manager-flask
```

#### **2.2 Set Up Python Environment**

1. **Create a Conda environment**:
```
conda create -n task-manager python=3.9
```

2. **Activate the environment**:
   - On **Mac/Linux**:
```
conda activate task-manager
```
   - On **Windows**:
```
activate task-manager
```

3. **Install required dependencies**:
   Navigate to the project folder (if not already there):
```
cd task-manager-flask
```

   Then, install the dependencies using `pip`:
```
pip install -r requirements.txt
```

   If a `requirements.txt` file doesn’t exist, manually install the key dependencies:
```
pip install Flask Flask-Testing
```

---

### **3. Running the Task Management App**

Once the environment is set up and the dependencies are installed, you can run the Flask app.

1. **Run the app**:
```
python app.py
```

2. **Access the app**:
   Open your browser and go to:
   http://127.0.0.1:5000


You should see the app running, and you can interact with the task management system through the available API endpoints.

### **4. Testing the Task Management App**

We’ve provided unit tests to ensure that the APIs are functioning correctly. To run the tests, follow these steps:

1. **Run the tests**:
```
python -m unittest tests.py
```

2. **Check the output**:
If everything is working correctly, you should see output similar to the following:
```
......
Ran 6 tests in 0.400s

OK
```


This indicates that all tests have passed successfully.

---

### **5. Additional Information**

#### **5.1 Common Commands**

- **To deactivate the Conda environment**:
- Mac/Linux:
```
conda deactivate
```
- Windows:
```
deactivate
```

- **To update the Conda environment with new dependencies**:
```
conda install <package-name>
```

---

### **6. Project Structure**

```
task-manager-flask/
│
├── app.py              # Main Flask application
├── models.py           # Database models for Task and User
├── tests.py            # Unit tests for the Task Management APIs
├── tasks.db            # SQLite database file (auto-generated)
└── README.md           # This file
```

---

### **7. Available API Endpoints**

The following API endpoints are currently available for task management:

- **POST /tasks**: Add a new task.
- **GET /tasks**: Get all tasks.
- **GET /tasks/<id>**: Get a specific task by ID.
- **PUT /tasks/<id>**: Update a task.
- **DELETE /tasks/<id>**: Delete a task.

**Future endpoints for user management** will be implemented soon.

---

### **8. Troubleshooting**

If you encounter issues during setup or running the app, here are some troubleshooting tips:

- **Database Issues**: If the SQLite database (`tasks.db`) is corrupted or outdated, delete it, and the app will automatically create a new one when run.
  
- **Dependency Issues**: If `pip install -r requirements.txt` fails, ensure you’re using the correct Python version (`3.9` or higher) in your Conda environment.

---

### **9. Contributing**

If you'd like to contribute to this project, please fork the repository, create a feature branch, and submit a pull request.

```
git checkout -b new-feature
git add .
git commit -m "Add new feature"
git push origin new-feature
```