function getBarOption(datas, title, color = '#2f89cf') {
    // option = {
    //     title: {
    //         text: title,
    //         textStyle: {
    //             color: '#A7A1AE'
    //         }
    //     },
    //     tooltip: {
    //         trigger: 'axis', //坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用
    //         axisPointer: {// 坐标轴指示器，坐标轴触发有效
    //             type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
    //         }
    //     },
    //     xAxis: {
    //         type: 'category',
    //         data: datas[0],
    //         axisLabel: {
    //             color: '#A7A1AE',
    //             interval: 0,
    //             rotate: 15
    //         }
    //     },
    //     yAxis: {
    //         type: 'value'
    //     },
    //     series: [
    //         {
    //             name: 'count',
    //             type: 'bar',
    //             stack: 'Total',
    //             label: {
    //                 show: true,
    //                 position: 'inside'
    //             },
    //             data: datas[1],
    //         },
    //     ]
    // };
    let option = {
        title: {
            text: title,
            textStyle: {
                color: '#A7A1AE'
            },
            x: 'center',
            y: 'top',
        },
        //  backgroundColor: '#00265f',
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        grid: {
            left: '0%',
            top: '50px',
            right: '0%',
            bottom: '4%',
            containLabel: true
        },
        xAxis: [{
            type: 'category',
            data: datas[0],
            axisLine: {
                show: true,
                lineStyle: {
                    color: "rgba(255,255,255,.1)",
                    width: 1,
                    type: "solid",
                },
            },

            axisTick: {
                show: false,
            },
            axisLabel: {
                interval: 0,
                // rotate:50,
                show: true,
                splitNumber: 15,
                textStyle: {
                    color: "rgba(255,255,255,.6)",
                    fontSize: '12',
                },
            },
        }],
        yAxis: [{
            type: 'value',
            axisLabel: {
                //formatter: '{value} %'
                show: true,
                textStyle: {
                    color: "rgba(255,255,255,.6)",
                    fontSize: '12',
                },
            },
            axisTick: {
                show: false,
            },
            axisLine: {
                show: true,
                lineStyle: {
                    color: "rgba(255,255,255,.1	)",
                    width: 1,
                    type: "solid"
                },
            },
            splitLine: {
                lineStyle: {
                    color: "rgba(255,255,255,.1)",
                }
            }
        }],
        series: [
            {
                type: 'bar',
                data: datas[1],
                barWidth: '35%', //柱子宽度
                // barGap: 1, //柱子之间间距
                itemStyle: {
                    normal: {
                        color: color,
                        opacity: 1,
                        barBorderRadius: 5,
                    }
                }
            }

        ]
    };

    return option;
}