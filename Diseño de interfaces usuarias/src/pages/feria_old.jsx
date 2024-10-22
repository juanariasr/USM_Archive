import React from 'react';
import { Link } from 'react-router-dom';
import Image1 from '../assets/activate.png';
import Image2 from '../assets/juno.png';
import Image3 from '../assets/onstage.png';
import NavBar from '../components/nav_bar';


function FeriaOld() {
  const linkStyles = {
    textDecoration: 'none',
    color: 'inherit',
  };

  const boxStyles = {
    border: '1px solid #ccc',
    borderRadius: '10px',
    padding: '10px',
    textAlign: 'center',
  };

  const backgroundStyles = {
    backgroundColor: '#D9D9D9',
    height: '12vh',
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: '50px',
  };

  const containerStyles = {
    position: 'relative',
  };

  return (
    <div style={containerStyles}>
      <div style={backgroundStyles}>
        <NavBar />
      </div>
      <div style={{ marginLeft: '180px', textDecoration: 'underline', textDecorationColor: '#FFFFFF' }}>
        <h1>30° Feria de Software - 2022</h1>
      </div>
      <div style={{
        display: 'flex',
        justifyContent: 'center',
        marginTop: '20px',
      }}>
        <div className="box" style={{ margin: '50px', textAlign: 'left', ...boxStyles, border: 'none', borderRadius: '10px' }}>
          <Link to="/activate" style={{ ...linkStyles }}>
            <img src={Image1} width={300} height={300} alt="Descripción de la imagen" style={{ borderRadius: '10px', marginBottom: '10px' }} />
            <div style={{ paddingLeft: '10px' }}>
              <h2 style={{ margin: '0' }}>Activate</h2>
              <p style={{ color: '#999', fontSize: '0.9em', margin: '0' }}>activate.feriadesoftware.cl</p>
            </div>
          </Link>
        </div>

        <div className="box" style={{ margin: '50px', textAlign: 'left', ...boxStyles, border: 'none', borderRadius: '10px' }}>
          <Link to="/junoapp" style={{ ...linkStyles }}>
            <img src={Image2} width={300} height={300} alt="Descripción de la imagen" style={{ borderRadius: '10px', marginBottom: '10px' }} />
            <div style={{ paddingLeft: '10px' }}>
              <h2 style={{ margin: '0' }}>Juno App</h2>
              <p style={{ color: '#999', fontSize: '0.9em', margin: '0' }}>junoapp.feriadesoftware.cl</p>
            </div>
          </Link>
        </div>

        <div className="box" style={{ margin: '50px', textAlign: 'left', ...boxStyles, border: 'none', borderRadius: '10px' }}>
          <Link to="/onstage" style={{ ...linkStyles }}>
            <img src={Image3} width={300} height={300} alt="Descripción de la imagen" style={{ borderRadius: '10px', marginBottom: '10px' }} />
            <div style={{ paddingLeft: '10px' }}>
              <h2 style={{ margin: '0' }}>OnStage</h2>
              <p style={{ color: '#999', fontSize: '0.9em', margin: '0' }}>onstage.feriadesoftware.cl</p>
            </div>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default FeriaOld;