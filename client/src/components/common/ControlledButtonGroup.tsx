import React from "react";
import { Button, ButtonGroup } from "shards-react";

const ControlledButtonGroup = ({ active, setActive, options }) => {
  const isActive = (value) => {
    return value === active;
  };

  return (
    <ButtonGroup>
      {options.map((option) => {
        return (
          <Button
            theme="white"
            key={option.value}
            onClick={() => setActive(option.value)}
            active={isActive(option.value)}
          >
            {option.name}
          </Button>
        );
      })}
    </ButtonGroup>
  );
};

export default ControlledButtonGroup;
