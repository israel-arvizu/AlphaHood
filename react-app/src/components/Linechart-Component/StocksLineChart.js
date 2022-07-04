import React, { useEffect, useState } from 'react'
import { Line } from "react-chartjs-2"
import Chart from 'chart.js/auto';
import { useDispatch, useSelector } from 'react-redux';
import { valuesToArray, keysToArray, soloKeyToArray } from './LinechartData'

function StockLineChart({ stockHistory }) {
    console.log(stockHistory)
    const [update, setUpdate] = useState(false);
    const [portData, setPortData] = useState(valuesToArray(stockHistory))
    const [portLabels, setPortLabels] = useState(soloKeyToArray(stockHistory))

    if (!update) {
        setPortData(valuesToArray(stockHistory))
        setPortLabels(soloKeyToArray(stockHistory))
        setUpdate(true)
    }

    return (
        <div className='linegraph'>
            <Line
                data={{
                    labels: portLabels,
                    datasets: [{
                        data: portData,
                        fill: false,
                        backgroundColor: "black",
                        borderColor: "rgb(3, 200, 5)",
                        borderWidth: 2,
                        pointBorderColor: 'rgba(0,0,0,0)',
                        pointBackgroundColor: 'rbga(0,0,0,0)',
                        pointHoverBackgroundColor: '#5AC53B',
                        pointHoverBorderColor: "#000000",
                        pointHoverBorderWidth: 4,
                        pointHoverRadius: 6,
                    }]
                }}
                options={{
                    plugins: {
                        legend: {
                            display: false
                        },
                        gridlines: {
                            display: false
                        }
                    }
                    ,
                    scales: {
                        y: {
                            ticks: {
                                display: true

                            },
                            grid: {
                                display: false,
                                drawBorder: false
                            },


                        },
                        x: {
                            ticks: {
                                display: false
                            },
                            grid: {
                                display: false,
                                drawBorder: false
                            }

                        }
                    }
                }}
            />

        </div>


    )
}

export default StockLineChart
