Highcharts.chart('leave-container', {
  chart: {
    type: 'line'
  },
  title: {
    text: 'Monthly Leaves Taken'
  },
  subtitle: {
    text: 'Source: Gareeb'
  },
  xAxis: {
    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  },
  yAxis: {
    title: {
      text: 'Days'
    }
  },
  plotOptions: {
    line: {
      dataLabels: {
        enabled: true
      },
      enableMouseTracking: false
    }
  },
  credits: {
            enabled: false
        },
        exporting: {
            enabled: false
      },
  series: [{
    name: 'Leaves',
    data: [7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
  }]
});