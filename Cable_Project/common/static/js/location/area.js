(function(global){
    function showLocation(province , city , town) {

        var location = new global.Location(),
            title = ['省份' , '地级市' , '市、县、区'],
            $loc_province = $('#loc_province'),
            $loc_city = $('#loc_city'),
            $loc_town = $('#loc_town');
//            $locationId = $('input[name="location_id"]');

        $.each(title , function(k , v) {
            title[k] = '<option value="">'+v+'</option>';
        });

        $loc_province.append(title[0]);
        $loc_city.append(title[1]);
        $loc_town.append(title[2]);

        $loc_province.change(function() {
            $loc_city.empty();
            $loc_city.append(title[1]);
            location.fillOption('loc_city' , '0,' + $loc_province.val());
            $loc_town.empty();
            $loc_town.append(title[2]);
//            $locationId.val($(this).val());
        });

        $loc_city.change(function() {
            $loc_town.empty();
            $loc_town.append(title[2]);
            location.fillOption('loc_town', '0,' + $loc_province.val() + ',' + $loc_city.val());
//            $locationId.val($(this).val());
        });

//        $loc_town.change(function() {
//            $locationId.val($(this).val());
//        });

        if (province) {
            location.fillOption('loc_province' , '0' , province);
            if (city) {
                location.fillOption('loc_city' , '0,' + province , city);
                if (town) {
                    location.fillOption('loc_town' , '0,' + province + ',' + city, town);
                }
            }
        } else {
            location.fillOption('loc_province' , '0');
        }
    }

    $(document).ready(function() {
        showLocation();
    });
})(window);
