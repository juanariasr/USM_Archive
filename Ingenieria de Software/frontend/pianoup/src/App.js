import './App.css';
import React, { useState} from 'react';

import { Routes, Route } from 'react-router-dom';
import { Image } from 'react-bootstrap';

//Middleware
import Middleware_login from './components/middleware/Middleware_login';

// User
import Home from './Home';
import Login from './components/user/Login';
import Register from './components/user/Register';

// Menu
import Etapa1 from './components/menu/Etapa1';
import Etapa2 from './components/menu/Etapa2';
import Etapa3 from './components/menu/Etapa3';
import Juegos from './components/menu/Juegos';

// Actividades
import Notas from './components/actividades/notas-musicales/Notas'
import { EmparejarDuracion} from './components/actividades/emparejar-duracion/EmparejarDuracion';
import MenuDuracion from './components/actividades/emparejar-duracion/MenuDuracion';
import { EmparejarTimbre} from './components/actividades/emparejar-timbre/EmparejarTimbre';
import MenuTimbre from './components/actividades/emparejar-timbre/MenuTimbre';
import { EmparejarIntensidad} from './components/actividades/emparejar-intensidad/EmparejarIntensidad';
import MenuIntensidad from './components/actividades/emparejar-intensidad/MenuIntensidad';
import { EmparejarFrecuencia} from './components/actividades/emparejar-frecuencia/EmparejarFrecuencia';
import MenuFrecuencia from './components/actividades/emparejar-frecuencia/MenuFrecuencia';
import Memorice from './components/actividades/memorice/MenuMem';
import MemoriceGame from './components/actividades/memorice/Memorice';
import Tempo from './components/actividades/tempo/Tempo';
import Metronome from "./components/actividades/metronome/Metronome";
import {Pentagrama} from './components/actividades/llave-de-sol/Pentagrama';
import {LlaveSol} from './components/actividades/llave-de-sol/LlaveSol';

function App() {

  const [imagesSelected, setImagesSelected] = useState([]);
  //Emparejar
  const [timbreSelected, setTimbreSelected] = useState([]);
  const [intensidadSelected, setIntensidadSelected] = useState([]);
  const [frecuenciaSelected, setFrecuenciaSelected] = useState([]);
  const [duracionSelected, setDuracionSelected] = useState([]);

  const[imagen,SetImagen] = React.useState(null);

  return (
        <div>
            <Routes>
                <Route path="/" element={<Login />} />
                <Route path="/m-login" element={<Middleware_login />} />
                <Route path="/register" element={<Register/>} />
                <Route path="/home" element={<Home />} />
                <Route path="/etapa1" element={<Etapa1 />} />
                <Route path="/etapa2" element={<Etapa2 />} />
                <Route path="/etapa3" element={<Etapa3 />} />
                <Route path="/juegos" element={<Juegos/>} />
                <Route path="/memorice" element={<Memorice setImagesSelected={setImagesSelected}/>}/>
                <Route path="/memoriceGame" element={<MemoriceGame imagesSelected={imagesSelected}/>}/>
                <Route path="/pentagrama" element={<Pentagrama
                  imagen = {imagen}
                />} />
                <Route path="/llavesol" element={<LlaveSol
                  SetImagen = {SetImagen}
                />} />
                <Route path="/tempo" element={<Tempo/>}/>
                <Route path="/menu-duracion" element={<MenuDuracion setDuracionSelected={setDuracionSelected}/>}/>
                <Route path="/emparejar-duracion" element={<EmparejarDuracion duracionSelected={duracionSelected}/>}/>
                <Route path="/menu-timbre" element={<MenuTimbre setTimbreSelected={setTimbreSelected}/>}/>
                <Route path="/emparejar-timbre" element={<EmparejarTimbre timbreSelected = {timbreSelected}/>}/>
                <Route path="/menu-intensidad" element={<MenuIntensidad setIntensidadSelected={setIntensidadSelected}/>}/>
                <Route path="/emparejar-intensidad" element={<EmparejarIntensidad intensidadSelected = {intensidadSelected}/>}/>
                <Route path="/menu-frecuencia" element={<MenuFrecuencia setFrecuenciaSelected={setFrecuenciaSelected}/>}/>
                <Route path="/emparejar-frecuencia" element={<EmparejarFrecuencia frecuenciaSelected = {frecuenciaSelected}/>}/>
                <Route path="/metronome" element={<Metronome/>}/>
                <Route path="/notas/" element={<Notas/>}/>
            </Routes>
      </div>
  );
}

export default App;
