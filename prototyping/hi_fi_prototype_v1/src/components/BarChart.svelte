<script lang="ts">
  import { Bar } from "svelte-chartjs";
  import { Chart, registerables } from "chart.js";
  Chart.register(...registerables);

  export let barData: {
    labels: string[];
    datasets: {
      label: string;
      data: number[];
      backgroundColor: string;
    }[];
  };

  let options = {
    responsive: true,
    scales: {
      x: {
        stacked: true,
      },
      y: {
        stacked: true,
      },
    },
    plugins: {
      legend: {
        display: false,
      },
      tooltip: {
        enabled: true,
        mode: "point",
        callbacks: {
          label: function (context: any) {
            let label = context.dataset.label || "";

            if (label) {
              label += ": ";
            }
            label += context.parsed.y + "h";
            return label;
          },
        },
      },
    },
    interaction: {
      mode: "point",
      intersect: true,
    },

    events: ["click"],
  };
</script>

<Bar data={$barData} {options} />
