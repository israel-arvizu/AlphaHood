import React, { useEffect, useState } from 'react'
import {Line} from "react-chartjs-2"
import Chart from 'chart.js/auto';
import {valuesToArray, keysToArray} from './LinechartData';
import { useDispatch, useSelector } from 'react-redux';

function LineChart({portfolio}){
    const [update, setUpdate] = useState(false);
    const [portData, setPortData] = useState(valuesToArray(portfolio))
    const [portLabels, setPortLabels] = useState(keysToArray(portfolio))

    if(!update){
        setPortData(valuesToArray(portfolio))
        setPortLabels(keysToArray(portfolio))
        setUpdate(true)
    }


    return (
        <div className='linegraph'>
            <Line
            data={{
                labels: portLabels,
                datasets:[{
                data: portData,
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
            }]}}
            options={{
                plugins:{
                legend:{
                    display: false
                },
                gridlines:{
                    display: false
                }},
                options: {
                    maintainAspectRatio: false,
                },
                scales:{
                    y: {
                        ticks:{
                            display:false

                        },
                        grid:{
                            display: false,
                            drawBorder: false
                        },


                    },
                    x:{
                        ticks:{
                            display:false
                        },
                        grid:{
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

export default LineChart
