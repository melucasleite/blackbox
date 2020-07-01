export default function () {
  return [
    {
      title: "",
      items: [
        {
          title: "Global",
          to: "/home",
          htmlBefore: '<i class="fa fa-columns"/>',
          htmlAfter: "",
        },
      ],
    },
    {
      title: "Controllers",
      items: [
        {
          title: "TIC_101",
          to: "/controller/TIC_101",
          htmlBefore: '<i class="fa fa-temperature-high"/>',
          htmlAfter: "",
        },
        {
          title: "GIC_101",
          to: "/controller/GIC_101",
          htmlBefore: '<i class="fa fa-fan"/>',
          htmlAfter: "",
        },
        {
          title: "HIC_101",
          to: "/controller/HIC_101",
          htmlBefore: '<i class="fa fa-tint"/>',
          htmlAfter: "",
        },
      ],
    },
    {
      title: "OUTPUTS",
      items: [
        {
          title: "DIC_101",
          to: "/controller/DIC_101",
          htmlBefore: '<i class="fa fa-fan"/>',
          htmlAfter: "",
        },
      ],
    },
    {
      title: "LOG",
      items: [
        {
          title: "Door",
          to: "/log/door",
          htmlBefore: '<i class="fa fa-door-open"/>',
          htmlAfter: "",
        },
        {
          title: "Controllers",
          to: "/log/controllers",
          htmlBefore: '<i class="fa fa-database"/>',
          htmlAfter: "",
        },
      ],
    },
  ];
}
