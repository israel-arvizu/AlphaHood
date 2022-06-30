import React, { useEffect } from 'react'
import {Line} from "react-chartjs-2"
import Chart from 'chart.js/auto';
import { dayData, graphData } from './LinechartData';
import { useDispatch, useSelector } from 'react-redux';
import { loadPortfolio } from '../../store/stocks';

function LineChart(){
    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)
    const portfolio = useSelector(state => state.stocks.portfolio)

    useEffect(() => {
        dispatch(loadPortfolio(user.id))
    }, [])

    const dayData1 =  {

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
    }]}

    return (
        <div className='linegraph'>
            <Line

            data={dayData1}
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
