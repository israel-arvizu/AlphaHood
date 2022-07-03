
const topTen = ["RDFN", "APPL", "ERIC", "PANW", "ROKU", "TSLA", "AMZN", "PYPL", "NVDA", "SHOP"]
const creator = ["GOOGL", "NVDA", "NKE", "MLAI" ]
const mostpop = ["APPL", "MSFT", "AMZN", "TSLA", "GOOGL", "GOOG", "NVDA", "BRK.B",
                "META", "UNH", "JNJ","JPM","V","PG","XOM","HD","CVX","MA","BAC",
                "ABBV","PFE", "AVGO","COST","DIS","KO"]
const tech = ["HPE", "MNDT", "ARW", "HPO","INTC","GDDY","BKI","SNX","ON","NATI","SWCH","AZPN","PANW", "PSTG", "DGI"]
const auto = ["TSLA", "GM","F","TM","KMX","CVNA","RACE","STLA","NIO","HMC"]

const topTenDefault = [
{marketCap: 55563132928, name: 'Amazon.com, Inc.', price: 109.56, ticker: 'AMZN', todayPerformance: 3.08},
{marketCap: 83890003968, name: 'PayPal Holdings, Inc.', price: 71.4, ticker: 'PYPL', todayPerformance: 2.23},
{marketCap: 361913155584, name: 'NVIDIA Corporation', price: 145.23, ticker: 'NVDA', todayPerformance: -2.52},
{marketCap: 3929987840, name: 'Shopify Inc.', price: 31.41, ticker: 'SHOP', todayPerformance: -2.09},
{marketCap: 945109760, name: 'Redfin Corporation', price: 8.96, ticker: 'RDFN', todayPerformance: 7.56},
{marketCap: 25096460288, name: 'Ericsson', price: 7.43, ticker: 'ERIC', todayPerformance: 0.41},
{marketCap: 50147196928, name: 'Palo Alto Networks, Inc.', price: 508.25, ticker: 'PANW', todayPerformance: 2.68},
{marketCap: 11274400768, name: 'Roku, Inc.', price: 83.91, ticker: 'ROKU', todayPerformance: 1.66},
{marketCap: 684694372352, name: 'Tesla, Inc.', price: 681.79, ticker: 'TSLA', todayPerformance: 0.12}]


const creatorDefault = [
{marketCap: 1434225868800, name: 'Alphabet Inc.', price: 2174.75, ticker: 'GOOGL', todayPerformance: 0.75},
{marketCap: 361913155584, name: 'NVIDIA Corporation', price: 145.23, ticker: 'NVDA', todayPerformance: -2.52},
{marketCap: 159234048000, name: 'Nike, Inc.', price: 101.18, ticker: 'NKE', todayPerformance: -0.45},
{marketCap: 251813568, name: 'McLaren Technology Acquisition ', price: 10.01, ticker: 'MLAI', todayPerformance: 0.5}]

const mostPopDefault = [
{marketCap: 1948921233408, name: 'Microsoft Corporation', price: 259.58, ticker: 'MSFT', todayPerformance: 1.24},
{marketCap: 55563132928, name: 'Amazon.com, Inc.', price: 109.56, ticker: 'AMZN', todayPerformance: 3.08},
{marketCap: 684694372352, name: 'Tesla, Inc.', price: 681.79, ticker: 'TSLA', todayPerformance: 0.12},
{marketCap: 1443601317888, name: 'Alphabet Inc.', price: 2174.75, ticker: 'GOOGL', todayPerformance: 0.75},
{marketCap: 1447991443456, name: 'Alphabet Inc.', price: 2181.62, ticker: 'GOOG', todayPerformance: 0.69},
{marketCap: 361913155584, name: 'NVIDIA Corporation', price: 145.23, ticker: 'NVDA', todayPerformance: -2.52},
{marketCap: 487313735680, name: 'UnitedHealth Group Incorporated', price: 517.4, ticker: 'UNH', todayPerformance: 0.99},
{marketCap: 472604377088, name: 'Johnson & Johnson', price: 179.52, ticker: 'JNJ', todayPerformance: 1.17},
{marketCap: 345382191104, name: 'JP Morgan Chase & Co.', price: 114.05, ticker: 'JPM', todayPerformance: 1.24},
{marketCap: null, name: 'Visa Inc.', price: 199.18, ticker: 'V', todayPerformance: 1.21},
{marketCap: 353578909696, name: 'Procter & Gamble Company (The)', price: 146.11, ticker: 'PG', todayPerformance: 1.3},
{marketCap: 373022556160, name: 'Exxon Mobil Corporation', price: 87.55, ticker: 'XOM', todayPerformance: 0.93},
{marketCap: 291426500608, name: 'Home Depot, Inc. (The)', price: 279.08, ticker: 'HD', todayPerformance: 1.21},
{marketCap: 282425851904, name: 'Chevron Corporation', price: 146.51, ticker: 'CVX', todayPerformance: -0.06},
{marketCap: 312688934912, name: 'Mastercard Incorporated', price: 318.24, ticker: 'MA', todayPerformance: 1.32},
{marketCap: 258289549312, name: 'Bank of America Corporation', price: 31.56, ticker: 'BAC', todayPerformance: 1.87},
{marketCap: 271899934720, name: 'AbbVie Inc.', price: 153.8, ticker: 'ABBV', todayPerformance: 0.47},
{marketCap: 293609242624, name: 'Pfizer, Inc.', price: 52.31, ticker: 'PFE', todayPerformance: 0.52},
{marketCap: 197287706624, name: 'Broadcom Inc.', price: 477.84, ticker: 'AVGO', todayPerformance: -0.33},
{marketCap: 215401529344, name: 'Costco Wholesale Corporation', price: 485.76, ticker: 'COST', todayPerformance: 0.95},
{marketCap: 174749827072, name: 'Walt Disney Company (The)', price: 96.14, ticker: 'DIS', todayPerformance: 2.02},
{marketCap: 278084255744, name: 'Coca-Cola Company (The)', price: 64.38, ticker: 'KO', todayPerformance: 2}]

