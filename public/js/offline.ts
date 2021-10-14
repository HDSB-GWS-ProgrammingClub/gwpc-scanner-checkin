// Show back online confirmation message
const online = () => {
    ipcRenderer.send('onlineConfirmationMessage');
    location.reload();
}

// Show offline error message
const offline = () => {
    window.addEventListener('online', online);
    ipcRenderer.send('offlineErrorMessage');
}

// If already offline
if (!navigator.onLine)
    offline();

// If goes offline
window.addEventListener('offline', offline);