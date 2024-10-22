import React from 'react';
import { Link } from "react-router-dom";
import './Etapa.css';
import NavBar from '../barra/NavBar';

import etapa2Image from './images/etapa2.png';

function Etapa2() {
	return (
		<>
			<div className='navbar_container' >
				<NavBar />
			</div>
			<div className='cards__container'>
				<div className='cards__wrapper'>
					<ul className='cards__items'>
						<li className='cards__item' style = {{backgroundColor: '#FF9300'}}>
							<Link className='cards__item__link' to='/menu-timbre' style={{textDecoration: 'none'}}>
							<figure className='cards__item__pic-wrap'>
								<img className='cards__item__img' src={etapa2Image}/>
							</figure>
							<div className='cards__item__info' style = {{backgroundColor: '#FF9300'}}>
								<h5 className='cards__item__text'>Timbre</h5>
							</div>
							</Link>
						</li>
						<li className='cards__item' style = {{backgroundColor: '#00B6FF'}}>
							<Link className='cards__item__link' to='/menu-duracion' style={{textDecoration: 'none'}}>
							<figure className='cards__item__pic-wrap'>
								<img className='cards__item__img' src={etapa2Image}/>
							</figure>
							<div className='cards__item__info' style = {{backgroundColor: '#00B6FF'}}>
								<h5 className='cards__item__text'>Duración</h5>
							</div>
							</Link>
						</li>
					</ul>
				</div>
			</div>     
		</>
	);
}
export default Etapa2;
