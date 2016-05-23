/**
 * Created by foxtrot on 23/05/16.
 */

ajaxImageHandler = function (category,pk,successFunction) {
    if(category.length===0||pk==""){
        return null;
    }
    return $.ajax({
        type: 'get',
        url: "/data/"+category+"/"+pk+"/images",

        // success: successFunction(data),

        error: function(xhr, ajaxOptions, thrownError) {
            alert(thrownError);
            console.log("ERROR!");
        }
    });
};

ajaxDataHandler = function (modelIdentifier) {
    //Avoid passing empty strings which will prompt a 400 error
    if(modelIdentifier.length === 0 || modelIdentifier==""){
        return;
    }

    $.ajax({
        type: 'get',
        url: "/data/"+modelIdentifier,
        
        success: function (data) {
            var result = JSON.parse(data);
            var ajaxKey = modelIdentifier;

            // console.log(data);

            //Initiate and Access the DATAMAP
            window.DATAMAP[ajaxKey] = {};
            for(var i=0; i<result.length; ++i){
                //The datamap only holds the fields of the model
                window.DATAMAP[ajaxKey][result[i]['pk']] = result[i]['fields'];
            }
        },

        error: function(xhr, ajaxOptions, thrownError) {
            alert(thrownError);
            console.log("ERROR!");
        }
    });
};