# Garth Webb Programming Club - Check-in 2.0

The HDSB requires information for contact tracing before entering in-person club meetings. This program is to ease the process.

## How it works
This program will be run on a computer with a barcode scanner connected. The barcode scanner will scan a student ID, and enter it into the program. The program will then check if the user already exists in the database.\
If the user does not, the user will be asked to provide their information. The program then saves it to the database.\
If the user does exist, the user will be checked into the system, and their information will be sent to the contact tracing Google Sheet.

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