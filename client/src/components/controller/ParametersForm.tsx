import React, { useEffect } from "react";
import {
  Button,
  Col,
  Form,
  FormGroup,
  FormInput,
  FormSelect,
  Row,
} from "shards-react";
import { useInputChange } from "../../utils";
import { analogPins, digitalPins } from "../../consts";

const ParametersForm = ({ parameters, handleSubmit }) => {
  const [input, handleInputChange, setInput] = useInputChange(parameters);

  useEffect(() => {
    setInput(parameters);
  }, [setInput, parameters]);

  const formOnSubmit = (e) => {
    e.preventDefault();
    handleSubmit(input);
  };
  return (
    <Form onSubmit={formOnSubmit}>
      <FormGroup>
        <label>Name</label>
        <FormInput
          name="name"
          onChange={handleInputChange}
          value={input.name}
        />
      </FormGroup>
      <FormGroup>
        <Row form>
          <Col md="4" className="form-group">
            <label>P</label>
            <FormInput name="P" onChange={handleInputChange} value={input.P} />
          </Col>
          <Col md="4" className="form-group">
            <label>I</label>
            <FormInput name="I" onChange={handleInputChange} value={input.I} />
          </Col>{" "}
          <Col md="4" className="form-group">
            <label>D</label>
            <FormInput name="D" onChange={handleInputChange} value={input.D} />
          </Col>
        </Row>
      </FormGroup>
      <Row form>
        <Col xs="6">
          <h6>Process Variable</h6>
          <div className="border-right pr-3">
            <FormGroup>
              <label>Input Port</label>
              <FormSelect
                id="feInputState"
                name="inputPort"
                value={input.inputPort}
                onChange={handleInputChange}
              >
                {analogPins.map((pin) => {
                  return (
                    <option key={pin} value={pin}>
                      {pin}
                    </option>
                  );
                })}
              </FormSelect>
            </FormGroup>
            <FormGroup>
              <label>inputMultiplier</label>
              <FormInput
                type="number"
                name="inputMultiplier"
                onChange={handleInputChange}
                value={input.inputMultiplier}
              />
            </FormGroup>
          </div>
        </Col>
        <Col xs="6">
          <div className="pl-2">
            <h6>Output</h6>
            <FormGroup>
              <label>Output Port</label>
              <FormSelect
                name="outputPort"
                value={input.outputPort}
                onChange={handleInputChange}
              >
                {digitalPins.map((pin) => {
                  return (
                    <option key={pin} value={pin}>
                      {pin}
                    </option>
                  );
                })}
              </FormSelect>
            </FormGroup>
          </div>
        </Col>
      </Row>
      <Button className="float-right" type="submit">
        Update
      </Button>
    </Form>
  );
};

export default ParametersForm;
