import React, { useState, useEffect } from 'react';
import Card from './Card';
import NavBar from '../../barra/NavBar';
import './Card.css';
import StopWatch from './StopWatch'
import { useNavigate } from 'react-router-dom';

const Memorice = ({ imagesSelected }) => {

  const [cards, setCards] = useState([]);
  const [firstCard, setFirstCard] = useState({});
  const [secondCard, setSecondCard] = useState({});

  const [unflippedCards, setUnflippedCards] = useState([]);
  const [unAllflippedCards, setUnAllflippedCards] = useState(0);
  const [disabledCards, setDisabledCards] = useState([]);
  const [imgs, setImgs] = useState([]);
  const [total, setTotal] = useState(0);
  const shuffleArray = (array) => {
    for (let i = array.length - 1; i > 0; i--) {
      let j = Math.floor(Math.random() * (i + 1));
      let temp = array[i];
      array[i] = array[j];
      array[j] = temp;
    }
  }
  
  useEffect(()=>{
    localStorage.setItem('imagesSelected', imagesSelected)
  },[imagesSelected]);

  useEffect(() => {


    shuffleArray(imagesSelected);
    setCards(imagesSelected);

  }, [])

  useEffect(() => {
    checkForMatch();
  }, [secondCard]);

  const flipCard = (name, number) => {
    if (firstCard.name === name && firstCard.number === number) {
      return 0;
    }
    if (!firstCard.name) {
      setFirstCard({ name, number });
    }
    else if (!secondCard.name) {
      setSecondCard({ name, number });
    }
    return 1;
  }

  const checkForMatch = () => {
    if (firstCard.name && secondCard.name) {
      const match = firstCard.name === secondCard.name;
      match ? disableCards() : unflipCards();
    }
  }

  const disableCards = () => {
    setDisabledCards([firstCard.number, secondCard.number]);
    setTotal(total+1);
    resetCards();
  };

  const unflipCards = () => {
    setUnflippedCards([firstCard.number, secondCard.number]);
    resetCards();
  };

  const resetCards = () => {
    setFirstCard({});
    setSecondCard({});
  }
  const navigate = useNavigate();

  const routeVolver = () => {
    navigate('/memorice');

  }

  const reiniciarMemorice= () =>{
    setUnAllflippedCards(unAllflippedCards + 1)  
    setTimeout(() => shuffleArray(imagesSelected), 100);
    setTimeout(() => setCards(imagesSelected), 100);
    setTotal(0);

  }
  return (
    <>
    <div className='app'>
      <NavBar/>
      <div className='app-div-btn'>
        <ul>
          <li>
            <button className='app-div-btn-volver' onClick={routeVolver}>Volver</button>

          </li>
          <li>
            <button className='app-div-btn-volver' onClick={reiniciarMemorice}>Reinciar</button>

          </li>
          <li>
            <StopWatch reset={unAllflippedCards} total={total}/>
          </li>
        </ul>
      </div>

      <div className='cards-container' id='card_cont'>
        {
          cards.map((card, index) => (
            <Card
              name={card.nota}
              number={index}
              frontFace={card.src}
              flipCard={flipCard}
              unflippedCards={unflippedCards}
              disabledCards={disabledCards}
              unAllflippedCards={unAllflippedCards}
            />
          ))
        }
      </div>
    </div>

    </>
  );
}

export default Memorice;
