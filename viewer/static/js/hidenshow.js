function HideNShow() {
        //Remove based on button click
    $(":button").on("click", function() {
    var $option = $select.find(":selected");
    var selected = $option.text();
    $option.remove();
    if ($select.is(':empty')) {
        $select.remove();
        $(this).remove();
    }
    $table.find("th:contains('" + selected + "')").click();
    });
}


