import React from "react";
import { useState, useEffect} from "react";
import Button from '@mui/material/Button';
import estilos from './DnD.module.css';
import PlayCircleIcon from '@mui/icons-material/PlayCircle';
import SaveIcon from '@mui/icons-material/Save';

import axios from "axios";

import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import IconButton from '@mui/material/IconButton';
import Grid from '@mui/material/Grid';
import DeleteIcon from '@mui/icons-material/Delete';
import MusicNoteIcon from '@mui/icons-material/MusicNote';


//Audios
import Dom from './sounds/0Dom.mp3';
import Re from './sounds/1Re.mp3';
import Mi from './sounds/2Mi.mp3';
import Fa from './sounds/3Fa.mp3';
import Sol from './sounds/4Sol.mp3';
import La from './sounds/5La.mp3';
import Si from './sounds/6Si.mp3';
import Do from './sounds/7Do.mp3';
import pickup from './sounds/pickup_sfx.mp3';
import drop from './sounds/drop_sfx.mp3';

//Imágenes notas
// import Espacio from './images/espacio.png';
import DomImg from './images/0Dom.png';
import ReImg from './images/1Re.png';
import MiImg from './images/2Mi.png';
import FaImg from './images/3Fa.png';
import SolImg from './images/4Sol.png';
import LaImg from './images/5La.png';
import SiImg from './images/6Si.png';
import DoImg from './images/7Do.png';

//Pentagrama
import linea from './images/linea.png';
import llave from './images/llave-sol.png';

//Recuperar cancines del usuario
const baseURL = 'http://localhost:8000/notas';

const username = sessionStorage.getItem('user');

