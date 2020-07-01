import React from "react";
import { Container, Row, Col } from "shards-react";

import PageTitle from "../components/common/PageTitle";
import ControllersTable from '../components/ControllersTable'
import OutputsTable from '../components/OutputsTable'

const Dashboard = () => (
  <Container fluid className="main-content-container px-4">
    <Row noGutters className="page-header py-4">
      <PageTitle title="Dashboard" subtitle="" className="text-sm-left mb-3" />
    </Row>
    <Row>
      <Col sm="12" className="mb-4">
        <ControllersTable/>
        <OutputsTable/>
      </Col>
    </Row>
  </Container>
);

export default Dashboard;
