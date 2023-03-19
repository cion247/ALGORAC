import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import ProjectCard from "./ProjectCards";
import Particle from "../Particle";

import demo from "../../Assets/Projects/placeholder.png";


function Projects() {
  return (
    <Container fluid className="project-section">
      <Particle />
      <Container>
        <h1 className="project-heading">
          Project <strong className="purple">Works </strong>
        </h1>
        <p style={{ color: "white" }}>
          projects conducted under the support of coding club.
        </p>
        <Row style={{ justifyContent: "center", paddingBottom: "10px" }}>
          <Col md={4} className="project-card">
            <ProjectCard
              imgPath={demo}
              isBlog={false}
              title="project zero"
              description="project 0 description"
              ghLink=""
              demoLink=""
            />
          </Col>

          <Col md={4} className="project-card">
            <ProjectCard
              imgPath={demo}
              isBlog={false}
              title="project one"
              description="project one description."
              ghLink=""
              demoLink=""
            />
          </Col>

          <Col md={4} className="project-card">
            <ProjectCard
              imgPath={demo}
              isBlog={false}
              title="project two"
              description="project 2 description"
              ghLink=""
              demoLink=""
            />
          </Col>


        </Row>
      </Container>
    </Container>
  );
}

export default Projects;
