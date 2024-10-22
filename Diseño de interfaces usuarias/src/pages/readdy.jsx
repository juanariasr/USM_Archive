import React from 'react'

import NavBar from '../components/nav_bar'
import Image from '../assets/proyecto_r.png';

function Readdy() {
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
            Readdy, una app móvil que mejora la comprensión lectora con ejercicios personalizados según el usuario utilizando teoría cognitiva e IA
          </div>
          <h2 className='label'>Dominio de la pagina</h2>
          <div className='parrafo-container'>
            https://readdy.feriadesoftware.cl
          </div>
          <h2 className='label'>Fecha de publicacion</h2>
          <div className='parrafo-container'>
            30 de Abril de 2023
          </div>
          <h2 className='label'>Tema del proyecto</h2>
          <div className='parrafo-container'>
            Tecnología en la Educación
          </div>
        </div>
      
    </>
        
  );
}

export default Readdy;
