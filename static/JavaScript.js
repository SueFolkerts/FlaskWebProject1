
    function placeEars() {
            if (document.getElementById("EarsX").src.includes("NoImage")) {
                return
            }
            else {
                var head = document.getElementById("Heads").src;
                if (head.includes('Head1.jpg')) {
        document.getElementById("EarsX").style.left = "9em";
                    document.getElementById("EarsY").style.left = "85em";
                } else if (head.includes('Head2.jpg')) {
        document.getElementById("EarsX").style.left = "10em";
                    document.getElementById("EarsX").style.top = "35em";
                    document.getElementById("EarsY").style.left = "82em";
                    document.getElementById("EarsY").style.top = "35em";
                    document.getElementById("EarsX").style.transform = 'rotate(25deg)';
                    document.getElementById("EarsY").style.transform = 'rotate(-25deg)';
                } else if (head.includes('Head4.jpg')) {
        document.getElementById("EarsX").style.top = "35em";
                    document.getElementById("EarsX").style.transform = 'rotate(40deg)';
                    document.getElementById("EarsY").style.top = "35em";
                    document.getElementById("EarsY").style.transform = 'rotate(-40deg)';
                } else if (head.includes('Head5.jpg')) {
        document.getElementById("EarsX").style.left = "8em";
                    document.getElementById("EarsX").style.top = "55em";
                    document.getElementById("EarsX").style.transform = 'rotate(-30deg)';
                    document.getElementById("EarsY").style.left = "84em";
                    document.getElementById("EarsY").style.top = "51em";
                    document.getElementById("EarsY").style.transform = 'rotate(30deg)';
                } else if (head.includes('Head6.jpg')) {
        document.getElementById("EarsX").style.left = "10em";
                    document.getElementById("EarsX").style.transform = 'rotate(-20deg)';
                    document.getElementById("EarsY").style.transform = 'rotate(20deg)';
                } else if (head.includes('Head7.jpg')) {
        document.getElementById("EarsX").style.left = "18em";
                    document.getElementById("EarsX").style.transform = 'rotate(-25deg)';
                    document.getElementById("EarsY").style.left = "79em";
                    document.getElementById("EarsY").style.transform = 'rotate(25deg)';
                } else if (head.includes('Head8.jpg')) {
        document.getElementById("EarsX").style.left = "5em";
                    document.getElementById("EarsX").style.top = "53em";
                    document.getElementById("EarsY").style.left = "90em";
                    document.getElementById("EarsY").style.top = "53em";
                } else if (head.includes('Head9.jpg')) {
        document.getElementById("EarsY").style.left = "86em";
                } else if (head.includes('Head10.jpg')) {
        document.getElementById("EarsX").style.left = "5em";
                    document.getElementById("EarsX").style.transform = 'rotate(20deg)';
                    document.getElementById("EarsY").style.left = "88em";
                    document.getElementById("EarsY").style.transform = 'rotate(-20deg)';
                } else if (head.includes('Head11.jpg')) {
        document.getElementById("EarsX").style.left = "10em";
                    document.getElementById("EarsX").style.transform = 'rotate(-20deg)';
                    document.getElementById("EarsY").style.left = "80em";
                    document.getElementById("EarsY").style.transform = 'rotate(20deg)';
                } else if (head.includes('Head12.jpg')) {
        document.getElementById("EarsX").style.left = "6em";
                    document.getElementById("EarsY").style.left = "88em";
                } else if (head.includes('Head13.jpg')) {
        document.getElementById("EarsX").style.transform = 'rotate(-20deg)';
                    document.getElementById("EarsY").style.left = "83em";
                    document.getElementById("EarsY").style.transform = 'rotate(20deg)';
                } else if (head.includes('Head14.jpg')) {
        document.getElementById("EarsX").style.top = "40em";
                    document.getElementById("EarsX").style.left = "22em";
                    document.getElementById("EarsY").style.top = "40em";
                    document.getElementById("EarsY").style.left = "72em";
                } else if (head.includes('Head15.jpg')) {
        document.getElementById("EarsX").style.left = "6em";
                    document.getElementById("EarsX").style.transform = 'rotate(26deg)';
                    document.getElementById("EarsY").style.left = "84em";
                    document.getElementById("EarsY").style.transform = 'rotate(-26deg)';
                } else if (head.includes('Head16.jpg')) {
        document.getElementById("EarsX").style.top = "40em";
                    document.getElementById("EarsX").style.left = "11em";
                    document.getElementById("EarsX").style.transform = 'rotate(20deg)';
                    document.getElementById("EarsY").style.top = "40em";
                    document.getElementById("EarsY").style.left = "84em";
                    document.getElementById("EarsY").style.transform = 'rotate(-20deg)';
                }
            }
        }

        //function PrintDiv() {
        //    var divContents = document.getElementById("picture").innerHTML;
        //    var oldPage = document.body.innerHTML;

        //    //Reset the page's HTML with div's HTML only
        //    document.body.innerHTML =
        //        '<html><head><style>body {align - content:center;}</style></head><body>' +
        //        divContents + "</body>";
        //    console.log(document.body.innerHTML);
        //    console.log(document.body.outerHTML);
        //    //Print Page
        //    window.print();

        //    //Restore orignal HTML
        //    document.body.innerHTML = oldPage;
        //}


