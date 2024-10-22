import React from 'react';
import { Button } from '@mui/material'

import NavBar from '../components/nav_bar'
import Image from '../assets/proyecto_a.png';

function Activate() {
  return (
    <><><div style={{
      backgroundColor: '#D9D9D9',
      height: '12vh',
      backgroundSize: 'cover',
      backgroundPosition: 'center',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      marginBottom: '50px',
    }}>
      <NavBar />
    </div></><div>
      <img src={Image} alt="Logo" style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto', width: '100%', maxHeight: '480px'}} />
      </div>
      <div className='page'>
          <h2 className='label'>Descripcion del proyecto</h2>
          <div className='parrafo-container'>
            Activate es una aplicación móvil que simula ser un gimnasio para tu cerebro. Por medio de Inteligencia Artificial, la dificultad de los ejercicios se regulará en base a tu desempeño.
          </div>
          <h2 className='label'>Dominio de la pagina</h2>
          <div className='parrafo-container'>
            https://activate.feriadesoftware.cl
          </div>
          <h2 className='label'>Fecha de publicacion</h2>
          <div className='parrafo-container'>
            30 de Abril de 2022
          </div>
          <h2 className='label'>Tema del proyecto</h2>
          <div className='parrafo-container'>
            Inteligencia Artificial y Ciencia de Datos
          </div>
        </div>
      
    </>
        
  );
}

export default Activate;
