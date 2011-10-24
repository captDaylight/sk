function add_vote(){
	console.log("/vote/"+itemUserId+"/"+voter+"/");
  	$.ajax({
		url: "/vote/"+itemUserId+"/"+voter+"/",
		type:"GET",
		success: function(data){
			try{
				jsonOBJ = $.parseJSON(data);
				$('#votearea').text(jsonOBJ.count);
				$('#votearea').append('<div>You have Voted.</div>');

			}
			catch(e){
				jsonOBJ = {};
			}
		}
	});
	
	return false;
};