const techDefault = [
{marketCap: 16762982400, name: 'Hewlett Packard Enterprise Comp', price: 12.96, ticker: 'HPE', todayPerformance: -1.97},
{marketCap: 5236516352, name: 'Mandiant, Inc.', price: 21.82, ticker: 'MNDT', todayPerformance: 0},
{marketCap: 7781759488, name: 'Arrow Electronics, Inc.', price: 111.76, ticker: 'ARW', todayPerformance: 0.1},
{marketCap: 147794788352, name: 'Intel Corporation', price: 36.34, ticker: 'INTC', todayPerformance: -2.02},
{marketCap: 11779091456, name: 'GoDaddy Inc.', price: 70.87, ticker: 'GDDY', todayPerformance: 1.34},
{marketCap: 10278415360, name: 'Black Knight, Inc.', price: 66.18, ticker: 'BKI', todayPerformance: 1.22},
{marketCap: 8874038272, name: 'TD SYNNEX Corporation', price: 92.43, ticker: 'SNX', todayPerformance: 1.68},
{marketCap: 20180262912, name: 'ON Semiconductor Corporation', price: 46.84, ticker: 'ON', todayPerformance: -4.97},
{marketCap: 4090979584, name: 'National Instruments Corporatio', price: 31.02, ticker: 'NATI', todayPerformance: -0.42},
{marketCap: 8081520128, name: 'Switch, Inc.', price: 33.45, ticker: 'SWCH', todayPerformance: -0.12},
{marketCap: 12797532160, name: 'Aspen Technology, Inc.', price: 191.24, ticker: 'AZPN', todayPerformance: 4.41},
{marketCap: 50147196928, name: 'Palo Alto Networks, Inc.', price: 508.25, ticker: 'PANW', todayPerformance: 2.68},
{marketCap: 7179087872, name: 'Pure Storage, Inc.', price: 24.76, ticker: 'PSTG', todayPerformance: -3.05}]

const autoDefault = [
{marketCap: 684694372352, name: 'Tesla, Inc.', price: 681.79, ticker: 'TSLA', todayPerformance: 0.12},
{marketCap: 46735372288, name: 'General Motors Company', price: 32.19, ticker: 'GM', todayPerformance: 2.91},
{marketCap: 45237432320, name: 'Ford Motor Company', price: 11.32, ticker: 'F', todayPerformance: 1.98},
{marketCap: 215430119424, name: 'Toyota Motor Corporation', price: 155.47, ticker: 'TM', todayPerformance: 1.69},
{marketCap: 15000678400, name: 'CarMax Inc', price: 92.67, ticker: 'KMX', todayPerformance: 2.07},
{marketCap: 3884112128, name: 'Carvana Co.', price: 21.87, ticker: 'CVNA', todayPerformance: -4.75},
{marketCap: 47244922880, name: 'Ferrari N.V.', price: 187.94, ticker: 'RACE', todayPerformance: 2.63},
{marketCap: 38843867136, name: 'Stellantis N.V.', price: 12.4, ticker: 'STLA', todayPerformance: 2.14},
{marketCap: 33974575104, name: 'NIO Inc.', price: 21.36, ticker: 'NIO', todayPerformance: -4.3},
{marketCap: 41505382400, name: 'Honda Motor Company, Ltd.', price: 24.21, ticker: 'HMC', todayPerformance: 1.94}]


export {topTen, creator, mostpop, tech, auto, topTenDefault, creatorDefault, mostPopDefault, techDefault, autoDefault}
