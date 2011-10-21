$(document).ready(function() {	
	if(isFollowing == 1){
		show follow
	}else if(isFollowing == 2){
		show unfollow
	}else if(){
		show signin 
	}
	
		
	$("#user").click(function(){
		openClose();
	});

	$("button").click(function(){
		if($(this).attr('id') == 'followbutton'){
			return add_follower();
		}else if($(this).attr('id') == 'unfollowbutton'){
			return delete_follower();
		}else if($(this).attr('id') == 'votebutton'){
			return add_vote();
		}	
	});

});