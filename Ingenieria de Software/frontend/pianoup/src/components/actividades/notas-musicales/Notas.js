import * as React from "react";
import { Link } from "react-router-dom"
import DnD from "./DnD";
import NavBar from "../../barra/NavBar";


export default function Notas() {
  
return (
    <>
      <div className="navbar_container">
        <NavBar />
      </div>
      <h1 style={{textAlign: 'center', padding: '30px 0 80px 0'}}>

        ¡Arrastra las notas musicales al pentagrama para componer tu canción!
      </h1>
      <DnD />
    </>
)
};
