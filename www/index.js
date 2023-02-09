$(() => {
  let activeTab = "map";

  Shiny.addCustomMessageHandler("toggleActiveTab", ({ requestedTab }) => {
    if (requestedTab === activeTab) {
      return;
    }
    $(".page-main").toggleClass("main-visible");
    activeTab = requestedTab;
  });
});
