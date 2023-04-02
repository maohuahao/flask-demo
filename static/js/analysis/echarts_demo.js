let abnormal = document.getElementById('abnormal');
let serious_illegal = document.getElementById('serious_illegal');
let executedpersons = document.getElementById('executedpersons');
let executions = document.getElementById('executions');
let seriousChart = echarts.init(serious_illegal);
let abnormalChart = echarts.init(abnormal);
let executedpersonsChart = echarts.init(executedpersons);
let executionsChart = echarts.init(executions);

let seriousData = serious_illegal.getAttribute('data');
let abnormalData = abnormal.getAttribute('data');
let executedpersonsData = executedpersons.getAttribute('data');
let executionsData = executions.getAttribute('data');

function getShowData(data) {
    let datas = [];
    let x = [];
    let y = []
    jsonData = JSON.parse(data)
    jsonData.forEach((item => {
        x.push(item['name']);
        y.push(item['count']);
    }))
    datas.push(x)
    datas.push(y)
    return datas
}

let seriousJsonData = getShowData(seriousData);
let abnormalJsonData = getShowData(abnormalData);
let executedpersonJsonData = getShowData(executedpersonsData);
let executionsJsonData = getShowData(executionsData);

function getOption(datas, title) {
    option = {
        title: {
            text: title,
            textStyle: {
                color: '#A7A1AE'
            }
        },
        tooltip: {
            trigger: 'axis', //坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用
            axisPointer: {// 坐标轴指示器，坐标轴触发有效
                type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        xAxis: {
            type: 'category',
            data: datas[0],
            axisLabel: {
                color: '#A7A1AE',
                interval: 0,
                rotate: 15
            }
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name: 'count',
                type: 'bar',
                stack: 'Total',
                label: {
                    show: true,
                    position: 'inside'
                },
                data: datas[1],
            },
        ]
    };
    return option;
}

let seriousOption = getOption(seriousJsonData, '严重违法次数排名TOP5');
let abnormalOption = getOption(abnormalJsonData, '经营异常工商公示次数排名TOP5');
let executedpersonOption = getOption(executedpersonJsonData, '企业被执行次数TOP5');
let executionsOption = getOption(executionsJsonData, '企业失信次数TOP5');

seriousChart.setOption(seriousOption);
abnormalChart.setOption(abnormalOption);
executedpersonsChart.setOption(executedpersonOption);
executionsChart.setOption(executionsOption);