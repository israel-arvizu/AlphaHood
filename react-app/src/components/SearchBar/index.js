import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink, Link, useHistory } from 'react-router-dom';
import { searchStocks } from '../../store/searchBar';
import { getOneStock, get } from '../../store/stocks';
