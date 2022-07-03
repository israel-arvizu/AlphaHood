
const labels =
    ["09:30", "09:35", "09:40", "09:45", "09:50",
    "09:55", "10:00", "10:05", "10:10", "10:15", "10:20",
    "10:25", "10:30", "10:35", "10:40",
    "10:45", "10:50", "10:55", "11:00",
    "11:05", "11:10", "11:15", "11:20",
    "11:25", "11:30", "11:35", "11:40",
    "11:45", "11:55", "12:00", "12:05",
    "12:10", "12:15", "12:20", "12:25",
    "12:30", "12:35", "12:40", "12:45",
    "12:50", "12:55", "01:00", "01:05",
    "01:10", "01:15", "01:20", "01:25",
    "01:30", "01:35", "01:40", "01:45",
    "01:50", "01:55", "02:00", "02:05",
    "02:10", "02:15", "02:20", "02:25",
    "02:30", "02:35", "02:40", "02:45",
    "02:50", "02:55", "03:00", "03:05",
    "03:10", "03:15", "03:20", "03:25",
    "03:30", "03:35", "03:40", "03:45",
    "03:50", "03:55", "04:00"]


const valuesToArray = (obj) => {
    let graphValues = [];
    Object.values(obj).forEach(val => {
        graphValues.push(val)
    })
    return graphValues
}

const soloKeyToArray = (obj) => {
    let graphValues = [];
    Object.keys(obj).forEach(val => {
        graphValues.push(val)
    })
    return graphValues
}

const keysToArray = (obj) => {
    let graphKeys = [];
    Object.keys(obj).forEach(key => {
        const dateTime = key.split(' ')
        if((dateTime[1][4] == 0 || dateTime[1][4] == 5) && dateTime[1].substring(6, 8) == '00')
            graphKeys.push(dateTime[1].substring(5, 0))
    })
    return graphKeys;
}

export { valuesToArray, keysToArray, labels, soloKeyToArray};
