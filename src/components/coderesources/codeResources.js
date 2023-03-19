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
          here are some <strong className="purple">learning resources </strong>

        </h2>
        <h2 className="project-sub-heading">
          choose an ideal Road Map and follow it until you reach your <strong>goal</strong>
        </h2>

        <Techstack />
        <Techstack />
        <Techstack />

      </Container>
    </Container>
  );
}

export default codeResources;