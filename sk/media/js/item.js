$(document).ready(function() {		
	$("button").click(function(){
		if($(this).attr('class') == 'followbutton'){
			return add_follower();
		}else if($(this).attr('class') == 'unfollowbutton'){
			return delete_follower();
		}else if($(this).attr('class') == 'votebutton'){
			console.log("VOTED")
			return add_vote();
		}
	});
});