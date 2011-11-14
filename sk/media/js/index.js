$(document).ready(function() {		
	var filterClicked = 0; // starts at zero, but filter one is 1, filter two is 2 ...
	var currentFilter = 0; // keep track of which filter is open.  0 == none selected
	var filters = ['countries', 'categories', 'people'];
	var subfilters = ['countriesfilter','categoriesfilter','peoplefilter']
	
	$('li').click(function(){
		if($(this).attr('id') == filters[0]){
			filterClicked = 1;
			openCloseFilter();
		}else if($(this).attr('id') == filters[1]){
			filterClicked = 2;
			openCloseFilter();
		}else if($(this).attr('id') == filters[2]){
			filterClicked = 3;
			openCloseFilter();
		}
	});
	
	function openCloseFilter(){
		if(filterClicked == currentFilter){
			$('#'+subfilters[filterClicked-1]).hide(100);
			currentFilter = 0;
		}else{
			if(currentFilter > 0){
				$('#'+subfilters[currentFilter-1]).hide();
				$('#'+subfilters[filterClicked-1]).show();
				currentFilter = filterClicked;
			}
			else{
				$('#'+subfilters[filterClicked-1]).show(100);
				currentFilter = filterClicked;
			}
		}
	}
	
	
	$('.item').mouseenter(function(){
		$(this).children('.prod_img').css('opacity', '0.75')
	}).mouseleave(function(){
		$(this).children('.prod_img').css('opacity', '1.0')
	})
});