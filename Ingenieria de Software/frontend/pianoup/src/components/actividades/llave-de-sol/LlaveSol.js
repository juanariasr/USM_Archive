import { Link } from "react-router-dom";
import { toPng } from "html-to-image";
import React, { useCallback, useRef } from "react";
import { Stage, Layer, Line } from "react-konva";
import NavBar2 from "../../barra/NavBar2";
import "./llavesol.css";

export const LlaveSol = ({ SetImagen }) => {
  const [tool, setTool] = React.useState("pen");
  const [lines, setLines] = React.useState([]);
  const isDrawing = React.useRef(false);

  const handleMouseDown = (e) => {
    isDrawing.current = true;
    const pos = e.target.getStage().getPointerPosition();
    setLines([...lines, { tool, points: [pos.x, pos.y] }]);
  };

  const handleMouseMove = (e) => {
    // no drawing - skipping
    if (!isDrawing.current) {
      return;
    }
    const stage = e.target.getStage();
    const point = stage.getPointerPosition();
    let lastLine = lines[lines.length - 1];
    // add point
    lastLine.points = lastLine.points.concat([point.x, point.y]);

    // replace last
    lines.splice(lines.length - 1, 1, lastLine);
    setLines(lines.concat());
  };

  const handleMouseUp = () => {
    isDrawing.current = false;
  };

  ///////

  const ref = useRef(null);

  const onButtonClick = useCallback(() => {
    if (ref.current === null) {
      return;
    }

    toPng(ref.current, { cacheBust: true })
      .then((dataUrl) => {
        var img = new Image();
        img.src = dataUrl;
        //document.body.appendChild(img);
        console.log(img);
        SetImagen(img.src);
      })
      .catch((err) => {
        console.log(err);
      });
    //console.log(a);
  }, [ref, SetImagen]);

  const clickHandler = (event) => {
    handleMouseUp();
    onButtonClick();
  };

  return (
    <div className="llavesol">
      <NavBar2 />
      <div>
        <h1 class="textStyle yellow">Dibuja una Llave de Sol</h1>
      </div>
      <div className="disminuir">
        <h3>
          En esta actividad debes dibujar una Llave de Sol dentro del recuadro
          que tienes abajo, una vez que hayas dibujado presionas
          continuar para avanzar al siguiente paso.
        </h3>
        <br />
      </div>
      <div style={{ border: "1px solid grey" }}>
        <div ref={ref}>
          <Stage
            align="center"
            width={window.innerWidth - 200}
            height={450}
            onMouseDown={handleMouseDown}
            onMousemove={handleMouseMove}
            onMouseup={clickHandler}
          >
            <Layer>
              {lines.map((line, i) => (
                <Line
                  key={i}
                  points={line.points}
                  stroke="#df4b26"
                  strokeWidth={line.tool === "eraser" ? 50 : 6}
                  tension={0.5}
                  lineCap="round"
                  lineJoin="round"
                  globalCompositeOperation={
                    line.tool === "eraser" ? "destination-out" : "source-over"
                  }
                />
              ))}
            </Layer>
          </Stage>
        </div>
      </div>
      <div>
        <select
          className="caja"
          value={tool}
          onChange={(e) => {
            setTool(e.target.value);
          }}
        >
          <option value="pen">Lápiz</option>
          <option value="eraser">Borrador</option>
        </select>
      </div>
      <div className="divisor">
        <Link to="/pentagrama">
          <button className="buttonStyle">Continuar</button>
        </Link>
      </div>
    </div>
  );
};
