import React from "react";
import { Container, Row, Col } from "shards-react";

import PageTitle from "../components/common/PageTitle";
import GraphCard from "../components/controller/GraphCard";
import ParametersCard from "../components/controller/ParametersCard";

const Controller = (props) => {
  const { id } = props.match.params;
  const controller = {
    name: id,
    id: id,
  };
  return (
    <Container fluid className="main-content-container px-4">
      <Row noGutters className="page-header py-4">
        <PageTitle
          title={controller.name}
          subtitle="Controller"
          className="text-sm-left mb-3"
        />
      </Row>
      <Row>
        <Col sm="12" className="mb-4">
          <GraphCard controller={controller} />
        </Col>
        <Col sm="12">
          <ParametersCard controller={controller} />
        </Col>
      </Row>
    </Container>
  );
};

export default Controller;
