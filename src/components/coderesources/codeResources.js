import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import Particle from "../Particle";
//import Techstack from "./Techstack";
import laptopImg from "../../Assets/about.png";


function codeResources() {
  return (
    <Container fluid className="CodeResources">
      <Particle />
      <Container>
        <Row style={{ justifyContent: "center", padding: "10px" }}>
          <Col md={7} style={{ justifyContent: "center", paddingTop: "30px", paddingBottom: "50px", }}>

            <h1 style={{ fontSize: "2.1em", paddingBottom: "20px" }}>
              lorem ipsum frfsfsfsrfsrfr<strong className="one"></strong>
            </h1>

          </Col>

          <Col md={5} className="" >

          </Col>
        </Row>
        <h1 className="project-heading">
          rfrdghfh <strong className="purple">Skillset </strong>
        </h1>

        {/* <Techstack /> */}

      </Container>
    </Container>
  );
}

export default codeResources;