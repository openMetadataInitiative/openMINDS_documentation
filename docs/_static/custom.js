
window.onload = function() {
    let currentVersion = document.getElementsByClassName("rst-current-version")[0];
    currentVersion.innerHTML = currentVersion.innerHTML.replace(/\n/g, '').replace(/.*v: /m, '').trim();
    let navig = document.getElementsByClassName("wy-side-nav-search")[0];
    navig.appendChild(document.getElementsByClassName("rst-versions")[0]);
    currentVersion.style.display =  "block";

  };