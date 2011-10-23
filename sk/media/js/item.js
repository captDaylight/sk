$(document).ready(function() {		
	$("button").click(function(){
		if($(this).attr('class') == 'followbutton'){
			return add_follower();
		}else if($(this).attr('class') == 'unfollowbutton'){
			return delete_follower();
		}else if($(this).attr('class') == 'votebutton'){
			return add_vote();
		}	
	});
	
	
/*
	$('form').submit(function(){
		$.ajax({
		url:"/unfollow/"+itemUserId+"/",
		type:"GET",		
		success: function(data){
			try{
				return false;			
			}
			catch(e){
				console.log("not cool");
			}
		}
		event.preventDefault();
	});
*/
});