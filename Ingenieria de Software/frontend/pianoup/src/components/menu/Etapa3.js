import React from 'react';
import { Link } from "react-router-dom";
import NavBar from '../barra/NavBar';
import './Etapa.css';

import etapa3Image from './images/etapa3.png';

function Etapa3() {
	return (
		<>
			<div className='navbar_container'>
				<NavBar />
			</div>
			<div className='cards__container'>
				<div className='cards__wrapper'>
					<ul className='cards__items'>
						<li className='cards__item' style = {{backgroundColor: '#F0E500'}}>
							<Link className='cards__item__link' to='/tempo' style={{textDecoration: 'none'}}>
							<figure className='cards__item__pic-wrap'>
								<img className='cards__item__img' src={etapa3Image}/>
							</figure>
							<div className='cards__item__info' style = {{backgroundColor: '#F0E500'}}>
								<h5 className='cards__item__text'>Tempo</h5>
							</div>
							</Link>
						</li>
						<li className='cards__item' style = {{backgroundColor: '#13CC00'}}>
							<Link className='cards__item__link' to='/menu-intensidad' style={{textDecoration: 'none'}}>
							<figure className='cards__item__pic-wrap'>
								<img className='cards__item__img' src={etapa3Image}/>
							</figure>
							<div className='cards__item__info' style = {{backgroundColor: '#13CC00'}}>
								<h5 className='cards__item__text'>Intensidad</h5>
							</div>
							</Link>
						</li>
					</ul>
				</div>
			</div>     
		</>
	);
}

export default Etapa3;

