import React from "react";
const shardsReact = require('shards-react');
const { Card, CardBody } = shardsReact

const OutputsTable = () => {
  return (
    <div>
      <Card small className="mb-4">
        <CardBody className="p-0 pb-3">
          <table className="table mb-0">
            <thead className="bg-light">
              <tr>
                <th scope="col" className="border-0">
                  Output
                </th>
                <th scope="col" className="border-0">
                  Mode
                </th>
                <th scope="col" className="border-0">
                  TI
                </th>
                <th scope="col" className="border-0">
                  SP
                </th>
                <th scope="col" className="border-0">
                  OUT
                </th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>DC 101</td>
                <td>Auto</td>
                <td>GI 101</td>
                <td>\&gt;= 15000</td>
                <td>
                  <span className="text-danger">ON until 1200 then off</span>
                </td>
              </tr>
            </tbody>
          </table>
        </CardBody>
      </Card>
    </div>
  );
};

export default OutputsTable;
