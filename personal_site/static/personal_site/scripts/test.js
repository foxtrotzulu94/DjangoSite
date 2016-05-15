/**
 * Created by foxtrot on 14/05/16.
 */

//Events passed into modals expect some standard information to be passed to it. Specifically
// "title" string, "description" string, "displays" list of urls to pictures. (More to come soon)

testy_modal = function (event) {
    var popupModal = window.POPUP_MODAL;

    popupModal.modal('show');
    $("#modal_title",popupModal).html(event.data.title);
    $("#modal_tech",popupModal).append("<b>"+event.data.title+"</b>");
    console.log( event.data.title ,event.data.subtitle );
};

$( document ).ready(function() {
    console.log( "ready!" );
    //Load all projects from Database
    var displayItem = $('#display_item'); //The item to be constantly cloned
    var divToAppendTo = $('#project_div');

    window.POPUP_MODAL = $("#test_popup");

    $.ajax({ //Ask if we can save this schedule
        type: 'get',
        url: "/example/projects",
        success: function (data) {
            $('#loading').hide();
            var result = JSON.parse(data);

            console.log(result.length);
            console.log(result);
            for(var i=0; i< result.length; ++i){
                var modelFields = result[i]["fields"];

                var newDisplayItem = displayItem.clone(true);
                newDisplayItem.selector = displayItem.selector+i;
                var testy = $('#item_thumbnail',newDisplayItem);
                testy.attr("src",window.MEDIA_URL +modelFields["img"]);
                var title = $('#display_title',newDisplayItem);
                title.html(modelFields["title"]);
                var s = $('#display_subtitle',newDisplayItem);
                s.html("saaf");
                newDisplayItem.show();
                newDisplayItem.click({title: modelFields["title"], subtitle: modelFields["summary"]},testy_modal);

                divToAppendTo.append(newDisplayItem);

            }

        },
        error: function(xhr, ajaxOptions, thrownError) {
            alert(thrownError);
            console.log("ERROR!");
        }
    });

    console.log( "done!!!" );
});