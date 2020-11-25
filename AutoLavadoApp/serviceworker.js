var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/css/style.css',
    '/static/img/auto.jpg',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {

          return fetch(event.request)
          .catch(function(rsp) {
             return response; 
          });
          
          
        })
    );
});


/////////////////////////////////////////////////////////////////
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');



var firebaseConfig = {
  apiKey: "AIzaSyCFJJ6G8W3YfW_UjWAirXPT1xplVJiVdlE",
  authDomain: "djangosec007-aeaf7.firebaseapp.com",
  databaseURL: "https://djangosec007-aeaf7.firebaseio.com",
  projectId: "djangosec007-aeaf7",
  storageBucket: "djangosec007-aeaf7.appspot.com",
  messagingSenderId: "497061398405",
appId: "1:497061398405:web:0e808e00aa388a74e0e6ec"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

///////////////////////////////////////////////////////////////////////////////
let messaging = firebase.messaging();
///////////////// modelo de notificacion offline //////////////////////////////
messaging.setBackgroundMessageHandler(function(payload){
  let titulo = payload.notification.title
  let opciones = {
    body: payload.notification.body,
    icon: payload.notification.icon
  }
  self.registration.showNotification(titulo, opciones)
});
///////////////////////////////////////////////////////////////////////////////

