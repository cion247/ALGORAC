import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import Img from "../../Assets/ICFAIlogo.svg";
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
              ABOUT <span className="purple"></span> US
            </h1>
            <p className="home-about-body">
              <p style={{ color: "rgb(40 142 156)" }}>
                "Alone we can do so little, together we can do so much."{" "}
              </p>
              <strong className="one">ALGORAC</strong> Coding Club is an ingrain part of ICFAI UNIVERSITY TRIPURA(IUT), a private university located at Agartala, Tripura, India.
              <br />
              <br />ALGORAC is the perfect platform for all techies who are inquisitive and diligent about tackling real life problem with the aid of programming. The club focuses on
              <i>
                <b className="purple"> Competitive programming, Web Designing, App Development, </b>
              </i> and various other aspects of programming.
              <br />
              <br />
              ALGORAC strives to inculcate and foster the culture of programming and to create a healthy programming environment in the campus. It aims to create an environment which proliferate quantity and quality of programmers irrespective of their respective engineering discipline. &nbsp;
              &nbsp;
              <i>
                <b className="purple">ALGORAC believes in coding the problems away.</b>
              </i>
            </p>
          </Col>
          <Col md={4} className="UniLogo">
            <Tilt>
              <img src={Img} className="img-fluid" alt="avatar" />
            </Tilt>
          </Col>
        </Row>
        <Row>
          <Col md={12} className="home-about-social">
            <h1>FIND US ON</h1>
            <p>
              Feel free to <span className="purple">connect </span>with ALGORAC
            </p>
            <ul className="home-about-social-links">
              <li className="social-icons">
                <a
                  href="https://github.com/soumyajit4419"
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour  home-social-icons"
                >
                  <AiFillGithub />
                </a>
              </li>
              <li className="social-icons">
                <a
                  href="https://twitter.com/Soumyajit4419"
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour  home-social-icons"
                >
                  <AiOutlineTwitter />
                </a>
              </li>
              <li className="social-icons">
                <a
                  href="https://www.linkedin.com/in/soumyajit4419/"
                  target="_blank"
                  rel="noreferrer"
                  className="icon-colour  home-social-icons"
                >
                  <FaLinkedinIn />
                </a>
              </li>
              <li className="social-icons">
                <a
                  href="https://www.instagram.com/soumyajit4419"
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
