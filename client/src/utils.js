import { useState } from "react";

export const getRandomVector = (length) => {
  return [...Array(length)].map(() => {
    return Math.floor(Math.random() * Math.floor(100));
  });
};

export const useInputChange = (defaults) => {
  const [input, setInput] = useState(defaults);

  const handleInputChange = (e) => {
    setInput({
      ...input,
      [e.currentTarget.name]: e.currentTarget.value,
    });
  };

  return [input, handleInputChange, setInput];
};
