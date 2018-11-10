function CreateTableFromJSON(data) {
        // EXTRACT VALUE FOR HTML HEADER.
        let col = [];
        for (let i = 0; i < data.length; i++) {
            for (let key in data[i]) {
                if (col.indexOf(key) === -1) {
                    col.push(key);
                }
            }
        }

        // CREATE DYNAMIC TABLE.
        let table = document.createElement("table");

        // CREATE HTML TABLE HEADER ROW USING THE EXTRACTED HEADERS ABOVE.
        let tr = table.insertRow(-1);                   // TABLE ROW.

        for (let i = 0; i < col.length; i++) {
            let th = document.createElement("th");      // TABLE HEADER.
            th.innerHTML = col[i];
            tr.appendChild(th);
        }

        // ADD JSON DATA TO THE TABLE AS ROWS.
        for (let i = 0; i < data.length; i++) {
            tr = table.insertRow(-1);
            for (let j = 0; j < col.length; j++) {
                let tabCell = tr.insertCell(-1);
                tabCell.innerHTML = data[i][col[j]];
            }
        }

        // ADD THE NEWLY CREATED TABLE WITH DATA TO CONTAINER.
        let divContainer = document.getElementById("showTable");
        divContainer.innerHTML = "";
        divContainer.appendChild(table);


        // ADD THE NEWLY CREATED DROPDOWN WITH TABLE HEADER TO CONTAINER
        let $ths = $("th").map(function() {
        return "<option>" + $.trim($(this).text()) + "</option>"
        }).get();
        $("select").append($ths.join(""));




}

function HideNShow() {

    let $select = $("select");

    //Remove based on button click
    let $option = $select.find(":selected");
    let selected = $option.text();

    // To update the list after removal of the column
    $option.remove();
    if ($select.is(':empty')) {
        $select.remove();
        $(this).remove();
    }
    // let stuff = $('table').find("th:contains('" + selected + "')");

    //remove the table col
    let $this = $('table').find("th:contains('" + selected + "')");
    let index = $this.index();
    if ( $this[0].tagName === "TD" ) {
        $('table').find("th").eq(index).remove();
    } else {
        $this.remove();
    }
    $('table').find("tr").each(function() {
        $(this).find("td").eq(index).remove();
    });

}

function rearrange(){

}