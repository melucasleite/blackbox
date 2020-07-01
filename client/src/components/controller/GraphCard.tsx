import React, { useEffect, useState } from "react";
import { Card, CardBody, Row, Col } from "shards-react";

import PidGraph from "./PidGraph";
import { fetchPidGraph } from "../../api/api";
import FrequencySelector from "./FrequencySelector";
import Loading from "../common/Loading";

const GraphCard = ({ controller }) => {
  const [dataset, setDataset] = useState({});
  const [scale, setScale] = useState(5);
  const [isLoading, setIsLoading] = useState(true);
  const refreshFrequency = 3000;

  useEffect(() => {
    setIsLoading(true);
    const loadGraph = async () => {
      const dataset = await fetchPidGraph(controller.id, scale);
      setDataset(dataset);
      setIsLoading(false);
    };
    loadGraph();
    const timer = setInterval(loadGraph, refreshFrequency);
    return () => clearTimeout(timer);
  }, [controller.id, scale]);

  return (
    <Card small className="h-100">
      {isLoading ? (
        <Loading />
      ) : (
        <CardBody>
          <Row className="border-bottom py-2 bg-light">
            <Col sm="6" className="col d-flex mb-2 mb-sm-0">
              <FrequencySelector active={scale} setActive={setScale} />
            </Col>
          </Row>
          <PidGraph dataset={dataset} />
        </CardBody>
      )}
    </Card>
  );
};

export default GraphCard;
