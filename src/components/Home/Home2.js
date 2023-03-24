import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import Img from "../../Assets/logo.svg";
import Tilt from "react-parallax-tilt";
import {
  AiFillGithub,
  AiOutlineTwitter,
  AiFillInstagram,
} from "react-icons/ai";
import { FaLinkedinIn } from "react-icons/fa";

function Home2() {
  return (
    <Container fluid className="home-about-section" id="about">
      <Container>
        <Row>
          <Col md={8} className="home-about-description">
            <h1 style={{ fontSize: "3.5em" }}>
              ABOUT US
            </h1>
            <p className="home-about-body">
              <p style={{ color: "rgb(40 142 156)" }}>
                "Alone we can do so little, together we can do so much."{" "}
              </p>
              <strong className="one">name</strong> name
              <br />
              <br />name
              <i>
                <b> name </b>
              </i> name
              <br />
              <br />
              name &nbsp;
              &nbsp;
              <i>
                <b>name.</b>
              </i>
            </p>
          </Col>
          <Col md={4} className="UniLogo">
            <Tilt>
              <img src={Img} className="img-fluid" alt="icfailogo" />
            </Tilt>
          </Col>
        </Row>
        <Row>
          <Col md={12} className="home-about-social">
            <h1>FIND US ON</h1>
            <p>
              Feel free to connect with name
            </p>
            <ul className="home-about-social-links">
              <li className="social-icons">
                <a
                  href=""
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour  home-social-icons"
                >
                  <AiFillGithub />
                </a>
              </li>
              <li className="social-icons">
                <a
                  href=""
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour  home-social-icons"
                >
                  <AiOutlineTwitter />
                </a>
              </li>
              <li className="social-icons">
                <a
                  href=""
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour  home-social-icons"
                >
                  <FaLinkedinIn />
                </a>
              </li>
              <li className="social-icons">
                <a
                  href=""
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour home-social-icons"
                >
                  <AiFillInstagram />
                </a>
              </li>
            </ul>
          </Col>
        </Row>
      </Container>
    </Container>
  );
}
export default Home2;
