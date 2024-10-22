import React from 'react';
import { Routes, Route, BrowserRouter, Link } from 'react-router-dom';
import Image from 'react-bootstrap/Image';
import './Menu.css';
import NavBar from '../barra/NavBar';

import etapa1Image from './images/etapa1.png';
import etapa2Image from './images/etapa2.png';
import etapa3Image from './images/etapa3.png';

function Menu({ user }) {
  return (
        <div className='parent_container'>
            <div className='navbar_container'>
                <NavBar menu={1}/>
            </div>
            <div className='title_container_menu'>
                <h1>Bienvenido usuario {user}</h1>
            </div>
            <div className='cards__container'>
                <div className='cards__wrapper'>
                    <ul className='cards__items'>
                        <li className='cards__item' style = {{backgroundColor: '#E30101'}}>
                            <Link className='cards__item__link' to='/etapa1' style={{textDecoration: 'none'}}>
                            <figure className='cards__item__pic-wrap'>
                                <img className='cards__item__img' src={etapa1Image}/>
                            </figure>
                            <div className='cards__item__info' style = {{backgroundColor: '#E30101'}}>
                                <h5 className='cards__item__text'>Etapa 1</h5>
                            </div>
                            </Link>
                        </li>
                        <li className='cards__item' style = {{backgroundColor: '#F0E500'}}>
                            <Link className='cards__item__link' to='/etapa2' style={{textDecoration: 'none'}}>
                            <figure className='cards__item__pic-wrap'>
                                <img className='cards__item__img' src={etapa2Image}/>
                            </figure>
                            <div className='cards__item__info' style = {{backgroundColor: '#F0E500'}}>
                                <h5 className='cards__item__text'>Etapa 2</h5>
                            </div>
                            </Link>
                        </li>
                        <li className='cards__item' style = {{backgroundColor: 'blue'}}>
                            <Link className='cards__item__link' to='/etapa3' style={{textDecoration: 'none'}}>
                            <figure className='cards__item__pic-wrap'>
                                <img className='cards__item__img' src={etapa3Image}/>
                            </figure>
                            <div className='cards__item__info'style = {{backgroundColor: 'blue'}}>
                                <h5 className='cards__item__text'>Etapa 3</h5>
                            </div>
                            </Link>
                        </li>
                        <li className='cards__item' style = {{backgroundColor: 'purple'}}>
                            <Link className='cards__item__link' to='/juegos' style={{textDecoration: 'none'}}>
                            <figure className='cards__item__pic-wrap'>
                                <img className='cards__item__img' src='logo.png'/>
                            </figure>
                            <div className='cards__item__info' style = {{backgroundColor: 'purple'}}>
                                <h5 className='cards__item__text'>Juegos</h5>
                            </div>
                            </Link>
                        </li>
                    </ul>
                </div>
            </div>
        </div>     
  );
}

export default Menu;
