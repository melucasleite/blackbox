import React from "react";
import ControlledButtonGroup from "../common/ControlledButtonGroup";

const FrequencySelector = ({ active, setActive }) => {
  const options = [
    {
      name: "5s",
      value: 5,
    },
    {
      name: "1m",
      value: 60,
    },
    {
      name: "1h",
      value: 60 * 60,
    },
    {
      name: "4h",
      value: 60 * 60 * 4,
    },
    {
      name: "24h",
      value: 60 * 60 * 24,
    },
  ];

  return (
    <ControlledButtonGroup
      setActive={setActive}
      active={active}
      options={options}
    />
  );
};

export default FrequencySelector;
