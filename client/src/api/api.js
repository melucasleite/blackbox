import { getRandomVector } from "../utils";

export const fetchPidGraph = (controllerId, scale, dataPoints = 20) => {
  console.log("fetchPidGraph", controllerId, scale, dataPoints);
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({
        target: getRandomVector(dataPoints),
        reading: getRandomVector(dataPoints),
        output: getRandomVector(dataPoints),
        labels: getRandomVector(dataPoints),
      });
    }, 800);
  });
};

export const fetchControllerParameters = (controllerId) => {
  console.log("fetchControllerParameters", controllerId);
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({
        name: controllerId,
        P: 1.0,
        I: 2.5,
        D: 14,
        inputPort: "A12",
        outputPort: "D3",
        inputMultiplier: 4,
      });
    }, 500);
  });
};

export const updateControllerParameters = (controllerId, parameters) => {
  console.log("updateControllerParameters", controllerId, parameters);
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve();
    }, 115);
  });
};

export const fetchControllers = () => {
  console.log("fetchControllers");
  const controllers = [
    { name: "TIC_101", id: "TIC_101", type: "pid" },
    { name: "GIC_101", id: "GIC_101", type: "pid" },
    { name: "HIC_101", id: "HIC_101", type: "pid" },
    { name: "DIC_101", id: "DIC_101", type: "output" },
  ];
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(controllers);
    }, 650);
  });
};
