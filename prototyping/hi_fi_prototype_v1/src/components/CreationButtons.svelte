<script lang="ts">
  import PlayTime from "../components/PlayTime.svelte";
  import Bookmark from "../components/Bookmark.svelte";
  import AddButton from "../components/AddButton.svelte";
  import Timer from "../components/Timer.svelte";

  let showModal = false;

  function onStarButtonClick() {}

  function onPlayButtonClick() {
    showModal = true;
  }

  function onAddEventButtonClick() {}
  import { onMount, onDestroy } from "svelte";
  import Star from "./Star.svelte";
  import Union from "./Union.svelte";
  import CalendarLight from "./Calendar_light.svelte";
  import Calendar from "./Calendar.svelte";

  let time = 0;
  let interval: number | undefined;

  onMount(() => {
    interval = setInterval(() => {
      time += 1;
    }, 1000);
  });

  onDestroy(() => {
    clearInterval(interval);
  });

  $: if (!showModal) {
    time = 0;
  }

  function formatTime(timeInSeconds: number) {
    const hours = Math.floor(timeInSeconds / 3600)
      .toString()
      .padStart(2, "0");
    const minutes = Math.floor((timeInSeconds % 3600) / 60)
      .toString()
      .padStart(2, "0");
    const seconds = (timeInSeconds % 60).toString().padStart(2, "0");
    return `${hours}:${minutes}:${seconds}`;
  }

  let categories = [
    { name: "Work", color: "#FFC331", selectedColor: "black" },
    { name: "Family", color: "#FD7A00", selectedColor: "black" },
    { name: "Gym", color: "#83A51A", selectedColor: "black" },
    { name: "Learn", color: "#4441C4", selectedColor: "black" },
  ];
  let selectedCategory = "";

  function selectCategory(category: string) {
    selectedCategory = category;
  }

  let isTimer = false;

  let timerValue = 0;
</script>

<div class="button-bar">
  <Timer bind:showModal>
    <div class="popup">
      <p class="time">
        {#if showModal}
          {formatTime(time)}
        {/if}
      </p>
      <div class="event-input">
        <input type="text" placeholder="Enter name..." />
      </div>
      <div class="wrapper">
        <div class="categories">
          <Union />
          {#each categories as category}
            <button
              class="category {category.name === selectedCategory
                ? 'selected'
                : ''}"
              on:click={() => selectCategory(category.name)}
              style="background-color: {category.name === selectedCategory
                ? category.selectedColor
                : category.color};"
            >
              {category.name}
            </button>
          {/each}
        </div>
      </div>
      <div class="time-category">
        Stopwatch
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <div on:click={() => (isTimer = !isTimer)} class="toggle-switch">
          <div class="toggle-handle {isTimer ? 'right' : ''}"></div>
        </div>
        Timer
      </div>
      {#if isTimer}
        <div class="timer-slider">
          <input
            class="slider"
            type="range"
            min="0"
            step="5"
            max="120"
            bind:value={timerValue}
          />
          <span>{timerValue}m</span>
        </div>
      {/if}
    </div>
  </Timer>
  <button class="button" on:click={onStarButtonClick}>
    <Star />
  </button>
  <button class="button" on:click={onPlayButtonClick}>
    <PlayTime />
  </button>
  <button class="button" on:click={onAddEventButtonClick}>
    <AddButton />
  </button>
</div>

<style>
  .time {
    display: flex;
    justify-content: center;
    margin: 0px;
  }
  .button-bar {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    padding: 10px;
    background-color: #fff;
  }

  .button {
    width: 80px;
    height: 80px;
    border-radius: 20px;
    background: none;
    border: none;
    padding: 10px;
    cursor: pointer;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .event-input {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10px;
  }
  .categories {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    padding: 5px;
  }
  .toggle-switch {
    width: 40px;
    height: 20px;
    background-color: #ffc331;
    border-radius: 15px;
    position: relative;
    cursor: pointer;
    transition: background-color 0.2s;
  }

  .toggle-switch .toggle-handle {
    position: absolute;
    top: 2px;
    left: 2px;
    width: 16px;
    height: 16px;
    background-color: #2c2c2c;
    border-radius: 50%;
    transition: left 0.2s;
  }

  .toggle-switch .toggle-handle.right {
    left: 22px;
  }

  .toggle-switch:hover {
    background-color: #c99c28;
  }
  .time-category {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    padding: 5px 30px 5px 5px;
  }
  .timer-slider {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 5px;
  }
  .slider {
    width: 100%;
    color: #ffc331;
  }
  .category {
    border: none;
    padding: 4px 8px;
    cursor: pointer;
    margin: 0 5px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
    color: white;
  }
</style>
