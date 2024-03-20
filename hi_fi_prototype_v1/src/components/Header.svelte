<script>
  import SettingLineLight from "./Setting_line_light.svelte";
</script>

<div class="header">
  <div class="calendar">
    <div>Calendar</div>
    <div>
      <SettingLineLight />
    </div>
  </div>
  <div class="weekdays-container">
    <div class="day-names">
      <div>
        <div class="day">M</div>
        <div class="day">13</div>
      </div>
      <div>
        <div class="day">T</div>
        <div class="day">14</div>
      </div>
      <div>
        <div class="day">W</div>
        <div class="day">15</div>
      </div>
      <div>
        <div class="day">T</div>
        <div class="day">16</div>
      </div>
      <div>
        <div class="day">F</div>
        <div class="day current-day"><span class="day-number">17</span></div>
      </div>
      <div>
        <div class="day">S</div>
        <div class="day">18</div>
      </div>
      <div>
        <div class="day">S</div>
        <div class="day">19</div>
      </div>
    </div>
  </div>
</div>

<style>
  .header {
    background-color: #fff;

    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;

    border-bottom: 1px solid #ccc;
    border-radius: 30px 30px 0px 0px;
  }

  .calendar {
    padding: 20px;
    font-size: 24px;
    display: flex;
    justify-content: space-between;
    width: 90%;
  }

  .weekdays-container {
    background: #fff; /* Example background color */
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
  }

  .day-names,
  .day-numbers {
    display: flex;
    justify-content: space-around;
    width: 100%;
    padding: 20px 0px 10px 0px;
    align-items: center;
  }

  .day {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .current-day {
    color: #ff4500; /* Example highlight color */
  }

  .current-day .day-number {
    border-radius: 25%;
    background-color: #ff4500; /* Example highlight color */
    color: white;
    padding: 0px 5px 0px 5px;
  }
</style>
