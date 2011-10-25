$(document).ready(function(){
	var geocoder;
	var map;
	
	geocoder = new google.maps.Geocoder();

	createMap();
	codeAddress();

	function createMap(){
	    var latlng = new google.maps.LatLng(-34.397, 150.644);
	    var myOptions = {
	      zoom: 3,
	      scrollwheel: false,
	      panControl: false,
		  zoomControl: false,
		  scaleControl: false,
		  streetViewControl: false,
		  mapTypeControl: false,
	      mapTypeId: google.maps.MapTypeId.TERRAIN,
	    }
	    console.log("Making a map");
	    map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);	
	}

	function codeAddress() {
		
		geocoder.geocode( {'address': address}, function(results, status) {
		  if (status == google.maps.GeocoderStatus.OK) {
		    map.setCenter(results[0].geometry.location);
		    var marker = new google.maps.Marker({
		        map: map, 
		        position: results[0].geometry.location
		    });
		  } else {
		    console.log("Geocode was not successful for the following reason: " + status);
		  }
		});
	}
});
