$(document).ready(function() {		
	var filterClicked = 0; // starts at zero, but filter one is 1, filter two is 2 ...
	var currentFilter = 0; // keep track of which filter is open.  0 == none selected
	var filters = ['countries', 'categories', 'people'];

	$('a').click(function(){
		if($(this).attr('id') == filters[0]){
			if(currentFilter == 1){
				closeSubFilter();
			}else{
				
			}
			openClose();
		}else if($(this).attr('id') == filters[1]){
			openClose()
		}else if($(this).attr('id') == filters[2]){
			openClose();
		}
	});
	
	function openSubFilter(){
	
	}
	function closeSubFilter(){
	
	}
});