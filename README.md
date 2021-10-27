# Garth Webb Programming Club - Check-in 2.0

The HDSB requires information for contact tracing before entering in-person club meetings. This program is to ease the process.

## How it works
This program will be run on a computer with a barcode scanner connected. The program will first pull all the data from the remote database into a local database.\
The barcode scanner will scan a student ID, and enter it into the program. The program will then check if the user already exists in the (local) database.\
If the user does not, the user will be asked to provide their information. The program then saves it to the (local) database.\
If the user does exist, the user will be checked into the system (local database).\
Once all the data is pushed (when button pressed or when app is closed), all the information on the local database is sent to the remote database and contact tracing Google Sheet.

## Note:
This is meant to be an internal application. It is not *super* efficient, because the code runs procedurally rather than asynchronally. The TS/JS GUI runs Python scripts to do all the work, rather than doing it in the same code.\
The purpose of this is to replace another check-in, that pushes to the remote database everytime rather than storing it locally and pushing it all together.\
Feel free to fork and optimize/update code.

## How to run it
1. Ensure that you have the `creds.json` and `.env` files.
2. Ensure that you have the latest supported version of [Node.js](https://nodejs.org/en/) and [Python](https://www.python.org/downloads/) installed.

You have the option of either running the program automatically, or manually.

### Automatically:
Run the following command:

For Mac/Linux:
```
./start
```
For Windows:
```
start.bat
```

### Manually:
1. Install the requirements by running `npm install` and `pip install -r requirements.txt`.
2. Compile the TypeScript code by running `npx tsc`.
3. Start the program by running `npm start`.