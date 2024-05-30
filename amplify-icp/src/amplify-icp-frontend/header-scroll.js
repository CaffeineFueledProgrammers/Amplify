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

document.addEventListener('DOMContentLoaded', () => {
    const faders = document.querySelectorAll('.fade-in');

    const appearOptions = {
        threshold: 0.5, /* Adjust this value based on when you want the animation to trigger */
        rootMargin: "0px 0px -50px 0px"
    };

    const appearOnScroll = new IntersectionObserver((entries, appearOnScroll) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('visible');
                appearOnScroll.unobserve(entry.target);
            }
        });
    }, appearOptions);

    faders.forEach(fader => {
        appearOnScroll.observe(fader);
    });
});