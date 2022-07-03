import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import Dashboard from './components/dashboard-component/Dashboard';
import User from './components/User';
import TrendingLists from './components/TrendingLists'
import StockDetail from './components/StockDetail'
import SplashPage  from './components/splashpage/splashpage';
import Wallet from './components/walletComponent';
import { authenticate } from './store/session';
import { ModalProvider } from './context/Modal';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();


  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
  <ModalProvider>
    <BrowserRouter>
      <Switch>
        <Route path='/' exact={true}>
          <SplashPage />
        </Route>
        <Route path='/login' exact={true}>
          <LoginForm />
        </Route>
        <Route path='/sign-up' exact={true}>
          <SignUpForm />
        </Route>
        <ProtectedRoute path='/wallet' exact={true}>
          <Wallet />
        </ProtectedRoute>
        <ProtectedRoute path='/users/:userId' exact={true} >
          <User />
        </ProtectedRoute>
        <ProtectedRoute path='/dashboard' exact={true} >
          <Dashboard />
        </ProtectedRoute>
        <ProtectedRoute path='/trendinglists/:list' exact={true} >
          <TrendingLists />
        </ProtectedRoute>
        <ProtectedRoute path='/stocks/:ticker' exact={true}>
          <StockDetail />
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  </ModalProvider>
  );
}

export default App;
