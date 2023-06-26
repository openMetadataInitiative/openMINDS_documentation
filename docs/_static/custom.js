
window.onload = function() {
    let currentVersion = document.getElementsByClassName("rst-current-version")[0];
    currentVersion.innerHTML = currentVersion.innerHTML.replace(/\n/g, '').replace(/.*v: /m, '').trim();
  };