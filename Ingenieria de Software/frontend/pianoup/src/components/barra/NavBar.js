import React, { useState } from 'react';

import HomeIcon from '@mui/icons-material/Home';

import ArrowBackIcon from '@mui/icons-material/ArrowBack';

import AccountCircleIcon from '@mui/icons-material/AccountCircle';

import { Link, useNavigate } from 'react-router-dom';

import Login_menu from './Login_menu';

import './navbar.css';


function NavBar({ menu = 0}){

    let navigate = useNavigate();

    
    const [open, setOpen] = useState(false);


    return(

        <div className='navbar'>

            <ul className='navbar_buttons'>

                {   

                    menu === 0

                    ? 

                    (

                        <>

                            <li className='navbar_left_item'>

                                <Link onClick={() => navigate(-1)}>

                                    <ArrowBackIcon sx={{ fontSize: "10vh", color: "white" }} />

                                </Link>

                            </li>
                            <li className='navbar_left_item'>

                                <Link to="/home">

                                    <HomeIcon sx={{ fontSize: "10vh", color: "white" }} />

                                </Link>

                            </li>

                        </>

                    )

                    :

                    (

                        <>

                            <li className='navbar_left_item'>

                                <Link to='/home'>

                                    <img  className = "navbar_logo"src='logo_blanco.png'/>

                                </Link>

                            </li>

                        </>

                    )

                }   

                <li className='navbar_right_item'>

                    <Link>

                        <AccountCircleIcon  sx={{ fontSize: "10vh", color: "white" }} onClick={() => {setOpen(!open)}}/>

                        {

                            open && <Login_menu />

                        }

                    </Link>

                </li>

            </ul>

        </div>

    );

}

export default NavBar;
