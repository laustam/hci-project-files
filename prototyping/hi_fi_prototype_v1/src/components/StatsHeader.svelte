<script>
  import SettingLineLight from "./Setting_line_light.svelte";
</script>

<div class="header">
  <div class="calendar">
    <div>Statistical Overview</div>
    <div>
      <SettingLineLight />
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
</style>
