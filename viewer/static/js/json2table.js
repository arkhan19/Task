function CreateTableFromJSON(data) {
        // EXTRACT VALUE FOR HTML HEADER.
        var col = [];
        for (var i = 0; i < data.length; i++) {
            for (var key in data[i]) {
                if (col.indexOf(key) === -1) {
                    col.push(key);
                }
            }
        }

        // CREATE DYNAMIC TABLE.
        var table = document.createElement("table");

        // CREATE HTML TABLE HEADER ROW USING THE EXTRACTED HEADERS ABOVE.
        var tr = table.insertRow(-1);                   // TABLE ROW.

        for (var i = 0; i < col.length; i++) {
            var th = document.createElement("th");      // TABLE HEADER.
            th.innerHTML = col[i];
            tr.appendChild(th);
        }

        // ADD JSON DATA TO THE TABLE AS ROWS.
        for (var i = 0; i < data.length; i++) {
            tr = table.insertRow(-1);
            for (var j = 0; j < col.length; j++) {
                var tabCell = tr.insertCell(-1);
                tabCell.innerHTML = data[i][col[j]];
            }
        }

        // ADD THE NEWLY CREATED TABLE WITH DATA TO CONTAINER.
        var divContainer = document.getElementById("showTable");
        divContainer.innerHTML = "";
        divContainer.appendChild(table);


        // ADD THE NEWLY CREATED DROPDOWN WITH TABLE HEADER TO CONTAINER
        var $ths = $("th").map(function() {
        return "<option>" + $.trim($(this).text()) + "</option>"
        }).get();
        $("select").append($ths.join(""));




}

function HideNShow() {

    var $select = $("select");

    //Remove based on button click
    var $option = $select.find(":selected");
    var selected = $option.text();

    // To update the list after removal of the column
    $option.remove();
    if ($select.is(':empty')) {
        $select.remove();
        $(this).remove();
    }
    //To Remove Entire Column Now. <<<<<<<<<<<<<
    var $table = $('table').on("click", "th", "td", function() {
        var $this = $(this);
        var index = $this.index();
        if ($this[0].tagName === "TD") {
            $table.find("th").eq(index).remove();
        } else {
            $this.remove();
        }
        $table.find("tr").each(function () {
            $(this).find("td").eq(index).remove();
        });
    });
    $table.find("th:contains('" + selected + "')").click();


}

function rearrange(){

}