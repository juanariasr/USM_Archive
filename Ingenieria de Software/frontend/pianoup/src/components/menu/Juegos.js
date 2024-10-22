import React from 'react';
import { Link } from "react-router-dom";
import './Etapa.css';
import NavBar from '../barra/NavBar';

function Juegos() {
	return (
		<>
			<div className='navbar_container'>
				<NavBar />
			</div>
			<div className='cards__container'>
				<div className='cards__wrapper'>
					<ul className='cards__items'>
						<li className='cards__item' style = {{backgroundColor: '#FF00AA'}}>
							<Link className='cards__item__link' to='/memorice' style={{textDecoration: 'none'}}>
							<figure className='cards__item__pic-wrap'>
								<img className='cards__item__img' src='logo.png'/>
							</figure>
							<div className='cards__item__info' style = {{backgroundColor: '#FF00AA'}}>
								<h5 className='cards__item__text'>Memorice</h5>
							</div>
							</Link>
						</li>
					</ul>
				</div>
			</div>
		</>
	);
}

export default Juegos;