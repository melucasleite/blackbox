export const analogPins = [...Array(16)].map((value, index) => {
  return "A" + index;
});

export const digitalPins = [2,3,4,5,6,7,8,9,10,11,12,13,44,45,46].map((value) => {
  return "D" + value;
});