export default function DnD() {
    const [savedSongs, setSavedSongs] = useState([]);

    const createSongList = songs => {
        for(let i=0; i<songs.length; i++){
            let notas = songs[i][2].split("");
            setSavedSongs(savedSongs => [...savedSongs, {id:songs[i][0], index:i+1, song:notas}]);
        }
    }
    
    useEffect(() => {
        getSongs();
    }, []);
    
  async function getSongs() {
    try {
      const response = await axios.get(`${baseURL}/${username}`);
      createSongList(response.data);
    } catch (error) {
      console.error('Error al obtener la lista de canciones', error);
    }
  }

  async function saveSong(e) {
    e.preventDefault();
    if(comp.length>=1){
        try {
            const resp = await axios.post(baseURL, {username:username, song:comp.join('')});
            console.log('Respuesta post: ', resp.data);
            window.location.reload();
        } catch (err) {
            console.error('Error al guardar la cancion', err);
        }
    } else {
        alert('Tu pentagrama está vacío!');

    }
  }

    async function deleteSong(song_id) {
        try {
            const resp = await axios.delete(`${baseURL}/${song_id}`)
            console.log('Respuesta post: ', resp);
            window.location.reload();
        } catch (err){
            console.error('Error al borrar la cancion', err);
        }
    }

    //Audios notas
    function playDom(){
        new Audio(Dom).play();
    }
    function playRe(){
        new Audio(Re).play();
    }
    function playMi(){
        new Audio(Mi).play();
    }
    function playFa(){
        new Audio(Fa).play();
    }
    function playSol(){
        new Audio(Sol).play();
    }
    function playLa(){
        new Audio(La).play();
    }
    function playSi(){
        new Audio(Si).play();
    }
    function playDo(){
        new Audio(Do).play();
    }
    function playPickup(){
        new Audio(pickup).play();
    }
    function playDrop(){
        new Audio(drop).play();
    }

    //Composición
    const [comp, setComp] = useState([]);

    //Filas pentagrama
    const [notasDom, setNotasDom] = useState([]);
    const [notasRe, setNotasRe] = useState([]);
    const [notasMi, setNotasMi] = useState([]);
    const [notasFa, setNotasFa] = useState([]);
    const [notasSol, setNotasSol] = useState([]);
    const [notasLa, setNotasLa] = useState([]);
    const [notasSi, setNotasSi] = useState([]);
    const [notasDo, setNotasDo] = useState([]);


    const estados = [
        [notasDom, setNotasDom],
        [notasRe, setNotasRe],
        [notasMi, setNotasMi],
        [notasFa, setNotasFa],
        [notasSol, setNotasSol],
        [notasLa, setNotasLa],
        [notasSi, setNotasSi],
        [notasDo, setNotasDo],
    ]


    const blankSpace = {            
            id: 0,
            type: 0,
            title: 'Espacio',
            body: <div style={{width: '165px', height: '50%'}}/>
        }

    const notas = [
        { 
            id: 1,
            type: 1,
            title: 'Dom',
            body: <img src={DomImg} alt="Nota DO" style={{width: '50%'}} onClick={playDom}/>
        },
        { 
            id: 2,
            type: 2,
            title: 'Re',
            body: <img src={ReImg} alt="Nota RE" style={{width: '50%'}} onClick={playRe}/>
        },
        { 
            id: 3,
            type: 3,
            title: 'Mi',
            body: <img src={MiImg} alt="Nota MI" style={{width: '50%'}} onClick={playMi}/>
        },
        { 
            id: 4,
            type: 4,
            title: 'Fa',
            body: <img src={FaImg} alt="Nota FA" style={{width: '50%'}} onClick={playFa}/>
        },
        { 
            id: 5,
            type: 5,
            title: 'Sol',
            body: <img src={SolImg} alt="Nota SOL" style={{width: '50%'}} onClick={playSol}/>
        },
        { 
            id: 6,
            type: 6,
            title: 'La',
            body: <img src={LaImg} alt="Nota LA" style={{width: '50%'}} onClick={playLa}/>
        },
        { 
            id: 7,
            type: 7,
            title: 'Si',
            body: <img src={SiImg} alt="Nota SI" style={{width: '50%'}} onClick={playSi}/>
        },
        { 
            id: 8,
            type: 8,
            title: 'Do',
            body: <img src={DoImg} alt="Nota Do" style={{width: '50%'}} onClick={playDo}/>
        }]
    
    //Añade una nota "tipoNota" a su respectiva fila en el pentagrama.
    const addNota = (tipoNota) => {
        
        const lista = estados[tipoNota][0];
        const set = estados[tipoNota][1]; 


        
        if (notasDom.length <= 6){ //Limita el máximo de notas en pentagrama
            set(lista => [...lista, notas[tipoNota]]);
            setComp(comp => [...comp, tipoNota]);
            console.log('Composicion: ',comp);
    
            
            //LLenar de espacios posiciones no disponibles
            for(let i=0; i<8; i++){
                if(i!=tipoNota){
                    let listas = estados[i][0];
                    let setBlanks = estados[i][1];
                    setBlanks(listas => [...listas, blankSpace]);
                }
            }
        }
    }

    const startDrag = (evt, item) => {
        playPickup();
        evt.dataTransfer.setData('itemID', item.id);
        evt.dataTransfer.setData('itemType', item.type);
        evt.dataTransfer.setData('itemTitle', item.title);

        //Printear item drageado
        console.log(item.title);
    }

    const draggingOver = (evt) => {
        evt.preventDefault();
    }

    const onDrop = (evt, list) => {
        console.log('Composicion: ',comp);
        playDrop();
        const itemType = evt.dataTransfer.getData('itemType');
        
        if(itemType == list) 
            addNota(itemType-1);
    }

    //Vacía cada fila del pentagrama.
    const clearNotas = () => {
        for(let i=0; i<8; i++){
            estados[i][1]([]);
        }
        setComp([]);
        playDo();
    }

    //Delay en microsegundos para funciones asincronas
    const delay = ms => new Promise(res => setTimeout(res, ms));

    //Toca las notas del pentagrama
    const playComp = async () => {
        if (comp.length==0) alert('No hay notas en tu pentagrama!');
        else {
            for (let i=0; i<comp.length; i++){
                console.log(comp[i]);
                switch (parseInt(comp[i])) {
                    case 0:
                        playDom();
                        break;
                    case 1:
                        playRe();
                        break;
                    case 2:
                        playMi();
                        break;
                    case 3:
                        playFa();
                        break;
                    case 4:
                        playSol();
                        break;
                    case 5:
                        playLa();
                        break;
                    case 6:
                        playSi();
                        break;
                    case 7:
                        playDo();
                        break;
                    
                }
                await delay(750);
            }
        }
    }

    //Carga en pentagrama una composición guardada
    //https://react.dev/learn/queueing-a-series-of-state-updates  <--No puede actualizarse dos veces el mismo estado en una sola llamada, se queda con el ultimo. (arreglado)
    const loadSong = song => {
        // clearNotas();
        if(comp.length != 0){
            alert('Primero vacia tu pentagrama');
        } else {
            playDrop();
            for (let i=0; i<song.length; i++){
                
                console.log(song[i]);
                addNota(song[i]);
            }
        }
    }

    function generate(element) {
        return savedSongs.map((value) =>
            React.cloneElement(
            
                <ListItem
                secondaryAction={
                    <IconButton edge="end" aria-label="delete" onClick={() => deleteSong(value.id)}>
                    <DeleteIcon />
                    </IconButton>
                }>
                <Button variant="text" size="large" startIcon={<MusicNoteIcon />} onClick={() => loadSong(value.song)}>Canción {value.index}</Button>
                </ListItem>, {
                key: value,
            }),
        );
    }
    
    return (
        <>  
            <div style={{width:'100%', margin:'20px 0px', display:'flex', alignItems:'center', justifyContent:'space-evenly'}}>
                <Button variant="contained" color="success" size="large" startIcon={<PlayCircleIcon />} onClick={playComp}>Reproducir</Button>
                <Button variant="contained" size="large" startIcon={<SaveIcon/>} onClick={saveSong}>Guardar</Button>
                <Button variant="contained" color="error" size="large" startIcon={<DeleteIcon/>} onClick={clearNotas}>Vaciar</Button>
            </div>
            <div className={estilos.draganddrop1}>
                <img src={llave} style={{height:'575px', position: 'absolute'}}/>

                <div className={`${estilos.column2} ${estilos.column22}`}>

                    {/* Lineas vacías */}
                    <div className={estilos.ddzone2} style={{backgroundImage: `url(${linea})`, backgroundRepeat:"repeat", backgroundSize:"contain" }}/>
                    <div className={estilos.ddzone2}/>
                    <div className={estilos.ddzone2} style={{backgroundImage: `url(${linea})`, backgroundRepeat:"repeat", backgroundSize:"contain" }}/>


                    {/* Do */}
                    <div 
                    className={estilos.ddzone2}
                    droppable="true"
                    onDragOver={(evt => draggingOver(evt))} onDrop={(evt => onDrop(evt, 8))}>
                        {notasDo.map(item => (
                            <div className={estilos.ddelement2} key={item.id} draggable onDragStart={(evt) => startDrag(evt, item)}>
                                <p className={estilos.body2} style={{margin:'0'}}>{item.body}</p>
                            </div>
                        ))}
                    </div>


                    {/* Si */}
                    <div
                    className={estilos.ddzone2}
                    droppable="true"
                    onDragOver={(evt => draggingOver(evt))}
                    onDrop={(evt => onDrop(evt, 7))}
                    style={{backgroundImage: `url(${linea})`, backgroundRepeat:"repeat", backgroundSize:"contain" }}>
                        {notasSi.map(item => (
                            <div className={estilos.ddelement2} key={item.id} draggable onDragStart={(evt) => startDrag(evt, item)}>
                                <p className={estilos.body2}>{item.body}</p>
                            </div>
                        ))}
                    </div>


                    {/* La */}
                    <div className={estilos.ddzone2} droppable="true" onDragOver={(evt => draggingOver(evt))} onDrop={(evt => onDrop(evt, 6))}>
                        {notasLa.map(item => (
                            <div className={estilos.ddelement2} key={item.id} draggable onDragStart={(evt) => startDrag(evt, item)}>
                                <p className={estilos.body2}>{item.body}</p>
                            </div>
                        ))}
                    </div>


                    {/* Sol */}
                    <div
                    className={estilos.ddzone2}
                    droppable="true"
                    onDragOver={(evt => draggingOver(evt))} onDrop={(evt => onDrop(evt, 5))}
                    style={{backgroundImage: `url(${linea})`, backgroundRepeat:"repeat", backgroundSize:"contain" }}>
                        {notasSol.map(item => (
                            <div className={estilos.ddelement2} key={item.id} draggable onDragStart={(evt) => startDrag(evt, item)}>
                                <p className={estilos.body2}>{item.body}</p>
                            </div>
                        ))}
                    </div>


                    {/* Fa */}
                    <div
                    className={estilos.ddzone2}
                    droppable="true"
                    onDragOver={(evt => draggingOver(evt))}
                    onDrop={(evt => onDrop(evt, 4))}>
                        {notasFa.map(item => (
                            <div className={estilos.ddelement2} key={item.id} draggable onDragStart={(evt) => startDrag(evt, item)}>
                                <p className={estilos.body2}>{item.body}</p>
                            </div>
                        ))}
                    </div>


                    {/* Mi */}
                    <div
                    className={estilos.ddzone2}
                    droppable="true"
                    onDragOver={(evt => draggingOver(evt))} onDrop={(evt => onDrop(evt, 3))}
                    style={{backgroundImage: `url(${linea})`, backgroundRepeat:"repeat", backgroundSize:"contain" }}>
                        {notasMi.map(item => (
                            <div className={estilos.ddelement2} key={item.id} draggable onDragStart={(evt) => startDrag(evt, item)}>
                                <p className={estilos.body2}>{item.body}</p>
                            </div>
                        ))}
                    </div>


                    {/* Re */}
                    <div className={estilos.ddzone2} droppable="true" onDragOver={(evt => draggingOver(evt))} onDrop={(evt => onDrop(evt, 2))}>
                        {notasRe.map(item => (
                            <div className={estilos.ddelement2} key={item.id} draggable onDragStart={(evt) => startDrag(evt, item)}>
                                <p className={estilos.body2}>{item.body}</p>
                            </div>
                        ))}
                    </div>


                    {/* Do */}
                    <div className={estilos.ddzone2} droppable="true" onDragOver={(evt => draggingOver(evt))} onDrop={(evt => onDrop(evt, 1))}>
                        {notasDom.map(item => (
                            <div className={estilos.ddelement2} key={item.id} draggable onDragStart={(evt) => startDrag(evt, item)}>
                                <p className={estilos.body2}>{item.body}</p>
                            </div>
                        ))}
                    </div>
                </div>
                

                <div className={`${estilos.column2} ${estilos.column21}`}>
                    <h3>
                        ¡También puedes presionar las notas para escucharlas!
                    </h3>
                    <div className={estilos.ddzone2} droppable="true" onDragOver={(evt => draggingOver(evt))} style={{paddingLeft: '0'}}>
                        {notas.map(item => (
                            <div className={estilos.ddelement2} key={item.id} draggable onDragStart={(evt) => startDrag(evt, item)}>
                                <strong className={estilos.title}>{item.title}</strong>
                                <div className={estilos.body2}  >{item.body}</div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>

            <div style={{padding:'0 20% 100px 20%'}}>
                <Grid item xs={12} md={6}>
                <h3>Escucha tus canciones</h3>
                <div>
                    <List dense={0}>
                    {generate()}
                    </List>
                </div>
                </Grid>
            </div>
        </>
    )
}
