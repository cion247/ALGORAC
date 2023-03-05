import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import Particle from "../Particle";
import Aboutcard from "./AboutCard";
import laptopImg from "../../Assets/about.png";


function About() {
  return (
    <Container fluid className="about-section">
      <Particle />
      <Container>
        <Row style={{ justifyContent: "center", padding: "10px" }}>
          <Col md={7} style={{ justifyContent: "center", paddingTop: "30px", paddingBottom: "50px", }}>

            <h1 style={{ fontSize: "2.1em", paddingBottom: "20px" }}>
              MEET OUR <strong className="one">TEAM</strong>
            </h1>
            <Aboutcard />
          </Col>

          <Col md={5} className="about-img" >
            <img src={laptopImg} alt="about" className="img-fluid" />
          </Col>
        </Row>
        <h1 className="project-heading">
          Professional <strong className="purple">Skillset </strong>
        </h1>

      </Container>
    </Container>
  );
}

export default About;
