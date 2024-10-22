import React from 'react'
import NavBar from '../components/nav_bar'

export const FigmaForm = () => {
    const handleSearch = (searchTerm, selectedTheme) => {
        alert("El proyecto se ha subido correctamente");
      };
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
          <NavBar/>
      </div></>
      <h1 className='figmatitulo'>Subir tu Proyecto</h1>
      <div className='figmaform-container'>
        <div className='figmaform-column'>
            <label className='figmaform-input-label'>Nombre del Proyecto <span className='asterisco-rojo'>*</span></label>
            <input className='figmaform-input' type="text" placeholder='Ej: Feria de Software' />
            <label className='figmaform-input-label'>Fecha de Publicacion <span className='asterisco-rojo'>*</span></label>
            <input className='figmaform-input' type="date" />
            <label className='figmaform-input-label'>Foto del Proyecto <span className='asterisco-rojo'>*</span></label>
            <input className='figmaform-input' type="file" accept='image/*'/>
        </div>
        <div className='figmaform-column'>
            <label className='figmaform-input-label'>Nombre del Dominio <span className='asterisco-rojo'>*</span></label>
            <input className='figmaform-input' type="text" placeholder='Ej: www.FeriadeSoftware.cl' />
            <label className='figmaform-input-label'>Tema del Proyecto<span className='asterisco-rojo'>*</span></label>
            <select className='figmaform-input' id="opciones" name="opciones">
                <option value="IA">Inteligencia Artificial</option>
                <option value="RAV">Realidad Aumentada y Virtual</option>
                <option value="TE">Tecnologia en la Educacion</option>
            </select>
        </div>
        </div><div className='figmaexaminar'>
            <label className='figmaform-input-label'>Descripcion del Proyecto <span className='asterisco-rojo'>*</span></label>
            <input className='examinar-input' type="text" />
            <button className='submit-button' onClick={handleSearch}>Subir Proyecto</button>
        </div></>
      
  )
}

export default FigmaForm