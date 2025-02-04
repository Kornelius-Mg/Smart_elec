/*Dashboard Init*/
 
"use strict"; 

/*****Ready function start*****/
$(document).ready(function(){
	$('#statement').DataTable({
		"bFilter": false,
		"bLengthChange": false,
		"bPaginate": false,
		"bInfo": false,
	});
	if( $('#chart_2').length > 0 ){
		var ctx2 = document.getElementById("chart_2").getContext("2d");
		var data2 = {
			labels: ["January", "February", "March", "April", "May", "June", "July"],
			datasets: [
				{
					label: "My First dataset",
					backgroundColor: "rgba(240,197,65,.6)",
					borderColor: "rgba(240,197,65,.6)",
					data: [10, 30, 80, 61, 26, 75, 40]
				},
				{
					label: "My Second dataset",
					backgroundColor: "rgba(46,205,153,.6)",
					borderColor: "rgba(46,205,153,.6)",
					data: [28, 48, 40, 19, 86, 27, 90]
				},
				{
					label: "My Third dataset",
					backgroundColor: "rgba(78,157,230,.6)",
					borderColor: "rgba(78,157,230,.6)",
					data: [8, 28, 50, 29, 76, 77, 40]
				}
			]
		};
		
		var hBar = new Chart(ctx2, {
			type:"bar",
			data:data2,
			
			options: {
				tooltips: {
					mode:"label"
				},
				scales: {
					yAxes: [{
						stacked: true,
						gridLines: {
							color: "rgba(135,135,135,0)",
						},
						ticks: {
							fontFamily: "Poppins",
							fontColor:"#878787"
						}
					}],
					xAxes: [{
						stacked: true,
						gridLines: {
							color: "rgba(135,135,135,0)",
						},
						ticks: {
							fontFamily: "Poppins",
							fontColor:"#878787"
						}
					}],
					
				},
				elements:{
					point: {
						hitRadius:40
					}
				},
				animation: {
					duration:	3000
				},
				responsive: true,
				maintainAspectRatio:false,
				legend: {
					display: false,
				},
				
				tooltip: {
					backgroundColor:'rgba(33,33,33,1)',
					cornerRadius:0,
					footerFontFamily:"'Poppins'"
				}
				
			}
		});
	}
	if( $('#chart_6').length > 0 ){
		var ctx6 = document.getElementById("chart_6").getContext("2d");
		var data6 = {
			 labels: [
			"organic",
			"Referral",
			"Other"
		],
		datasets: [
			{
				data: [200,550,250],
				backgroundColor: [
					"rgba(240,197,65,.6)",
					"rgba(46,205,153,.6)",
					"rgba(78,157,230,.6)",
				],
				hoverBackgroundColor: [
					"rgba(240,197,65,.6)",
					"rgba(46,205,153,.6)",
					"rgba(78,157,230,.6)",
				]
			}]
		};
		
		var doughnutChart  = new Chart(ctx6,{
			type: 'doughnut',
			data: data6,
			options: {
				animation: {
					duration:	3000
				},
				responsive: true,
				maintainAspectRatio:false,
				legend: {
					display:false
				},
				tooltip: {
					backgroundColor:'rgba(33,33,33,1)',
					cornerRadius:0,
					footerFontFamily:"'Poppins'"
				},
				elements: {
					arc: {
						borderWidth: 0
					}
				}
			}
		});
	}
	if($('#area_chart').length > 0) {
		var data=[{
            temps: 'Sunday',
            phase1: 102,
            phase2: 80,
            phase3: 20
        }, {
            temps: 'Mon',
            phase1: 130,
            phase2: 100,
            phase3: 80
        }, {
            temps: 'Tue',
            phase1: 80,
            phase2: 30,
            phase3: 70
        }, {
            temps: 'Wednesday',
            phase1: 70,
            phase2: 200,
            phase3: 140
        }, {
            temps: 'Thu',
            phase1: 180,
            phase2: 50,
            phase3: 140
        }, {
            temps: 'Fri',
            phase1: 105,
            phase2: 170,
            phase3: 80
        },
         {
            temps: 'Sat',
            phase1: 250,
            phase2: 150,
            phase3: 200
        }];
		var dataNew = [{
            temps: 'Jan',
            phase1: 10,
            phase2: 60,
            phase3: 20
        }, 
		{
            temps: 'Feb',
            phase1: 110,
            phase2: 100,
            phase3: 80
        },
		{
            temps: 'March',
            phase1: 120,
            phase2: 100,
            phase3: 80
        },
		{
            temps: 'April',
            phase1: 110,
            phase2: 100,
            phase3: 80
        },
		{
            temps: 'May',
            phase1: 170,
            phase2: 100,
            phase3: 80
        },
		{
            temps: 'June',
            phase1: 120,
            phase2: 150,
            phase3: 80
        },
		{
            temps: 'July',
            phase1: 120,
            phase2: 150,
            phase3: 80
        },
		{
            temps: 'Aug',
            phase1: 190,
            phase2: 120,
            phase3: 80
        },
		{
            temps: 'Septembre',
            phase1: 110,
            phase2: 120,
            phase3: 80
        },
		{
            temps: 'Oct',
            iphone: 10,
            ipad: 170,
            itouch: 10
        },
		{
            temps: 'Nov',
            phase1: 10,
        	phase2: 470,
            phase3: 10
        },
		{
            temps: 'Dec',
            phase1: 30,
            phase2: 170,
            phase3: 10
        }
		];
		
		var lineChart = Morris.Area({
        element: 'area_chart',
        data: data ,
        xkey: 'temps',
        ykeys: ['phase1', 'phase2', 'phase3'],
        labels: ['phase1', 'phase2', 'phase3'],
        pointSize: 0,
        lineWidth:0,
		fillOpacity: 0.6,
		pointStrokeColors:['#ff0000', '#00ff00', '#0000ff'],
		behaveLikeLine: true,
		grid: false,
		hideHover: 'auto',
		lineColors: ['#ff0000', '#00ff00', '#0000ff'],
		resize: true,
		redraw: true,
		smooth: true,
		gridTextColor:'#878787',
		gridTextFamily:"Poppins",
        parseTime: false
    });
	}
	
	/* Switchery Init*/
	var elems = Array.prototype.slice.call(document.querySelectorAll('.js-switch'));
	$('.js-switch').each(function() {
		new Switchery($(this)[0], $(this).data());
	});
	var swichMorris = function() {
		if($("#morris_switch").is(":checked")) {
			lineChart.setData(data);
			lineChart.redraw();
		} else {
			lineChart.setData(dataNew);
			lineChart.redraw();
		}
	}
	swichMorris();	
	btnSwitch.on(
		{
			click: (event) => {
				event.preventDefault();
	
				if(btnSwitch.is(":checked")) {
					startEngin();
				}
				else {
					stopEngin();
				}
			},
			change: () => {
				setPowerState();
				swichMorris();
			}
		}
	);
	
});
/*****Ready function end*****/

