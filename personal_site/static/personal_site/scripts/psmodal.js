/**
 * Created by foxtrot on 14/05/16.
 */

// Function that handles populating the modular modal to display more info on a display item.
// Takes an event that should have the following fields as data (shown as [field name] -> [type of value when accessed])
// type -> string (e.g. "projects", "games", "hobbies")
// pk -> int
modal_popup = function (event) {
    var popupModal = window.POPUP_MODAL;
    var popupData = window.DATAMAP[event.data.category][event.data.pk];

    //Populate all the fields
    $("#modal_title",popupModal).html(popupData.title);
    $("#modal_tech",popupModal).html("Technologies: "+"<b>"+popupData.highlights+"</b>");

    //Dates are special
    var startDate = Date.parse(popupData.start_date).toString("MMM yyyy");
    var endDate = Date.parse(popupData.end_date).toString("MMM yyyy");
    if(popupData.ongoing){
        $("#modal_date",popupModal).html("(Started "+startDate+" - Ongoing)");
    }
    else{
        if(startDate==endDate){
            $("#modal_date",popupModal).html("("+startDate+")");
        }
        else{
            $("#modal_date",popupModal).html("("+startDate+" - "+endDate+")");
        }
    }

    $("#modal_description",popupModal).html(popupData.description);

    //carousel is also special
    var imgCount = popupData.display_pictures.length;
    //The one start image is the thumbnail, which is automatically enlarged
    $("#modal_img_indicators",popupModal).html("<li data-target=\"#myCarousel\" data-slide-to=\"0\" class=\"active\"></li>");
    $("#modal_img_slides",popupModal).html("<div class='item active text-center'><img src=\""+window.MEDIA_URL+popupData.thumbnail+"\" alt='testy' style='height: 256px;width: auto;' class='img-rounded img-responsive'></div>");

    //Trigger another AJAX to load the rest of the images
    var ajaxImgRequest = ajaxImageHandler(event.data.category,event.data.pk,function(data){console.log(data)});
    if(ajaxImgRequest){
        ajaxImgRequest.success(function(data){
            console.log(data);
            result = JSON.parse(data);
            for(var i=0; i<result.length; ++i){
                $("#modal_img_slides",popupModal).append("<div class='item text-center img-rounded img-responsive'><img src=\""+result[i]+"\" alt='testy' style='height: 256px;width: auto;' class='img-rounded img-responsive'></div>");
                $("#modal_img_indicators",popupModal).append("<li data-target='#myCarousel' data-slide-to='"+(i+1)+"' class=''></li>");
            }
            //We know the data is actually a list of strings
        }); // end Success function
        popupModal.off('hide.bs.modal');
        popupModal.on('hidden.bs.modal',function () {
            ajaxImgRequest.abort();
        })
    }

    //Show the Modal
    popupModal.modal('show');

    return false; //We don't want the page to refresh... at all.
};