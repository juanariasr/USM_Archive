import React from 'react';
import { Button } from '@mui/material'

import NavBar from '../components/nav_bar'
import Image from '../assets/proyecto_m.png';

function Mindfull() {
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
          Yoga personalizado con corrección de postura
          </div>
          <h2 className='label'>Dominio de la pagina</h2>
          <div className='parrafo-container'>
            https://mindfullmotion.feriadesoftware.cl
          </div>
          <h2 className='label'>Fecha de publicacion</h2>
          <div className='parrafo-container'>
            30 de Abril de 2023
          </div>
          <h2 className='label'>Tema del proyecto</h2>
          <div className='parrafo-container'>
            Inteligencia Artificial
          </div>
        </div>
      
    </>
        
  );
}

export default Mindfull;


