// init() executes after DOMContent has been loaded
function init()
{
    // define the nav objects and finds the placeholder for the nav
    var nav_element = document.querySelector("#nav");
    var nav_objects = [["index", "Home"], ["index", "Home"],
        ["index", "Home"], ["index", "Home"]]

    // defines the content to be added to the placeholder
    var nav_content = '<div class="nav-bar">';

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