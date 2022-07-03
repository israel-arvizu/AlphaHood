import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import session from './session'
import newsReducer from './news';
import stocksReducer from './stocks';
import listsReducer from './list';
import listStockReducer from './liststock';
import owndedStocksReducer from './ownedStocks'


const rootReducer = combineReducers({
  session,
  newsReducer,
  stocks: stocksReducer,
  lists: listsReducer,
  listStockReducer,
  ownedStocks: owndedStocksReducer

});


let enhancer;

if (process.env.NODE_ENV === 'production') {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require('redux-logger').default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
