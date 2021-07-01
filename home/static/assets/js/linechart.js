new Chart(document.getElementById("linechart"), {
	type: 'line',
	data: {
		labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
		datasets: [{
			label: '2020',
			backgroundColor: window.chartColors.navy,
			borderColor: window.chartColors.navy,
			data: [30,10,70,15,60,20,70,80],
			fill: false,
		}, {
			label: '2021',
			fill: false,
			backgroundColor: window.chartColors.purple,
			borderColor: window.chartColors.purple,
			data: [10,40,20,35,25,50,10,70],
		}]
	},
	options: {
		responsive: true,
		// title: {
		// 	display: true,
		// 	text: 'Chart.js Line Chart'
		// },
		tooltips: {
			mode: 'index',
			intersect: false,
		},
		hover: {
			mode: 'nearest',
			intersect: true
		},
		scales: {
			xAxes: [{
				display: true,
				scaleLabel: {
					display: true,
					labelString: 'Month'
				}
			}],
			yAxes: [{
				display: true,
				scaleLabel: {
					display: true,
					labelString: 'Value'
				}
			}]
		}
	}
});
