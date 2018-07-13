# Fibonacci application 
Python application to calculate Fibonacci sequence

## Getting Started
Clone the repository using command line 

1.Navigate to your repository’s Code tab.

2.Click Clone or download.

3.Copy the URL provided.

4.Open your command line or Terminal application and enter the directory where you would like to copy the repository.
```
cd ~/
```
5.Clone the repository by replacing <URL> with clone URL you copied in the previous step. The repository will be cloned into a new directory in this location.
```
git clone <URL>
```

### Prerequisites

1.Activate virtual environment

```
source fib_application/bin/activate
```
2.Install requirements

```
pip3 install -r requirements.txt 
```
3.If you are done working in the virtual environment for the moment, you can deactivate it:

```
deactivate
```
## Running the tests

Run tests

1.Give execute permission to your script

```
chmod +x run_tests.sh

```
2. Run script from root directory
```
./run_tests.sh
```

### Running application

1. Run app from root directory
```
python3 app.py 
```
In app.py just change **number_of_terms** to run app for different values
