$(() => {

  $("#tab_plot").click(() => {
    window.dispatchEvent(new Event("resize"));
  });

  $("#tab_map").click(() => {
    window.dispatchEvent(new Event("resize"));
  });

  Shiny.addCustomMessageHandler("toggleActiveTab", (payload) => {
    if (payload.activeTab === "map") {
      $("#map-container").show()
      $("#plot-container").hide()
    } else {
      $("#plot-container").show()
      $("#map-container").hide()
    }
  });
});
