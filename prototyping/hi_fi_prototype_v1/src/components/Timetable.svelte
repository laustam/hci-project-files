<script lang="ts">
  let times: string[] = [
    "8 AM",
    "9 AM",
    "10 AM",
    "11 AM",
    "12 AM",
    "1 PM",
    "2 PM",
    "3 PM",
    "4 PM",
    "5 PM",
    "6 PM",
    "7 PM",
  ];

  type Event = { time: string; title: string; duration: number };

  let events: Event[] = [{ time: "11 AM", title: "Meeting", duration: 1 }];

  function eventAtTime(time: string): Event | undefined {
    return events.find((event) => event.time === time);
  }
</script>

<div class="timetable">
  {#each times as time}
    <div class="time-slot">
      {time}
      {#if eventAtTime(time)}
        <div class="event">{eventAtTime(time)?.title}</div>
      {/if}
    </div>
  {/each}
</div>

<style>
  .timetable {
    font-family: Arial, sans-serif;
    background-color: #fff;
    padding: 16px 0;
  }

  .time-slot {
    border-bottom: 1px solid #cbcbcb;
    padding: 10px;
    position: relative;
  }

  .event {
    position: absolute;
    left: 80px;
    top: 2px;
    background-color: #ffd900b7;
    padding: 10px;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    width: 70%;
    height: 130%;
  }
</style>
