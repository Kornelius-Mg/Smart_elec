 /*****Temporary Alerts function start*****/

var tempSuccessAlert = (message) => {
    window.setTimeout(function(){
		$.toast({
			heading: 'Success',
			text: message,
			position: 'top-right',
			loaderBg:'#f0c541',
			icon: 'success',
			hideAfter: 4000, 
			stack: 6
		});
	}, 3000);
};

var tempWarningAlert = (message) => {
    window.setTimeout(function(){
		$.toast({
			heading: 'Alerte',
			text: message,
			position: 'top-right',
			loaderBg:'#f0c541',
			icon: 'warning',
			hideAfter: 4000, 
			stack: 6
		});
	}, 3000); 
};

var tempErrorAlert = (message) => {
    window.setTimeout(function(){
		$.toast({
			heading: 'Erreur',
			text: message,
			position: 'top-right',
			loaderBg:'#f0c541',
			icon: 'error',
			hideAfter: 4000, 
			stack: 6
		});
	}, 3000); 
}

// /*****Temporary alerts functions end*****/ */