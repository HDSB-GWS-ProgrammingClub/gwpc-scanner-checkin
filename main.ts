const { app, BrowserWindow, ipcMain, dialog } = require('electron');
require('electron-reloader')(module);
const { execSync } = require('child_process');
require('dotenv').config();

/* Initialize Electron app ------------------------------------------------- */

const createMainWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
            devTools: false
        }
    });
    win.removeMenu()
    win.loadFile('./views/index.html');
}

const pythonCommand = process.platform === "win32" ? "py" : "python3";

// Update data
const updateData = () => {
    execSync(`${pythonCommand} ./scripts/pushData.py`);
    execSync(`${pythonCommand} ./scripts/pullData.py`);
}
// Push data on window close
app.on('window-all-closed', () => {
    dialog.showMessageBox({
        message: 'Updating data',
        type: 'info'
    })
    updateData();
})
ipcMain.on('updateData', (event: any) => {
    updateData();
    dialog.showMessageBox({
        message: 'Data has been updated',
        type: 'info'
    });
})

// Run app
app.whenReady().then(() => {
    createMainWindow();
    execSync(`${pythonCommand} ./scripts/pullData.py`);
})

/* ------------------------------------------------------------------------- */



/* On user scan ------------------------------------------------------------ */

// User check-in confirm
ipcMain.on('userCheckedInConfirm', (event: any, name: string, currentTime: string) => {
    dialog.showMessageBox({
        message: `Checked in ${name} at ${currentTime}`,
        type: 'info'
    })
})

/* ------------------------------------------------------------------------- */



/* New user sign-up -------------------------------------------------------- */

// Open window for new user
const newUserWindow = (studentID: number) => {
    let data = {studentID: studentID};

    const win = new BrowserWindow({
        width: 575,
        height: 575,
        frame: false,
        resizable: false,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
            devTools: false
        }
    });
    win.removeMenu()
    win.loadFile('./views/signup.html', {query: {'data': JSON.stringify(data)}});
}
// Open window on frontend submit
ipcMain.on('createNewUserWindow', (event: any, studentID: number) => {
    newUserWindow(studentID);
});
ipcMain.on('confirmUserCreated', (event: any, msg: string) => {
    dialog.showMessageBox({
        message: msg,
        type: 'info'
    })
})
ipcMain.on('userSignupInvalid', (event: any, msg: string) => {
    dialog.showMessageBox({
        message: msg,
        type: 'error'
    })
})

/* ------------------------------------------------------------------------- */



/* Open acknowledgements ------------------------------------------------------------ */

// Open acknowledgements window
const openAcknowledgementsWindow = () => {

    const win = new BrowserWindow({
        width: 600,
        height: 700,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
            devTools: false
        }
    });
    win.removeMenu()
    win.loadFile('./views/acknowledgements.html');
}
// Open window on frontend url click
ipcMain.on('showAcknowledgementsWindow', (event: any) => {
    openAcknowledgementsWindow();
});

/* ------------------------------------------------------------------------- */



/* Offline ---------------------------------------------------------------- */

// Offline error message
ipcMain.on('offlineErrorMessage', (event: any) => {
    dialog.showMessageBox({
        message: 'You are currently offline.',
        type: 'error'
    })
})

// Back online confirmation message
ipcMain.on('onlineConfirmationMessage', (event: any) => {
    dialog.showMessageBox({
        message: 'You are back online. Please restart the application.',
        type: 'info'
    })
})

/* ------------------------------------------------------------------------- */