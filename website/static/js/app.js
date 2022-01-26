console.log("oi! - app.js")

// slide-out nav
function openNav() {
    document.getElementById('mySidenav').style.width="250px";
    document.getElementById('closeBtn').style.display="initial";
}

function closeNav() {
    document.getElementById('mySidenav').style.width="0";
    document.getElementById('closeBtn').style.display="none";
}

// drop down MyFiles
function openMyFilesDropdown() {
    document.getElementById("myFilesDropdownContent").classList.toggle("show");
}