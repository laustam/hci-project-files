<script>
  import Calendar from "../components/Calendar.svelte";
  import CalendarLight from "../components/Calendar_light.svelte";
  import ChartLight from "../components/Chart_light.svelte";
  import Stats from "../components/Stats.svelte";
  let Component = Calendar;
</script>

<div class="global-wrapper">
  <svelte:component this={Component} />
  <div class="bottom-navbar">
    <button on:click={() => (Component = Calendar)} role="button"
      ><CalendarLight /></button
    >
    <button on:click={() => (Component = Stats)} role="button"
      ><ChartLight /></button
    >
  </div>
</div>

<link
  href="https://fonts.googleapis.com/css?family=Lato:400,700&display=swap"
  rel="stylesheet"
/>

<style>
  .global-wrapper {
    width: 360px;
    height: 800px;
    font-family: "Lato", sans-serif;

    margin: auto;
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;

    border: 1px solid #000;
    border-radius: 30px;
  }
  .bottom-navbar {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 50px;

    background-color: #fd7a00;
    color: #fff;

    display: flex;
    justify-content: space-around;
    align-items: center;

    border-radius: 0 0 30px 30px;
  }
  button {
    background: none;
    border: none;
    color: #fff;
    cursor: pointer;
  }
</style>
