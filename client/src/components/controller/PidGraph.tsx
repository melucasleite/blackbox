import React, { useEffect, useRef, useState } from "react";
import colors from "../../utils/colors";
import Chart from "chart.js";

const PidGraph = (props) => {
  const legendRef = useRef<HTMLDivElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [chartInstance, setChartInstance] = useState<Chart>();

  useEffect(() => {
    const newChart = new Chart(canvasRef.current, {
      type: "line",
      data: props.chartData,
      options: chartOptions,
    });
    if (legendRef && legendRef.current) {
      legendRef.current.innerHTML = newChart.generateLegend();
    }
    setChartInstance(newChart);
  }, [canvasRef, legendRef, props.chartData]);

  if (chartInstance) {
    chartInstance.data.datasets[0].data = props.dataset.output;
    chartInstance.data.datasets[1].data = props.dataset.target;
    chartInstance.data.datasets[2].data = props.dataset.reading;
    chartInstance.data.labels = props.dataset.labels;
    chartInstance.update();
  }

  return (
    <React.Fragment>
      <div ref={legendRef} />
      <canvas
        height="120"
        ref={canvasRef}
        style={{ maxWidth: "100% !important" }}
        className="analytics-overview-sessions"
      />
    </React.Fragment>
  );
};

PidGraph.defaultProps = {
  chartData: {
    labels: [],
    datasets: [
      {
        label: "Output",
        fill: "none",
        data: [],
        backgroundColor: colors.salmon.toRGBA(0.1),
        borderColor: colors.salmon.toRGBA(1),
        pointBackgroundColor: colors.white.toHex(),
        pointHoverBackgroundColor: colors.salmon.toRGBA(1),
        borderWidth: 3,
        lineTension: 0.2,
      },
      {
        label: "Process Variable",
        fill: "none",
        data: [],
        backgroundColor: colors.primary.toRGBA(0.1),
        borderColor: colors.primary.toRGBA(1),
        pointBackgroundColor: colors.white.toHex(),
        pointHoverBackgroundColor: colors.primary.toRGBA(1),
        borderWidth: 3,
        pointRadius: 0,
        pointBorderColor: colors.primary.toRGBA(1),
        lineTension: 0.2,
      },
      {
        label: "Setpoint",
        fill: "none",
        data: [],
        backgroundColor: colors.green.toRGBA(0.1),
        borderColor: colors.green.toRGBA(1),
        pointBackgroundColor: colors.white.toHex(),
        pointHoverBackgroundColor: colors.green.toRGBA(1),
        borderWidth: 3,
        pointBorderColor: colors.green.toRGBA(1),
        lineTension: 0.2,
      },
    ],
  },
};

const chartOptions = {
  responsive: true,
  legend: false,
  elements: {
    line: {
      tension: 0.38,
    },
  },
  scales: {
    xAxes: [
      {
        gridLines: false,
      },
    ],
    yAxes: [
      {
        ticks: {
          beginAtZero: true,
        },
      },
    ],
  },
  tooltips: {
    enabled: false,
    mode: "index",
    position: "nearest",
  },
};

export default PidGraph;
