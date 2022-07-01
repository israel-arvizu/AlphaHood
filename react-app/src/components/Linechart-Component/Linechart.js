import React, { useEffect, useState } from 'react'
import {Line} from "react-chartjs-2"
import Chart from 'chart.js/auto';
import {valuesToArray, keysToArray} from './LinechartData';
import { useDispatch, useSelector } from 'react-redux';

function LineChart({portfolio}){

    const dayData =  {
        labels:[],
        datasets:[{
        data: [],
        fill: false,
        backgroundColor:"black",
        borderColor:"#5AC53B",
        borderWidth: 2,
        pointStyle: Line,
        pointBorderColor:'rgba(0,0,0,0)',
        pointBackgroundColor:'rbga(0,0,0,0)',
        pointHoverBackgroundColor:'#5AC53B',
        pointHoverBorderColor:"#000000",
        pointHoverBorderWidth: 4,
        pointHoverRadius: 6,
    }]}

        if(portfolio != undefined){
            dayData.datasets[0].data = valuesToArray(portfolio)
            dayData.labels = keysToArray(portfolio)
        }

    return (
        <div className='linegraph'>
            <Line
            data={dayData}
            options={{
                plugins:{
                legend:{
                    display: false
                },
                gridlines:{
                    display: false
                }}
            ,
                scales:{
                    y: {
                        ticks:{
                            display:true

                        },
                        grid:{
                            display: false,
                            drawBorder: false
                        },


                    },
                    x:{
                        ticks:{
                            display:true
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
