import React from "https://cdn.skypack.dev/react@17.0.1";
import { useState } from 'react';
import './EmparejarIntensidad.css';
import NavBar from "../../barra/NavBar";
import { useNavigate } from 'react-router-dom';

const baseUrl = 'http://localhost:8000/';

export const EmparejarIntensidad = ( {intensidadSelected} ) => {
    
    const [tasks, setTasks] = useState(intensidadSelected);

    const navigate = useNavigate();

    function changeTipo() {
            for (var i in tasks) {
                if (tasks[i].tipo == "Suave") {
                        tasks[i].tipo = 2;
                    }
                if (tasks[i].tipo == "Fuerte") {
                        tasks[i].tipo = 3;
                    }
                }
        }

    const getList = (list) => {
        changeTipo();
        return tasks.filter(item => item.list === list);
    }

    const startDrag = (evt, item) => {
        evt.dataTransfer.setData('itemID', item.id);
    }

    const draggingOver = (evt) => {
        evt.preventDefault();
    }

    const onDrop = (evt, list) => {
        const itemID = evt.dataTransfer.getData('itemID');
        const item = tasks.find(item => item.id == itemID);
        item.list = list;

        const newState = tasks.map(task => {
            if(task.id === itemID) return item;
            return task
        })

        setTasks(newState);
    }

    const makeProgress = (tasks) => {
        var correct = 0;
        const total = tasks.length;
        for (var n = 0; n<tasks.length; n++){
            if (tasks[n].tipo === tasks[n].list) {
                correct += 1;
            }
        }
        var porcentaje = Math.round(parseFloat(correct/total)*100)
        alert("Respuestas correctas: "+ correct + "\nPorcentaje correcto: " + porcentaje +"%");
    }
        

    const axios = require('axios');

    const addResumen = (e) => {
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today.getFullYear();

        today = dd + '/' + mm + '/' + yyyy;

        var correct = 0;
        const total = tasks.length;
        for (var n = 0; n<tasks.length; n++){
            if (tasks[n].tipo === tasks[n].list) {
                correct += 1;
            }
        }
        
        e.preventDefault();
        const data = {
            actividad: 'Intensidad',
            aciertos: String(correct),
            fallos: String(total - correct),
            fecha: today
        }
        console.log(data);
        //POST DATA
        axios.post(baseUrl + 'resumenes', data)
        .then(function(response) {
            navigate('/menu-intensidad');
        }).catch(function (error) {
            console.log(error);
        });
    }


    return (
        <>
            <div className='navbar_container'>
                <NavBar />
            </div>
            <h1>
                Sonidos según su intensidad musical &nbsp;
            </h1>
            <p>
                Reproduce el audio de las imágenes y deslízalas a la columna que les corresponda según su intensidad, 
                estos pueden ser sonidos suaves o fuertes. ¡Mucho éxito!
            </p>
            <br/>
            <div className="backend-button">
                <div>
                    <button
                        className="check-button"
                        onClick={() => makeProgress(tasks)}
                        >
                        Revisa tus respuestas
                    </button>
                </div>
                <div>
                    <button
                        className="save-button"
                        onClick={addResumen}
                        >
                        Guarda tu resultado
                    </button>
                </div>
            </div>

            <div className="drag-and-drop">
            <div className="column column--1">
                    <h3>
                        Imágenes disponibles
                    </h3>
                    <div className='dd-zone' droppable="true" onDragOver={(evt => draggingOver(evt))} onDrop={(evt => onDrop(evt, 1))}>
                        {getList(1).map(item => (
                            <div className='dd-element' 
                            key={item.id} draggable onDragStart={(evt) => startDrag(evt, item)}>

                                <img className='img' src={item.imagen} alt={item.imagen}></img>
                                <p>Escucha su sonido (precaución volumen)</p>
                                <audio volume='0.1' controls type="audio/mpeg" src={item.audio}>
                                </audio>

                            </div>
                        ))}
                    </div>
                </div>


                <div className="column column--2">
                    <h3>
                        Sonidos suaves
                    </h3>
                    <div className='dd-zone' droppable="true" onDragOver={(evt => draggingOver(evt))} onDrop={(evt => onDrop(evt, 2))}>
                        {getList(2).map(item => (
                            <div className='dd-element' 
                            key={item.id} draggable onDragStart={(evt) => startDrag(evt, item)}>
                                <img className='img' src={item.imagen} alt={item.imagen}></img>
                                <p>Escucha su sonido (precaución volumen)</p>
                                <audio volume='0.1' controls type="audio/mpeg" src={item.audio} >
                                </audio>
                            </div>
                        ))}
                    </div>
                </div>

                <div className="column column--3">
                    <h3>
                        Sonidos fuertes
                    </h3>
                    <div className='dd-zone' droppable="true" onDragOver={(evt => draggingOver(evt))} onDrop={(evt => onDrop(evt, 3))}>
                        {getList(3).map(item => (
                            <div className='dd-element' 
                            key={item.id} draggable onDragStart={(evt) => startDrag(evt, item)}>
                                <img className='img' src={item.imagen} alt={item.imagen}></img>
                                <p>Escucha su sonido (precaución volumen)</p>
                                <audio volume='0.1' controls type="audio/mpeg" src={item.audio} >
                                </audio>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </>
    )
};
