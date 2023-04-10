function getPie2Option() {
    var dataStyle = {
        normal: {
            label: {
                show: false
            },
            labelLine: {
                show: false
            },
            // shadowBlur: 40,
            // shadowColor: 'rgba(40, 40, 40, 1)',
        }
    };
    var placeHolderStyle = {
        normal: {
            color: 'rgba(255,255,255,.05)',
            label: {show: false,},
            labelLine: {show: false}
        },
        emphasis: {
            color: 'rgba(0,0,0,0)'
        }
    };
    option = {
        title: [{
            text: "一线城市情况",
            left: 'center',
            textStyle: {
                color: '#fff',
                fontSize: '16'
            },
        }
        ],
        color: ['#0f63d6', '#0f78d6', '#0f8cd6', '#0fa0d6', '#0fb4d6'],
        tooltip: {
            show: true,
            formatter: "{a} : {c} "
        },
        legend: {
            itemWidth: 10,
            itemHeight: 10,
            itemGap: 12,
            bottom: '10%',
            data: ['浙江', '上海', '广东', '北京', '深圳'],
            textStyle: {
                color: 'rgba(255,255,255,.6)',
            }
        },
        series: [
            {
                name: '浙江',
                type: 'pie',
                clockWise: false,
                center: ['50%', '42%'],
                radius: ['59%', '70%'],
                itemStyle: dataStyle,
                hoverAnimation: false,
                data: [{
                    value: 80,
                    name: '01'
                }, {
                    value: 20,
                    name: 'invisible',
                    tooltip: {show: false},
                    itemStyle: placeHolderStyle
                }]
            },

            {
                name: '上海',
                type: 'pie',
                clockWise: false,
                center: ['50%', '42%'],
                radius: ['49%', '60%'],
                itemStyle: dataStyle,
                hoverAnimation: false,
                data: [{
                    value: 70,
                    name: '02'
                }, {
                    value: 30,
                    name: 'invisible',
                    tooltip: {show: false},
                    itemStyle: placeHolderStyle
                }]
            },

            {
                name: '广东',
                type: 'pie',
                clockWise: false,
                center: ['50%', '42%'],
                radius: ['39%', '50%'],
                itemStyle: dataStyle,
                hoverAnimation: false,
                data: [{
                    value: 65,
                    name: '03'
                }, {
                    value: 35,
                    name: 'invisible',
                    tooltip: {show: false},
                    itemStyle: placeHolderStyle
                }]
            },

            {
                name: '北京',
                type: 'pie',
                clockWise: false,
                center: ['50%', '42%'],
                radius: ['29%', '40%'],
                itemStyle: dataStyle,
                hoverAnimation: false,
                data: [{
                    value: 60,
                    name: '04'
                }, {
                    value: 40,
                    name: 'invisible',
                    tooltip: {show: false},
                    itemStyle: placeHolderStyle
                }]
            },

            {
                name: '深圳',
                type: 'pie',
                clockWise: false,
                center: ['50%', '42%'],
                radius: ['20%', '30%'],
                itemStyle: dataStyle,
                hoverAnimation: false,
                data: [{
                    value: 50,
                    name: '05'
                }, {
                    value: 50,
                    name: 'invisible',
                    tooltip: {show: false},
                    itemStyle: placeHolderStyle
                }]
            },

        ]
    };
    return option;
}