
function addId() {
    if (document.getElementById("EarsX").src.includes("NoImage")) {
        console.log("no image ");
        return;
    }
    else {
        var EarsX = document.getElementById("EarsX");
        var EarsY = document.getElementById("EarsY");
        EarsX.id = "EarsX";
        EarsY.id = "EarsY";
        var head = document.getElementById("Heads").src;
        pos = head.indexOf("/Heads/");
        namePart = head.substring((pos + 7), (pos + 7 + 6))
        namePart = namePart.replace('.', '');
        EarsX.classList.add(namePart + 'X');
        EarsY.classList.add(namePart + 'Y');
        console.log("class list " + document.getElementById("EarsX").classList);
    }
}

function AddId() {
    console.log("hello");
}

function PrintDiv() {
    var divContents = document.getElementById("picture").outerHTML;
    var oldPage = document.body.innerHTML;
    //Reset the page's HTML with div's HTML only
    var newContent = '<head><meta charset = "utf-8"/><link rel="stylesheet" type="text/css" href="/static/styles.css"></head>'
    newContent += '<body> ' + divContents + '</body> ';
    document.open();
    document.write(newContent);
    document.close();
    //Print Page
    window.print();

    //Restore orignal HTML
    document.body.innerHTML = oldPage;
    document.location.reload();
}


