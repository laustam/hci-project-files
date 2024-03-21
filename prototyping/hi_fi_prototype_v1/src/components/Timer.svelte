<script lang="ts">
  export let showModal: boolean; // boolean

  let dialog: HTMLDialogElement; // explicitly specify the type of the dialog variable

  $: if (dialog && showModal) dialog.showModal();
</script>

<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
<!-- svelte-ignore a11y-click-events-have-key-events -->
<dialog
  bind:this={dialog}
  on:close={() => (showModal = false)}
  on:click|self={() => dialog.close()}
>
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <div on:click|stopPropagation>
    <!-- svelte-ignore a11y-autofocus -->
    <button class="close-button" autofocus on:click={() => dialog.close()}
      >✖️</button
    >
    <!-- svelte-ignore a11y-autofocus -->
    <button class="done-button" autofocus on:click={() => dialog.close()}
      >✔️</button
    >
    <slot />
  </div>
</dialog>

<style>
  dialog {
    position: absolute;
    bottom: -525px;
    left: 0;
    right: 0;
    width: 300px;

    background-color: #fff;
    border-radius: 20px;
    border: none;
    box-shadow: 0 -5px 15px rgba(0, 0, 0, 0.1);

    transition: transform 0.3s ease;
    padding: 20px;
    transform: translateY(0);
  }
  dialog::backdrop {
    background: transparent;
  }
  .close-button {
    position: absolute;
    top: 20px;
    left: 20px;
    border: none;
    background: none;
    cursor: pointer;
  }

  .done-button {
    position: absolute;
    top: 20px;
    right: 20px;
    border: none;
    background: none;
    cursor: pointer;
  }
</style>