/*****Load function start*****/
// $(window).load(function(){
// 	window.setTimeout(function(){
// 		$.toast({
// 			heading: 'Bienvenu(e) à SmartEelec',
// 			text: "Pour l'administration des installations electriques",
// 			position: 'top-right',
// 			loaderBg:'#f0c541',
// 			icon: 'success',
// 			hideAfter: 3500, 
// 			stack: 6
// 		});
// 	}, 3000);
// });
// /*****Load function* end*****/

var sparklineLogin = function() { 
	if( $('#sparkline_1').length > 0 ){
		$("#sparkline_1").sparkline([2,4,4,6,8,5,6,4,8,6,6,2 ], {
			type: 'line',
			width: '100%',
			height: '35',
			lineColor: '#2ecd99',
			fillColor: 'rgba(46,205,153,.6)',
			minSpotColor: '#2ecd99',
			maxSpotColor: '#2ecd99',
			spotColor: '#2ecd99',
			highlightLineColor: 'rgba(0, 0, 0, 0.6)',
			highlightSpotColor: '#2ecd99'
		});
	}	
	if( $('#sparkline_2').length > 0 ){
		$("#sparkline_2").sparkline([0,2,8,6,8], {
			type: 'line',
			width: '100%',
			height: '35',
			lineColor: '#2ecd99',
			fillColor: 'rgba(46,205,153,.6)',
			minSpotColor: '#2ecd99',
			maxSpotColor: '#2ecd99',
			spotColor: '#2ecd99',
			highlightLineColor: 'rgba(0, 0, 0, 0.6)',
			highlightSpotColor: '#2ecd99'
		});
	}	
	if( $('#sparkline_3').length > 0 ){
		$("#sparkline_3").sparkline([0, 23, 43, 35, 44, 45, 56, 37, 40, 45, 56, 7, 10], {
			type: 'line',
			width: '100%',
			height: '35',
			lineColor: '#2ecd99',
			fillColor: 'rgba(46,205,153,.6)',
			minSpotColor: '#2ecd99',
			maxSpotColor: '#2ecd99',
			spotColor: '#2ecd99',
			highlightLineColor: 'rgba(0, 0, 0, 0.6)',
			highlightSpotColor: '#2ecd99'
		});
	}
	if( $('#sparkline_4').length > 0 ){
		$("#sparkline_4").sparkline([0,2,8,6,8,5,6,4,8,6,6,2 ], {
			type: 'bar',
			width: '100%',
			height: '50',
			barWidth: '5',
			barSpacing: '5',
			barColor: '#2ecd99',
			highlightSpotColor: '#2ecd99'
		});
	}	
}
var sparkResize;
	$(window).resize(function(e) {
		clearTimeout(sparkResize);
		sparkResize = setTimeout(sparklineLogin, 200);
	});
sparklineLogin();