$(() => {
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
