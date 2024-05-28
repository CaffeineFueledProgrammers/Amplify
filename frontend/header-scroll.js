// NOTE: pakitanggal nalang if it's not yet working.
window.onscroll = function() {scrollFunction();};

/*
 * This function applies the `header-hidden` class to `header-title` ID
 * when the user scrolls 80 pixels down.
 */
function scrollFunction()
{
    // TODO: Implement `header-hidden` class.
    var header_title = document.getElementById("header-title");
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80)
    {header_title.classList.add("header-hidden");}
    else {header_title.classList.remove("header-hidden");}
}
