const { ipcRenderer } = require('electron');

// Get form object and student ID
const checkin_form = document.getElementById("checkin-form");
const getStudentID = () => { return Number((<HTMLInputElement>document.getElementById("form-studentid")).value) };

const userExists = (studentID: number) => {
    const stdout = execSync(`${pythonCommand} ./scripts/checkUserExists.py ${studentID}`);
    return (stdout.toString().includes('true'));
}

const getCurrentTime = () => {
    let current_time = new Date();
    return `${current_time.toLocaleDateString()} ${current_time.toLocaleTimeString()}`;
}

const checkin = (studentID: number) => {
    let currentTime = getCurrentTime();
    // Check in user
    const stdout = execSync(`${pythonCommand} ./scripts/checkinUser.py ${studentID} "${currentTime}"`);
    // Confirmation dialog
    ipcRenderer.send('userCheckedInConfirm', stdout.toString(), currentTime);
}

const createNewUserWindow = (studentID: number) => {
    ipcRenderer.send('createNewUserWindow', studentID);
}

// Push data
document.getElementById("push-data")?.addEventListener('click', (event) => {
    ipcRenderer.send('updateData');
})

// On check-in form submit
checkin_form?.addEventListener('submit', (event) => {
    event.preventDefault();
    document.getElementById("checkin-btn")!.innerHTML = 'Processing...';
    let studentID = getStudentID();
    if (userExists(studentID))
        checkin(studentID);
    else
        createNewUserWindow(studentID);
    document.getElementById("checkin-btn")!.innerHTML = 'Check in';

})

// Credits page
document.getElementById("acknowledgements-link")?.addEventListener('click', (event) => {
    ipcRenderer.send('showAcknowledgementsWindow');
})