import React from 'react';
import { Button } from '@mui/material'

import NavBar from '../components/nav_bar'
import Image from '../assets/proyecto_j.png';

function JunoApp() {
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
            App para gestionar y enriquecer comunidades mediante el valor que cada integrante puede brindar.
          </div>
          <h2 className='label'>Dominio de la pagina</h2>
          <div className='parrafo-container'>
            https://junoapp.feriadesoftware.cl
          </div>
          <h2 className='label'>Fecha de publicacion</h2>
          <div className='parrafo-container'>
            30 de Abril de 2022
          </div>
          <h2 className='label'>Tema del proyecto</h2>
          <div className='parrafo-container'>
            Transformación Digital y Social
          </div>
        </div>
      
    </>
        
  );
}

export default JunoApp;
