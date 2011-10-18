	$(document).ready(function() {	
		var userInfoOpen = false;
		var button = new Array("#followbutton","#unfollowbutton","#loginbutton");
		var jsonOBJ;
		
		$("#user").click(function(){
			openClose();
		});
		
		function openClose(){
			if(userInfoOpen == false){
				$(button[isFollowing-1]).show(200);
				userInfoOpen = true;
			}else if(userInfoOpen == true){
				$(button[isFollowing-1]).hide(200);
				userInfoOpen = false;
			}			
		}

		$("button").click(function(){
			if($(this).attr('id') == 'followbutton'){
				return add_follower();
			}else if($(this).attr('id') == 'unfollowbutton'){
				return delete_follower();
			}
		});

		function delete_follower(){
			console.log("delete follower");
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
			console.log("add follower");
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
			console.log(jsonOBJ);
			openClose();
			isFollowing = 2;
			openClose();
			return false;
		};
	});