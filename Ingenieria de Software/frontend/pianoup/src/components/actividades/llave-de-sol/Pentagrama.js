import React from "react";
import { Link } from "react-router-dom";
import { Stage, Layer, Image } from "react-konva";
import useImage from "use-image";
import NavBar from "../../barra/NavBar";
import "./pentagrama.css";
import "./llavesol.css";
import background from "./images/pentagrama.png";

const URLImage = ({ image }) => {
  const [img] = useImage(image.src);
  return (
    <Image
      image={img}
      x={image.x}
      y={image.y}
      // I will use offset to set origin to the center of the image
      offsetX={img ? img.width / 2 : 0}
      offsetY={img ? img.height / 2 : 0}
    />
  );
};

export const Pentagrama = ({ imagen }) => {
  const dragUrl = React.useRef(null);
  const stageRef = React.useRef(null);
  const [images, setImages] = React.useState([]);
  var sectionStyle = {
    backgroundImage: `url(${background})`,
    width: `${window.innerWidth - 200}px`,
    height: "500px",
  };
  return (
    <div className="llavesol">
      <div className="navbar_container">
        <NavBar />
      </div>
      <br />
      <div>
        <h1 class="textStyle yellow">Arrastra la Llave de Sol al pentagrama</h1>
      </div>
      <div className="disminuir">
        <h3>
          Para concluir la actividad arrastra la Llave de Sol dibujada dentro
          del pentagrama.
        </h3>
        <br />
      </div>
      <br />
      <br />
      <img
        alt="llave_sol"
        src={imagen}
        draggable="true"
        onDragStart={(e) => {
          dragUrl.current = e.target.src;
        }}
      />
      <div
        className="bg"
        style={sectionStyle}
        onDrop={(e) => {
          e.preventDefault();
          // register event position
          stageRef.current.setPointersPositions(e);
          // add image
          setImages(
            images.concat([
              {
                ...stageRef.current.getPointerPosition(),
                src: dragUrl.current,
              },
            ])
          );
        }}
        onDragOver={(e) => e.preventDefault()}
      >
        <Stage width={window.innerWidth} height={500} ref={stageRef}>
          <Layer>
            {images.map((image) => {
              return <URLImage image={image} />;
            })}
          </Layer>
        </Stage>
      </div>
      <div>
        <Link to="/llavesol">
          <button className="buttonStyle">Volver</button>
        </Link>
      </div>
    </div>
  );
};
