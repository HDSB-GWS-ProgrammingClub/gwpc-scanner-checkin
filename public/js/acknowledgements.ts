const openSourceData = [
    // GitHub repos in alphabetical order
    "benjaminp/six",
    "burnash/gspread",
    "certifi/python-certifi",
    "electron/electron",
    "etingof/pyasn1",
    "etingof/pyasn1-modules",
    "googleapis/google-auth-library-python",
    "googleapis/google-auth-library-python-oauthlib",
    "googleapis/oauth2client",
    "httplib2/httplib2",
    "kjd/idna",
    "microsoft/TypeScript",
    "mongodb/mongo-python-driver",
    "motdotla/dotenv",
    "oauthlib/oauthlib",
    "psf/requests",
    "pyparsing/pyparsing/",
    "requests/requests-oauthlib",
    "sindresorhus/electron-reloader",
    "sybrenstuvel/python-rsa/",
    "theskumar/python-dotenv",
    "tkem/cachetools/",
    "urllib3/urllib3"
]

const openSourceDiv = document.getElementById("open-source");

const getRepoURL = (repoName: string) => {
    return `https://github.com/${repoName}`;
}

for (let i = 0; i < openSourceData.length; i++) {
    // Create <a> tag
    let a = document.createElement('a');
    a.href = '#';
    a.className = 'text-center text-info';
    a.addEventListener('click', () => require('electron').shell.openExternal(getRepoURL(openSourceData[i])))

    // Create <h5> tag
    let h5 = document.createElement('h6');
    h5.textContent = openSourceData[i];

    // Put on screen
    a.appendChild(h5);
    openSourceDiv?.appendChild(a);
}