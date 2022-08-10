if('serviceWorker' in navigator) {
  navigator.serviceWorker
    .register('respiratory_disease_pyshiny/pwa-service-worker.js', { scope: '/respiratory_disease_pyshiny/' })
    .then(function() { console.log('Service Worker Registered'); });
}
