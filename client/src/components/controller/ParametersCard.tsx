import React, { useCallback, useEffect, useState } from "react";
import { Card, CardBody, CardHeader } from "shards-react";
import ParametersForm from "./ParametersForm";
import {
  fetchControllerParameters,
  updateControllerParameters,
} from "../../api/api";
import swal from "sweetalert";
import Loading from "../common/Loading";

const ParametersCard = ({ controller }) => {
  const [controllerParameters, setControllerParameters] = useState({});
  const [isLoading, setIsLoading] = useState(true);

  const handleSubmit = async (input) => {
    await updateControllerParameters(controller.id, input);
    await swal("Ok", "Parameters updated.", "success");
    await fetchData();
  };

  const fetchData = useCallback(async () => {
    const parameters = await fetchControllerParameters(controller.id);
    setControllerParameters(parameters);
    setIsLoading(false);
  }, [controller.id]);

  useEffect(() => {
    setIsLoading(true);
    fetchData();
  }, [fetchData]);
  return (
    <Card small className="mb-4">
      <CardHeader className="border-bottom">
        <h6 className="">Controller parameters</h6>
      </CardHeader>
      <CardBody className="pb-3">
        {isLoading ? (
          <Loading />
        ) : (
          <ParametersForm
            parameters={controllerParameters}
            handleSubmit={handleSubmit}
          />
        )}
      </CardBody>
    </Card>
  );
};

export default ParametersCard;
