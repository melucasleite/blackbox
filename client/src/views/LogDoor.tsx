import React from "react";
import DataGrid from "react-data-grid";
import { Container, Row, Col } from "shards-react";
import "react-data-grid/dist/react-data-grid.css";
import PageTitle from "../components/common/PageTitle";

const columns = [
  { key: "id", name: "ID" },
  { key: "title", name: "Title" },
];

const rows = [
  { id: 0, title: "Example" },
  { id: 1, title: "Demo" },
];

const LogDoor = () => {
  return (
      <Container fluid className="main-content-container px-4">
        <Row noGutters className="page-header py-4">
          <PageTitle
              title="Door"
              subtitle="LOG"
              className="text-sm-left mb-3"
          />
        </Row>
        <Row>
          <Col sm="12" className="mb-4">
            <div>
              <DataGrid columns={columns} rows={rows} />
            </div>
          </Col>
        </Row>
      </Container>
  );
};

export default LogDoor;
