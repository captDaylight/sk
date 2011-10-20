function add_vote(){
	console.log("add follower");
  	$.ajax({
		url: "/vote/"+itemUserId+"/"+voter+"/",
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