import React, { useEffect, useState } from 'react'
import {Line} from "react-chartjs-2"
import Chart from 'chart.js/auto';
import { useDispatch, useSelector } from 'react-redux';

function StockLineChart({stockHistory}){

    return (
        <div className='linegraph'>
            <Line
            data={{
                labels: [0, 1, 2, 3, 4, 5],
                datasets:[{
                data: [0, 1, 2, 3, 4, 5],
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

export default StockLineChart
