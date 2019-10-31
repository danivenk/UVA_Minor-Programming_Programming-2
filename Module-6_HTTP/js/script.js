// init() executes after DOMContent has been loaded
function init()
{
    // define the nav objects and finds the placeholder for the nav
    var nav_element = document.querySelector("#nav");
    var nav_objects = [["index", "Home"], ["page1", "Winner"],
        ["page2", "Runner Up"], ["page3", "Third place"]]

    // defines the content to be added to the placeholder
    var nav_content = '<button class="navbar-toggler" type="button" \
        data-toggle="collapse" data-target="#navbarNavAltMarkup" \
        aria-controls="navbarNavAltMarkup" aria-expanded="false" \
        aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span> \
        </button><div class="collapse navbar-collapse" id="navbarNavAltMarkup"> \
        <div class="navbar-nav">';

    // create a link to a page for each nav object and add it to nav_content
    for (object in nav_objects)
    {
        nav_content += '<a class="nav-item nav-link" href="' + 
            nav_objects[object][0] + '.html">' + nav_objects[object][1] + "</a>";
    }

    // close nav_content div
    nav_content += "</div>";

    // set push nav_content into nav_element
    nav_element.innerHTML = nav_content;
}
// make sure DOMContent is loaded before the code runs
document.addEventListener("DOMContentLoaded", init, false);