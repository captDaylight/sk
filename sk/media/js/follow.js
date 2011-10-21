var button = new Array("#followbutton","#unfollowbutton","#loginbutton");
var jsonOBJ;

function openClose(){
	if(userInfoOpen == false){
		$(button[isFollowing-1]).show(200);
	}else if(userInfoOpen == true){
		$(button[isFollowing-1]).hide(200);
	}
}

function delete_follower(){
	$.ajax({
		url:"/unfollow/"+itemUserId+"/",
		type:"GET",
		success: function(data){
			try{
				jsonOBJ = $.parseJSON(data);
			}
			catch(e){
				jsonOBJ = {};
			}
		}
	});
	console.log(jsonOBJ);
/*
	there is some shit that needs to be cleaned up here
	in particular not to change isFollowing until I parse out success correctly
*/
/*
	if(jsonOBJ.success == "success"){
		console.log("yup it work");
	}
*/
	openClose();
	isFollowing = 1;
	openClose();
	return false;
}

function add_follower() {
  	$.ajax({
		url: "/follow/"+itemUserId+"/",
		type:"GET",
		success: function(data){
			try{
				jsonOBJ = $.parseJSON(data);
			}
			catch(e){
				jsonOBJ = {};
			}
		}
	});
	openClose();
	isFollowing = 2;
	openClose();
	return false;
};