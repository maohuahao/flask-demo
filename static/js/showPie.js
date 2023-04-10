function getPieOption(datas, legend_titles, title) {
    console.log(title)
    console.log(datas)
    console.log(legend_titles)
    let option = {
        title: [{
            text: title,
            left: 'center',
            textStyle: {
                color: '#fff',
                fontSize: '16'
            },
        }
        ],
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b}: {c} ({d}%)",
            position: function (p) {   //其中p为当前鼠标的位置
                return [p[0] + 10, p[1] - 10];
            }
        },
        legend: {
            top: '70%',
            itemWidth: 10,
            itemHeight: 10,
            data: legend_titles,
            textStyle: {
                color: 'rgba(255,255,255,.5)',
                fontSize: '12',
            }
        },
        series: [
            {
                name: '年龄分布',
                type: 'pie',
                center: ['50%', '42%'],
                radius: ['40%', '60%'],
                color: ['#065aab', '#066eab', '#0682ab', '#0696ab', '#06a0ab', '#06b4ab', '#06c8ab', '#06dcab', '#06f0ab'],
                label: {show: false},
                labelLine: {show: false},
                data: datas,
            }
        ]
    };

    return option;
}