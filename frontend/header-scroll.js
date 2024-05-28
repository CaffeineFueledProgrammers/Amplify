window.onscroll = function () {
    scrollFunction();
};

/*
 * This function applies the `navbar-minimized` class to `navbar-title` ID
 * when the user scrolls 80 pixels down.
 */
function scrollFunction() {
    var navbar = document.getElementById("navbar-title");
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
        navbar.classList.add("navbar-minimized");
        navbar.classList.remove("navbar-normal");
    } else {
        navbar.classList.remove("navbar-minimized");
        navbar.classList.add("navbar-normal");
    }
}
