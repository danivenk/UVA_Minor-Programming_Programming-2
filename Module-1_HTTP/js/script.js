var SITE = "https://mprog.hakkajiten.com/module-1_http/"

function init()
{
    var nav_element = document.querySelector("#nav");
    var nav_objects = [["index", "Home"], ["index", "Home"], ["index", "Home"], ["index", "Home"]]

    var nav_content = '<div class="nav-bar">';
    for (object in nav_objects)
    {
        nav_content += '<a class="nav-item nav-link" href="' + nav_objects[object][0] + '.html">' + nav_objects[object][1] + "</a>";
    }

    nav_content += "</div>";

    nav_element.innerHTML = nav_content;
}
document.addEventListener("DOMContentLoaded", init, false);