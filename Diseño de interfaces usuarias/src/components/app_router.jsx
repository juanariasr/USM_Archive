import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import HomePage from '../pages/home'
import Versiones from '../pages/v_anteriores'
import Mindfull from '../pages/mindfullmotion'
import CuisineAR from '../pages/cuisinear'
import Readdy from '../pages/readdy'
import FeriaOld from '../pages/feria_old'
import Activate from '../pages/activate'
import JunoApp from '../pages/junoapp'
import OnStage from '../pages/onstage'
import FigmaForm from '../pages/figmaform'

const AppRouter = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<HomePage />} />
        <Route path='/v_anteriores' element={<Versiones />} />
        <Route path='/feria_old' element={<FeriaOld />} />
        <Route path='/mindfullmotion' element={<Mindfull/>} />
        <Route path='/cuisinear' element={<CuisineAR/>} />
        <Route path='/readdy' element={<Readdy/>} />
        <Route path='/activate' element={<Activate/>} />
        <Route path='/junoapp' element={<JunoApp/>} />
        <Route path='/onstage' element={<OnStage/>} />
        <Route path='/figmaform' element={<FigmaForm/>} />
      </Routes>
    </BrowserRouter>
  )
}

export default AppRouter
