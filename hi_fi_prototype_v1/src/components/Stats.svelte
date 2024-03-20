<script lang="ts">
  import StatsHeader from "./StatsHeader.svelte";
  import PieChart from "./PieChart.svelte";
  import BarChart from "./BarChart.svelte";
  import { writable } from "svelte/store";
  import Union from "./Union.svelte";

  const PI_CATEGORY_LABELS = ["Work", "Family", "Gym", "Learning"];
  const PI_BACKGROUND_COLORS = ["#FFC331", "#FD7A00", "#83A51A", "#4441C4"];
  const PI_HOVER_COLORS = ["#FFC331", "#FD7A00", "#83A51A", "#4441C4"];

  let pieData = writable({
    datasets: [
      {
        data: [38, 28, 15, 10],
        backgroundColor: PI_BACKGROUND_COLORS,
        hoverBackgroundColor: PI_HOVER_COLORS,
      },
    ],
    labels: PI_CATEGORY_LABELS,
  });

  let pieDataWeek = {
    datasets: [
      {
        data: [25, 28, 15, 10],
        backgroundColor: PI_BACKGROUND_COLORS,
        hoverBackgroundColor: PI_HOVER_COLORS,
      },
    ],
    labels: PI_CATEGORY_LABELS,
  };

  let pieDataMonth = {
    datasets: [
      {
        data: [154, 98, 56, 23],
        backgroundColor: PI_BACKGROUND_COLORS,
        hoverBackgroundColor: PI_HOVER_COLORS,
      },
    ],
    labels: PI_CATEGORY_LABELS,
  };

  let pieDataYear = {
    datasets: [
      {
        data: [1890, 648, 742, 490],
        backgroundColor: PI_BACKGROUND_COLORS,
        hoverBackgroundColor: PI_HOVER_COLORS,
      },
    ],
    labels: PI_CATEGORY_LABELS,
  };

  let ogData = {
    // barchart data
    labels: ["M", "T", "W", "T", "F", "S", "S"],
    datasets: [
      {
        label: "Work",
        data: [8, 5, 6, 8, 6, 5, 4],
        backgroundColor: "#FFC331",
      },
      {
        label: "Family",
        data: [2, 3, 4, 1, 2, 1, 3],
        backgroundColor: "#FD7A00",
      },
      {
        label: "Gym",
        data: [1, 2, 1, 1, 1, 2, 2],
        backgroundColor: "#83A51A",
      },
      {
        label: "Learning",
        data: [3, 2, 0, 2, 1, 0, 1],
        backgroundColor: "#4441C4",
      },
    ],
  };

  function updateDataset(event: any) {
    const timeframe = event.target.value;
    if (timeframe === "week") {
      pieData.set(pieDataWeek);
    } else if (timeframe === "month") {
      pieData.set(pieDataMonth);
    } else if (timeframe === "year") {
      pieData.set(pieDataYear);
    }
  }

  let barData = writable(ogData);

  const selectedCategories = writable(new Set(["all"]));

  function toggleCategory(category: string) {
    selectedCategories.update((current) => {
      if (current.has(category)) {
        current.delete(category);
        if (current.size === 0) {
          // If no category is selected, default to "all"
          current.add("all");
        }
      } else {
        current.delete("all"); // Remove "all" if any specific category is added
        current.add(category);
      }
      return current;
    });

    // Filter barData based on the updated selected categories
    filterCategory();
  }

  function filterCategory() {
    selectedCategories.subscribe((current) => {
      if (current.has("all")) {
        barData.set({ ...ogData });
      } else {
        barData.set({
          ...ogData,
          datasets: ogData.datasets.filter((dataset) =>
            current.has(dataset.label)
          ),
        });
      }
    })();
  }

  function darkenColor(color: string, amount = 0.3) {
    return `rgba(0, 0, 0, ${amount}), ${color}`;
  }

  let time = 0;
  $: {
    const totalTimeInSeconds =
      $pieData.datasets[0].data.reduce((acc, curr) => acc + curr, 0) * 3600;
    time = totalTimeInSeconds;
  }

  function formatTime(timeInSeconds: number) {
    const days = Math.floor(timeInSeconds / (3600 * 24));
    const hours = Math.floor((timeInSeconds % (3600 * 24)) / 3600)
      .toString()
      .padStart(2, "0");
    const minutes = Math.floor((timeInSeconds % 3600) / 60)
      .toString()
      .padStart(2, "0");

    return `${days}d ${hours}h ${minutes}m`;
  }
</script>

<div class="global-wrapper">
  <StatsHeader />
  <div>
    <div class="time-tracker">
      <div>Tracked Time</div>
      <div>{formatTime(time)}</div>
      <select on:change={updateDataset}>
        <option value="week">Week</option>
        <option value="month">Month</option>
        <option value="year">Year</option>
      </select>
    </div>
    <div class="doughnut">
      <PieChart pieData={$pieData} />
    </div>
    <BarChart {barData} />
    <div class="filter-bar">
      <Union />
      <div class="filters">
        {#each $pieData.labels as category (category)}
          <button
            class="button {$selectedCategories.has(category) ? 'selected' : ''}"
            on:click={() => toggleCategory(category)}
            style="background-color: {ogData.datasets.find(
              (dataset) => dataset.label === category
            )?.backgroundColor || '#fff'};"
          >
            {category}
          </button>{/each}
      </div>
    </div>
  </div>
</div>

<style>
  .time-tracker {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    padding: 10px;
    font-size: x-large;
  }
  .doughnut {
    display: flex;
    justify-content: center;
    height: 300px;
    padding: 20px;
  }
  .filters {
    display: flex;
    justify-content: space-around;
  }
  .button {
    border: none;
    color: white;
    padding: 10px;
    margin: 5px;
    border-radius: 5px;
    cursor: pointer;
    transition:
      background-color 0.3s,
      filter 0.3s;
  }

  .selected {
    filter: brightness(75%);
  }

  .filter-bar {
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding: 10px 20px 10px 20px;
  }
</style>
