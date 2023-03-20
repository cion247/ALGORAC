import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import Particle from "../Particle";
import Techstack from "./Techstack";


function codeResources() {
  return (
    <Container fluid className="CodeResources">
      <Particle />
      <Container>
        <Row style={{ justifyContent: "center", padding: "50px" }}> <Col md={5} className="" /></Row>
        {/*top padding */}
        <h2 className="project-heading">
          here are some <strong className="purple">learning resources </strong> </h2>

            <h1 style={{ fontSize: "2.1em", paddingBottom: "20px" }}>
              lorem ipsum frfsfsfsrfsrfr<strong className="one"></strong>
              get ready<strong className="one">I'M</strong>
            </h1>

          

          <Col md={5} className="" >

          </Col>
        
        <h1 className="project-heading">
          rfrdghfh <strong className="purple">Skillset </strong>
        </h1>

        <Techstack />
        <Techstack />
        <Techstack />

      </Container>
    </Container>
  );
}

export default codeResources;