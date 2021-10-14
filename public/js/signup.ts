// Get student ID and insert into form
const querystring = require('querystring');
let data = JSON.parse(querystring.parse(global.location.search)['?data']);
(<HTMLInputElement>document.getElementById("form-studentid")).value = data['studentID'];

const validateUserInfo = (name: string, email: string, phonenumber: number, address: string, studentID: number) => {
    let message = '';

    if (name.length < 1 || name == '')
        message = 'Please enter your full name';
    else if (!email.match(/[a-zA-Z0-9]+@hdsb.ca/))
        message = 'Please enter your school email address';
    else if (address.length < 1 || address == '')
        message = 'Please enter your address';
    
    return message;
}

// On submit
const signup_form = document.getElementById("signup-form");

signup_form?.addEventListener('submit', (event) => {
    event.preventDefault();

    // Get data
    let name = (<HTMLInputElement>document.getElementById("form-name")).value;
    let email = (<HTMLInputElement>document.getElementById("form-email")).value;
    let phonenumber = Number((<HTMLInputElement>document.getElementById("form-phonenumber")).value);
    let address = (<HTMLInputElement>document.getElementById("form-address")).value;
    let studentID = Number((<HTMLInputElement>document.getElementById("form-studentid")).value);

    let user = {name, email, phonenumber, address, studentID};

    document.getElementById("checkin-btn")!.innerHTML = 'Processing...';

    let invalidUserInfo = validateUserInfo(name, email, phonenumber, address, studentID)
    if (invalidUserInfo) {
        ipcRenderer.send('userSignupInvalid', invalidUserInfo)
        document.getElementById("checkin-btn")!.innerHTML = 'Sign up';
    } else {
        // Create user
        let stdout = execSync(`${pythonCommand} ./scripts/createNewUser.py ${JSON.stringify(user)}`);
        ipcRenderer.send('confirmUserCreated', stdout.toString());
        window.close();
    }
})