import React, { useState,useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Howl } from 'howler';
import './Tempo.css';
import axios from 'axios';
import NavBar from '../../barra/NavBar';

const baseUrl = 'http://localhost:8000/tempo';

export default function Tempo() {
  const [currentSound, setCurrentSound] = useState(null);
  const [tempoData, setTempoData] = useState([]);

  useEffect(() => {
    getTempo();
  }, []);

  async function getTempo() {
    try {
      const response = await axios.get(baseUrl);
      const tempoData = response.data;
      setTempoData(tempoData);
      console.log(tempoData);
    } catch (error) {
      console.error('Error al obtener los datos del tempo', error);
    }
  }


  
  const playSound = (soundUrl) => {
    // Detener el sonido actual si se está reproduciendo
    if (currentSound) {
      currentSound.stop();
    }

    const sound = new Howl({ src: [soundUrl], volume: 0.3 });
    setCurrentSound(sound);
    sound.play();
  };

  const handleClick = (event,audio) => {
    const tempo = event.target.dataset.value;
    playSound(audio);
    console.log(audio)
    console.log('Image clicked');

  };

  return (
    <>
      <div className='navbar_container'>
          <NavBar />
      </div>
      <div className='image-container'>
        {tempoData.map((tempo) => (
          <figure key={tempo[0]}>
            <img
              src={tempo[2]}
              onClick={(event) => handleClick(event,tempo[3])}
              className="imgSound"
              data-value={tempo}
              alt={tempo[2]}
            />
            <figcaption className='elegant-text'>{tempo[1]}</figcaption>
          </figure>
        ))}
      </div>
    </>
  );
}
