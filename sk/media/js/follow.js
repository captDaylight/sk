function delete_follower(){
	$.ajax({
		url:"/unfollow/"+itemUserId+"/",
		type:"GET",		
		success: function(data){
			try{
				var jsonOBJ = $.parseJSON(data);
				$('.unfollowbutton').removeClass('unfollowbutton').addClass('followbutton');			
				$('.followbutton').text('Follow');
			}
			catch(e){
				console.log("not cool");
			}
		}
	});
	return false;
}

function add_follower() {
  	$.ajax({
		url: "/follow/"+itemUserId+"/",
		type:"GET",
		success: function(data){
			try{
				var jsonOBJ = $.parseJSON(data);
				$('.followbutton').removeClass('followbutton').addClass('unfollowbutton');			
				$('.unfollowbutton').text('Unfollow');
			}
			catch(e){
				jsonOBJ = {};
			}
		}
	});
	return false;
};