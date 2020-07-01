import React, { useEffect } from "react";
import { connect } from "react-redux";
import { Card, CardBody } from "shards-react";
import { RootState } from "../store/reducers";
import { getPidControllers } from "../store/pid_controller/actions";
import { Dispatch } from "redux";

const ControllersTable = ({ getPidControllers, controllers, isLoading }) => {
  useEffect(() => {
    getPidControllers();
    const timer = setInterval(getPidControllers, 5000);
    return () => clearTimeout(timer);
  }, [getPidControllers]);
  return (
    <React.Fragment>
      <Card small className="mb-4">
        <CardBody className="p-0 pb-3">
          <table className="table mb-0">
            <thead className="bg-light">
              <tr>
                <th scope="col" className="border-0">
                  Controller
                </th>
                <th scope="col" className="border-0">
                  Mode
                </th>
                <th scope="col" className="border-0">
                  Measure
                </th>
                <th scope="col" className="border-0">
                  SP
                </th>
                <th scope="col" className="border-0">
                  Out (%)
                </th>
              </tr>
            </thead>
            <tbody>
              {controllers
                ? controllers.map((controller) => (
                    <tr key={controller.id}>
                      <td>{controller.name}</td>
                      <td>{controller.mode}</td>
                      <td>
                        {controller.inputPort || "N/A"}:{" "}
                        {controller.reading || "N/A"} {controller.unit}
                      </td>
                      <td>
                        {controller.setPoint} {controller.unit}
                      </td>
                      <td>
                        {controller.outputs.map((output, index) => (
                          <p key={index}>
                            {output.port}: {output.value * 100}%
                            {controller.outputs.length > 1 ? " / " : null}
                          </p>
                        ))}
                      </td>
                    </tr>
                  ))
                : null}
            </tbody>
          </table>
        </CardBody>
      </Card>
      <Card small className="mb-4">
        <CardBody className="p-0 pb-3">
          <table className="table mb-0">
            <thead className="bg-light">
              <tr>
                <th scope="col" className="border-0">
                  Controller
                </th>
                <th scope="col" className="border-0">
                  Mode
                </th>
                <th scope="col" className="border-0">
                  Measure
                </th>
                <th scope="col" className="border-0">
                  SP
                </th>
                <th scope="col" className="border-0">
                  Out (%)
                </th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>TIC 101</td>
                <td>Master</td>
                <td>TI101 (20.0 C)</td>
                <td>23.0 C</td>
                <td>TCV101A (25%) / TCV101B (25%)</td>
              </tr>
              <tr>
                <td>GIC 101</td>
                <td>Auto</td>
                <td>GI101 (12.000 PPM)</td>
                <td>15.000 PPM</td>
                <td>GCV101 (50%)</td>
              </tr>
              <tr>
                <td>HIC 101</td>
                <td>Master</td>
                <td>HI101 (22.2%)</td>
                <td>25%</td>
                <td>HCV101 (80%)</td>
              </tr>
            </tbody>
          </table>
        </CardBody>
      </Card>
    </React.Fragment>
  );
};
const mapStateToProps = (state: RootState) => ({
  controllers: state.pidController.controllers,
  isLoading: state.pidController.isLoading,
});

const mapDispatchToProps = (dispatch: Dispatch) => ({
  getPidControllers: getPidControllers(dispatch),
});

const connector = connect(mapStateToProps, mapDispatchToProps);

export default connector(ControllersTable);
