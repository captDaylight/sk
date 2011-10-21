function add_vote(){
	console.log("add follower");
  	$.ajax({
		url: "/vote/"+itemUserId+"/"+voter+"/",
		type:"GET",
		success: function(data){
			try{
				jsonOBJ = $.parseJSON(data);
				console.log(jsonOBJ);
			}
			catch(e){
				jsonOBJ = {};
			}
		}
	});
	
	return false;
};