$(document).ready(function() {		
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