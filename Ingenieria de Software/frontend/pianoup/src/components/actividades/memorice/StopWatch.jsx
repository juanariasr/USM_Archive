import React, { useState } from "react";
import "./StopWatch.css";
import Timer from "./Timer";
  
function StopWatch({reset,total}) {
  const [isActive, setIsActive] = useState(true);
  const [isPaused, setIsPaused] = useState(false);
  const [time, setTime] = useState(0);
  
  React.useEffect(() => {
    let interval = null;
  
    if (isActive && isPaused === false) {
      interval = setInterval(() => {
        setTime((time) => time + 10);
      }, 10);
    } else {
      clearInterval(interval);
    }
    return () => {
      clearInterval(interval);
    };
  }, [isActive, isPaused]);
  
  React.useEffect(()=>{
    setTime(0);
    setIsPaused(false)
  },[reset])

  React.useEffect(()=>{
    if(total === 6){
        setIsPaused(true)
    }
  },[total])

  
  return (
    <div className="stop-watch">
      <Timer time={time} />
    </div>
  );
}
  
export default StopWatch;