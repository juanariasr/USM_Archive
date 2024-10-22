import React from 'react';
import NavBar from '../components/nav_bar';
import EventIcon from '@mui/icons-material/Event';
import LocationOnIcon from '@mui/icons-material/LocationOn';
import PeopleIcon from '@mui/icons-material/People';
import { Link } from 'react-router-dom';

const versionData = [
  { numero: '30°', feria: 'Feria de Software', ano: '2022', fecha: '25 de Noviembre de 2022', ubicacion: 'Universidad Técnica Federico Santa María', sede: 'Campus Casa Central Valparaíso', ubi: 'Avenida España 1680, Valparaíso' , cantidadPersonas: '29 expositores' },
  { numero: 'XXIX', feria: 'Feria de Software', ano: '2021', fecha: '18 de Marzo de 2022', ubicacion: 'Universidad Técnica Federico Santa María', sede: 'Formato híbrido', ubi: 'San Joaquín, Santiago' , cantidadPersonas: '24 expositores' },
  { numero: 'XXVIII', feria: 'Feria de Software', ano: '2020', fecha: '17 de Diciiembre de 2020', ubicacion: 'Universidad Técnica Federico Santa María', sede: 'Online' , cantidadPersonas: '33 expositores' },
  { numero: 'XXVII', feria: 'Feria de Software', ano: '2019', fecha: 'Evento Presencial Suspendido', ubicacion: 'Universidad Técnica Federico Santa María', sede: 'Campus Casa Central', ubi: 'Avenida España 1680, Valparaíso' , cantidadPersonas: '25 expositores' },
  { numero: 'XXVI', feria: 'Feria de Software', ano: '2018', fecha: '30 de Noviembre de 2018', ubicacion: 'Universidad Técnica Federico Santa María', sede: 'Campus Santiago San Joaquín', ubi: 'Avenida Vicuña Mackenna 3939, Santiago' , cantidadPersonas: '28 expositores' },
  { numero: 'XXV', feria: 'Feria de Software', ano: '2017', fecha: '10 de Noviembre de 2017', ubicacion: 'Universidad Técnica Federico Santa María', sede: 'Campus Casa Central Valparaíso', ubi: 'Avenida España 1680, Valparaíso' , cantidadPersonas: '18 expositores' },
  { numero: 'XXIV', feria: 'Feria de Software', ano: '2016', fecha: '18 de Noviembre de 2016', ubicacion: 'Universidad Técnica Federico Santa María', sede: 'Campus Santiago San Joaquín', ubi: 'Avenida Vicuña Mackenna 3939, Santiago' , cantidadPersonas: '9 expositores' },
  { numero: 'XXIII', feria: 'Feria de Software', ano: '2015', fecha: '18 de Marzo de 2016', ubicacion: 'Universidad Técnica Federico Santa María', sede: 'Campus Casa Central Valparaíso', ubi: 'Avenida España 1680, Valparaíso' , cantidadPersonas: '16 expositores' },
  { numero: 'XXII', feria: 'Feria de Software', ano: '2014', fecha: '14 de Noviembre de 2014', ubicacion: 'Universidad Técnica Federico Santa María', sede: 'Campus Santiago San Joaquín', ubi: 'Avenida Vicuña Mackenna 3939, Santiago' , cantidadPersonas: '21 expositores' },
  { numero: 'XXI', feria: 'Feria de Software', ano: '2013', fecha: '	21 de Marzo de 2014', ubicacion: 'Universidad Técnica Federico Santa María', sede: 'Campus Casa Central Valparaíso', ubi: 'Avenida España 1680, Valparaíso' , cantidadPersonas: '21 expositores' },
  { numero: 'XX', feria: 'Feria de Software', ano: '2012', fecha: '9 de Noviembre de 2012', ubicacion: 'Universidad Técnica Federico Santa María', sede: 'Campus Santiago San Joaquín', ubi: 'Avenida Vicuña Mackenna 3939, Santiago' , cantidadPersonas: '46 expositores' },
];

export const Versiones = () => {
  return (
    <>
      <div style={{
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
      </div>
      <div style={{ marginLeft: '180px', textDecoration: 'underline', textDecorationColor: '#FFFFFF' }}>
        <h1>Versiones Anteriores</h1>
      </div>
      <div style={{ display: 'flex', justifyContent: 'center', flexWrap: 'wrap' }}>
        {versionData.map((version, index) => (
          <div key={index} style={{
            border: '1px solid #ccc',
            borderRadius: '10px',
            padding: '10px',
            textAlign: 'justify',
            margin: '10px',
          }}>
            <Link to="/feria_old">
            <p>{`${version.numero} ${version.feria}`}</p>
            </Link>
            <p> {version.ano}</p>
            <p><EventIcon /> {version.fecha}</p>
            <p><LocationOnIcon /> {version.ubicacion}</p>
            <p> {version.sede}</p>
            <p> {version.ubi}</p>
            <p><PeopleIcon /> {`${version.cantidadPersonas}`}</p>
          </div>
        ))}
      </div>
    </>
  );
}

export default Versiones;