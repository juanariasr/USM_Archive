import React from 'react';
import { Link } from "react-router-dom";
import './Etapa.css';
import './Menu.css';
import NavBar from '../barra/NavBar';

import etapa1Image from './images/etapa1.png';

function Etapa1() {
	return (
		<>
			<div className='navbar_container'>
				<NavBar />
			</div>
			<div className='cards__container'>
				<div className='cards__wrapper'>
					<ul className='cards__items'>
						<li className='cards__item' style = {{backgroundColor: '#13CC00'}}>
							<Link className='cards__item__link' to='/llavesol' style={{textDecoration: 'none'}}>
							<figure className='cards__item__pic-wrap'>
								<img className='cards__item__img' src={etapa1Image}/>
							</figure>
							<div className='cards__item__info' style = {{backgroundColor: '#13CC00'}}>
								<h5 className='cards__item__text'>Llave de Sol</h5>
							</div>
							</Link>
						</li>
						<li className='cards__item' style = {{backgroundColor: '#FF00AA'}}>
							<Link className='cards__item__link' to='/notas/' style={{textDecoration: 'none'}}>
							<figure className='cards__item__pic-wrap'>
								<img className='cards__item__img' src={etapa1Image}/>
							</figure>
							<div className='cards__item__info' style = {{backgroundColor: '#FF00AA'}}>
								<h5 className='cards__item__text'>Notas Musicales</h5>
							</div>
							</Link>
						</li>
						<li className='cards__item' style = {{backgroundColor: '#FF9300'}}>
							<Link className='cards__item__link' to='/metronome' style={{textDecoration: 'none'}}>
							<figure className='cards__item__pic-wrap'>
								<img className='cards__item__img' src={etapa1Image}/>
							</figure>
							<div className='cards__item__info' style = {{backgroundColor: '#FF9300'}}>
								<h5 className='cards__item__text'>Pulso</h5>
							</div>
							</Link>
						</li>
						<li className='cards__item' style = {{backgroundColor: '#E30101'}}>
							<Link className='cards__item__link' to='/menu-frecuencia' style={{textDecoration: 'none'}}>
							<figure className='cards__item__pic-wrap'>
								<img className='cards__item__img' src={etapa1Image}/>
							</figure>
							<div className='cards__item__info' style = {{backgroundColor: '#E30101'}}>
								<h5 className='cards__item__text'>Altura</h5>
							</div>
							</Link>
						</li>
					</ul>
				</div>
			</div>     
		</>
	);
}

export default Etapa1;
