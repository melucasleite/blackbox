import React from "react";
import ReactLoading from "react-loading";
import styled from "styled-components";

const Wrapper = styled.div`
  height: 100px;
  width: 100px;
  opacity: 0.5;
  padding: 35px;
`;

const Loading = () => {
  return (
    <div className="d-flex justify-content-center">
      <Wrapper>
        <ReactLoading
          type={"spokes"}
          color={"#007bff"}
          height={"100%"}
          width={"100%"}
        />
      </Wrapper>
    </div>
  );
};

export default Loading;
