import React from 'react'
import { NavLink } from 'react-router-dom'

import logo from '../assets/fesw-logo-w.png'
import SearchBar from '../components/searchbar';

export const NavBar = ({ onThemeSelect }) => {
  const handleSearch = (searchTerm, selectedTheme) => {
    // Redirige a la página correspondiente según la búsqueda
    switch (searchTerm.toLowerCase()) {
      case 'mindfull motion':
        window.location.href = '/mindfullmotion';
        break;
      case 'cuisinear':
        window.location.href = '/cuisinear';
        break;
      case 'readdy':
        window.location.href = '/readdy';
        break;
      default:
        // Si no es una búsqueda directa, actualiza el tema seleccionado
        onThemeSelect(selectedTheme);
        break;
    }
  };

  const searchBarStyles = {
    position: 'absolute',
    top: '50%',
    right: '20px', // Ajuste para posicionar a la derecha
    transform: 'translateY(-50%)', // Ajuste para centrar verticalmente
    maxWidth: '100px',
  };

  return (
    <nav className='nav-bar' style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '95%' }}>
      <img src={logo} height={80} alt="Imagen 1" />
      <SearchBar style={searchBarStyles} onSearch={handleSearch} />
      <div>
        <NavLink
          className={({ isActive }) => `nav-bar__link ${isActive ? 'nav-bar__link--active' : ''}`}
          to='/'
        >
          Inicio
        </NavLink>
        <NavLink
          className={({ isActive }) => `nav-bar__link ${isActive ? 'nav-bar__link--active' : ''}`}
          to='/v_anteriores'
        >
          Versiones Anteriores
        </NavLink>
        <NavLink
          className={({ isActive }) => `nav-bar__link ${isActive ? 'nav-bar__link--active' : ''}`}
          to='/figmaform'
        >
          Subir Proyecto
        </NavLink>
      </div>
    </nav>
  )
}



export default NavBar
