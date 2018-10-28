/**
 * Created by foxtrot on 14/05/16.
 */

 // Fills in the link information
 function PopulateLinks(modal, data){
    var linksHtml = ""
    if(data.sourcecode_url){
        var sourceLinkText = "Source Code"
        if(data.sourcecode_url.includes("github")){
            sourceLinkText = "Github Repo"
        }
        linksHtml += "<a href="+data.sourcecode_url+" style='color: #FFFFFF' target='_blank'>"+sourceLinkText+"</a>"
    }

    if(data.live_url){
        if(linksHtml.length > 1){
            linksHtml += ", "
        }
        linksHtml += "<a href="+data.live_url+" style='color: #FFFFFF' target='_blank'>Live Website</a>"
    }

    if(data.app_install_link){
        var installLinkText = "Download App"
        if(linksHtml.length > 1){
            linksHtml += ", "
        }
        if(data.app_install_link.includes("play.google.com")){
            installLinkText = "Download from Google Play"
        }
        linksHtml += "<a href="+data.app_install_link+" style='color: #FFFFFF' target='_blank'>"+installLinkText+"</a>"
    }

    if(linksHtml.length == 0){
        $("#modal_links",modal).hide();
    }
    else{
        $("#modal_links",modal).show();
        $("#modal_links",modal).html("Links: <b>"+linksHtml+"<b>");
    }
 }

 // Simplest text substitution ever
 function PopulateSimpleTextFields(modal, data){
    $("#modal_title",modal).html(data.title);
    $("#modal_tech",modal).html("Technologies: <b>"+data.highlights+"</b>");
    $("#modal_description",modal).html(data.description);
 }

 // De serialize and display the date
 function FormatDate(modal, data){
    //Dates are special
    var startDate = Date.parse(data.start_date).toString("MMM yyyy");
    var endDate = Date.parse(data.end_date).toString("MMM yyyy");

    if(data.ongoing){
        $("#modal_date",modal).html("Started "+startDate+" - Ongoing");
    }
    else{
        if(startDate==endDate){
            $("#modal_date",modal).html(startDate);
        }
        else{
            $("#modal_date",modal).html(startDate+" - "+endDate);
        }
    }
 }

 // Make all the necessary change to the carousel
 function UpdateCarousel(modal, data, category, pk){
    //The one start image is the thumbnail, which is automatically enlarged
    $("#modal_img_indicators",modal).html("<li data-target=\"#myCarousel\" data-slide-to=\"0\" class=\"active\"></li>");
    $("#modal_img_slides",modal).html("<div class='item active text-center'><img src=\""+window.MEDIA_URL+data.thumbnail+"\" alt='Project Main Image' style='height: 256px;width: auto; object-fit: contain' class='img-rounded img-responsive'></div>");

    //Trigger another AJAX to load the rest of the images
    var ajaxImgRequest = ajaxImageHandler(category, pk, function(call_data){console.log(call_data)});
    if(ajaxImgRequest){
        ajaxImgRequest.success(function(ajax_data){
            result = JSON.parse(ajax_data);

            // The result should be a list of image URLs
            // We can plug them in directly to the HTML
            for(var i=0; i<result.length; ++i){
                $("#modal_img_slides",modal).append("<div class='item text-center img-rounded img-responsive'><img src=\""+result[i]+"\" alt='ProjectImages' style='height: 256px;width: auto; object-fit: contain' class='img-rounded img-responsive'></div>");
                $("#modal_img_indicators",modal).append("<li data-target='#myCarousel' data-slide-to='"+(i+1)+"' class=''></li>");
            }

        }); // end Success function

        modal.off('hide.bs.modal');
        modal.on('hidden.bs.modal',function () {
            ajaxImgRequest.abort();
        })
    }
 }

// Function that handles populating the modular modal to display more info on a display item.
// Takes an event that should have the following fields as data (shown as [field name] -> [type of value when accessed])
// type -> string (e.g. "projects", "games", "hobbies")
// pk -> int
modal_popup = function (event) {
    var popupModal = window.POPUP_MODAL;
    var data = window.DATAMAP[event.data.category][event.data.pk];

    PopulateSimpleTextFields(popupModal, data);
    PopulateLinks(popupModal, data);
    FormatDate(popupModal, data);
    UpdateCarousel(popupModal, data, event.data.category, event.data.pk);

    //Show the Modal
    popupModal.modal('show');

    return false; //We don't want the page to refresh... at all.
};