
var InitStats = function(data){
	var options = {
		xaxis: {
			ticks: [[1, 'Mon'], [2, 'Tues'], [3, 'Wed'], [4, 'Thurs'], [5, 'Fri'], [6, 'Sat'], [7, 'Sun']]
		},
		series: {
			lines: { show: true },
			points: { show: true }
		},
		grid: { hoverable: true }
	};
	
	$('#dailyActivity').plot([data], options);

	var previousPoint = null;

	$("#dailyActivity").bind("plothover", function (event, pos, item) {
		if (item) {
			if (previousPoint != item.dataIndex) {
				previousPoint = item.dataIndex;

				$("#tooltip").remove();
				var x = item.datapoint[0].toFixed(0),
				y = item.datapoint[1].toFixed(0);

				showTooltip(item.pageX, item.pageY, 'Avg: ' + y.toString() + ' messages');
			}
		}
		else {
			$("#tooltip").remove();
			previousPoint = null;            
		}
	});

	function showTooltip(x, y, contents) {
		$('<div id="tooltip">' + contents + '</div>').css({
			position: 'absolute',
			display: 'none',
			top: y + 5,
			left: x + 5,
			border: '1px solid #fdd',
			padding: '2px',
			'background-color': '#fee',
			opacity: 0.80
		}).appendTo('body').fadeIn(200);
	}
}
			