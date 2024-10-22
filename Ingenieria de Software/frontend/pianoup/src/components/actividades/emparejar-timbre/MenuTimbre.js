import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from "axios";
import NavBar from '../../barra/NavBar';
import './MenuTimbre.css';


const baseURL = "http://localhost:8000/emparejar";

const MenuTimbre = ({ setTimbreSelected }) => {

    const [images, setImages] = useState([]);

    var arrImgBd = [];

    const navigate = useNavigate();

    useEffect(() => {
        const loadImg = async () => {

            const response = await axios.get(baseURL);

            response.data.forEach((imgBD, index) => {
                if (imgBD[1] == "Timbre"){
                    const arr1 = [{
                        id: imgBD[0],
                        imagen: imgBD[2],
                        audio: imgBD[3],
                        tipo: imgBD[4]
                    }]
                    arrImgBd = [...arrImgBd, ...arr1];
                    setImages(arrImgBd)
                }
            })
        }
        loadImg();

    }, []);

    const handleSubmit = event => {
        event.preventDefault();
        var arrImgBd = [];
        for (var i = 0; i < images.length; i++) {
            if (event.target[i].checked === true) {
                const arr1 = [{
                    id: images[event.target[i].value].id,
                    list: 1,
                    imagen: images[event.target[i].value].imagen,
                    audio: images[event.target[i].value].audio,
                    tipo: images[event.target[i].value].tipo
                }]
                arrImgBd = [...arrImgBd, ...arr1];
                setTimbreSelected(arrImgBd);
            }
            }
        navigate('/emparejar-timbre');
    };

    const handleOnChange = (e) => {
        const { checked, type } = e.target;
    };

//Crear imagen nueva
    function extractFilename(path) {
        if (path.substr(0, 12) == "C:\\fakepath\\")
            return path.substr(12); // modern browser
        var x;
        x = path.lastIndexOf('/');
        if (x >= 0) // Unix-based path
            return path.substr(x+1);
        x = path.lastIndexOf('\\');
        if (x >= 0) // Windows-based path
            return path.substr(x+1);
        return path; // just the filename
    }
    function updateFilename(path) {
        var name = extractFilename(path);
        console.log(name);
        document.getElementById('imagen').textContent = name;
    }
    
    const [imagen, setImagen] = useState("");
    const [audio, setAudio] = useState("");
    const [tipo, setTipo] = useState("");

    const addImage = (e) => {
        
        e.preventDefault();
        const data = {
            actividad: 'Timbre',
            imagen: imagen,
            audio: audio,
            tipo: tipo
        }
        console.log(data);
        //POST DATA
        axios.post(baseURL, data)
        .then(function(response) {
            window.location.reload();
        }).catch(function (error) {
            console.log(error);
        });
    }

    return (
        <div className='app'>
            <NavBar/>
            <div className='head-menu-emparejar'>
                <h3>Seleccione las imagenes que desee utilizar</h3>
                
                <div className='column-menu'>
                    <form onSubmit={ handleSubmit }>
                        {
                            images.map((card, index) => (
                                <label className='block-image-emparejar' for={index}>
                                        <div>
                                            <img className="img-emparejar" src={card.imagen}></img>
                                            <audio volume='0.1' controls type="audio/mpeg" src={card.audio}></audio>
                                        </div>
                                    <input
                                        type="checkbox"
                                        id={index}
                                        name={card.imagen}
                                        value={index}
                                        onChange={e => handleOnChange(e)}
                                    ></input>
                                </label>
                            ))
                        }
                        <input className="button-continue" type="submit" value="Continuar"></input>
                    </form>
                </div>

                <div>
                    <div>
                        <div>
                            <div>
                                <h4>Crear nueva imagen</h4>
                            </div>
                            <form method="post" enctype="multipart/form-data" onSubmit={addImage}>
                                <div>
                                    <label>Elige una imagen: </label>
                                    <input
                                    type="file"
                                    id="emp-imagen"
                                    name="imagen"
                                    accept=".jpg, .jpeg, .png"
                                    value={imagen}
                                    onChange={(e) => setImagen(e.target.value)}
                                    />
                                </div>
                                <div>
                                    <label>Elige un audio: </label>
                                    <input
                                    type="file"
                                    id="emp-audio"
                                    name="audio"
                                    accept="audio/*"
                                    value={audio}
                                    onChange={(e) => setAudio(e.target.value)}
                                    />
                                </div>
                                <div>
                                    <label>Selecciona un tipo</label>
                                    <input list="tipos" id="myTipo" name="myTipo" value={tipo} onChange={(e) => setTipo(e.target.value)}/>
                                    <datalist id="tipos">
                                    <option value="Viento"></option>
                                    <option value="Percusion"></option>
                                    <option value="Cuerda"></option>
                                    </datalist>
                                </div>
                                <div>
                                    <button type='submit'>Submit</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default MenuTimbre;
