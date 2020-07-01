import React from "react";
import { Card, CardBody } from "shards-react";

const ControllersTable = () => {
  return (
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
  );
};

export default ControllersTable;
