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
    let jsonData = JSON.parse(data)
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


let seriousOption = getBarOption(seriousJsonData, '严重违法次数排名TOP5');
let abnormalOption = getBarOption(abnormalJsonData, '经营异常工商公示次数排名TOP5');
let executedpersonOption = getBarOption(executedpersonJsonData, '企业被执行次数TOP5');
let executionsOption = getBarOption(executionsJsonData, '企业失信次数TOP5');

seriousChart.setOption(seriousOption);
abnormalChart.setOption(abnormalOption);
executedpersonsChart.setOption(executedpersonOption);
executionsChart.setOption(executionsOption);

// window.addEventListener('resize', function () {
//     seriousChart.resize();
// });