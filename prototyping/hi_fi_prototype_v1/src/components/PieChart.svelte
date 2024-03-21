<script lang="ts">
  import { Doughnut } from "svelte-chartjs";
  import { Chart, registerables } from "chart.js";
  import ChartDataLabels from "chartjs-plugin-datalabels";
  Chart.register(...registerables);

  export let pieData: {
    datasets: {
      data: number[];
      backgroundColor: string[];
      hoverBackgroundColor: string[];
    }[];
    labels: string[];
  };

  let options = {
    responsive: true,
    plugins: {
      tooltip: {
        enabled: false,
      },
      legend: {
        display: false,
      },
      datalabels: {
        color: "black",
        formatter: (value: number, ctx: any) => {
          let sum = 0;
          let dataArr = ctx.chart.data.datasets[0].data;
          dataArr.map((data: number) => {
            sum += data;
          });
          let hours = value + "h";
          let percentage = ((value * 100) / sum).toFixed(2) + "%";
          return [hours, percentage];
        },
      },
    },
  };
</script>

<Doughnut {options} data={pieData} plugins={[ChartDataLabels]} />
