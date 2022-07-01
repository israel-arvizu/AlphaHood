let graphData = [{
        x: 5,
        y: 5
    },
    {
        x: 7,
        y: 10
    },
    {
        x: 10,
        y: 12
    },
    {
        x: 15,
        y: 7
    },
    {
        x: 20,
        y: 30
    },
    {
        x: 25,
        y: 80
    }
    ]

const dayData =  {

    labels:["test", "test2", "test3", "test4", "test5", "test6"],

    datasets:[{
        label:"price",
    data: graphData,
    fill: false,
    backgroundColor:"black",
    borderColor:"#5AC53B",
    borderWidth: 2,
    pointBorderColor:'rgba(0,0,0,0)',
    pointBackgroundColor:'rbga(0,0,0,0)',
    pointHoverBackgroundColor:'#5AC53B',
    pointHoverBorderColor:"#000000",
    pointHoverBorderWidth: 4,
    pointHoverRadius: 6,
}]
}


export {graphData, dayData};
