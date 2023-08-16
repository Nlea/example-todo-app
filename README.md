# example-todo-app
This is an application that simulates the backend of an todo list in combination with autometrics-py and the Autometrics explorer

To run the demo you can download the [Autometrics CLI](https://docs.autometrics.dev/local-development#getting-started-with-am). 

Navigate to the project folder and start the Python application from the main.py file: 

```
uvicorn main:app
```

The app will start on port 8000. From the same directory start up Autometrics Explorer and a Proemtheus instance using

```
am start :8000
```
This will create a .autometrics folder in your directory. Make sure you delete it if you want to start with fresh data

Now run the script to generate traffic to your endpoint
```
python3 script/traffic.py
```

Now you can open the autometrics Explorer and inspect your metrics. 
