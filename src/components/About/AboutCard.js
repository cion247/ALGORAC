import React from "react";
import Card from "react-bootstrap/Card";
//import { ImPointRight } from "react-icons/im";//

function AboutCard() {
  return (
    <Card className="quote-card-view">
      <Card.Body>
        <blockquote className="blockquote mb-0">
          <p style={{ textAlign: "justify" }}>
            hello, we are from <span className="one">ICFAI University Tripura</span>
            from <span className="one">Kamalghat, Mohanpur</span>

            <br />
            <br />
            We are the official ICFAI Coding Club operated by students<br />
            we look to find new and enthusiastic faces in our clubs <br />
            we will welcome you with open arms and will help you <br /> with anything you need
          </p>


          <p style={{ color: "rgb(39 141 155)" }}>
            "I code , therefore I am."{" "}
          </p>
          <footer className="blockquote-footer">ALGORAC</footer>
        </blockquote>
      </Card.Body>
    </Card>
  );
}

export default AboutCard;
