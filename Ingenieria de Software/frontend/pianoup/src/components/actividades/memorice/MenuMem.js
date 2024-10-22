import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from "axios";
import NavBar from '../../barra/NavBar';
import './Card.css';

const baseURL = "http://localhost:8000/memorice";

const MenuMem = ({ setImagesSelected }) => {

    const [images, setImages] = useState([]);
    const [count, setCount] = useState(0);
    //const [imagesSelected, setImagesSelected] = useState([]);

    var arrImgBd = [];

    const navigate = useNavigate();
    useEffect(() => {

        const loadImg = async () => {

            const response = await axios.get(baseURL);

            response.data.forEach((imgBD, index) => {
                const arr1 = [{
                    src1: imgBD[2],
                    src2: imgBD[3],
                    nota: imgBD[1]
                }]
                arrImgBd = [...arrImgBd, ...arr1];
                setImages(arrImgBd)
            })
        }
        loadImg();

    }, [])
    const handleSubmit = event => {
        event.preventDefault();
        var arrImgBd = [];
        if (count < 6) {
            alert('Seleccione 6 parejas')
        } else {
            for (var i = 0; i < images.length; i++) {
                if (event.target[i].checked === true) {
                    const arr1 = [{
                        //src: './images'+images[event.target[i].value].src1.slice(1),
                        src: images[event.target[i].value].src1,
                        nota: images[event.target[i].value].nota
                    }]
                    const arr2 = [{
                        src: images[event.target[i].value].src2,
                        //src: './images'+images[event.target[i].value].src2.slice(1),
                        nota: images[event.target[i].value].nota
                    }]
                    const arrMerg = [...arr1, ...arr2];
                    arrImgBd = [...arrImgBd, ...arrMerg];
                    setImagesSelected(arrImgBd)
                }
            }
            navigate('/memoriceGame');
        }
    }

    const handleOnChange = (e) => {

        const { checked, type } = e.target;
        if (checked === true) {
            const aux = count + 1
            if (aux > 6) {
                e.target.checked = false;
                alert('Solo puede seleccionar 6 parejas')
            } else {
                setCount(aux)
            }
        } else {

            const aux = count - 1
            setCount(aux)
            console.log(count)
            console.log(aux)
        }



    };

    return (
        <div className='app'>
            <NavBar/>
            <div className='option-memorice-head'>
                <h3>Seleccione las 6 parejas</h3>
                <div className='option-memorice'>
                    <form onSubmit={handleSubmit}>
                        {
                            images.map((card, index) => (
                                <div>
                                    <input
                                        type="checkbox"
                                        id={index}
                                        name={card.nota}
                                        value={index}
                                        onChange={e => handleOnChange(e)}
                                    ></input>
                                    <label className='lblImg' for={index}>
                                        <img className="imgBd" src={card.src1}></img>
                                        <img className="imgBd" src={card.src2}></img>
                                    </label>
                                </div>
                            ))
                        }
                        <input className="btnJugar" type="submit" value="Jugar"></input>
                    </form>
                </div>

            </div>
        </div>

    );
}

export default MenuMem;
