(function () {
    "use strict";

    var slider = document.querySelector(".leo-hero-slider");
    if (!slider) return;

    var slides = Array.prototype.slice.call(slider.querySelectorAll(".leo-slide"));
    var dots = Array.prototype.slice.call(slider.querySelectorAll(".leo-slider-dots button"));
    var prev = slider.querySelector(".leo-slider-prev");
    var next = slider.querySelector(".leo-slider-next");
    var count = slider.querySelector(".leo-slide-count strong");
    var progress = slider.querySelector(".leo-slider-progress");
    var loader = slider.querySelector(".leo-slider-loader");
    var current = 0;
    var timer = null;
    var duration = 5800;
    var paused = false;

    function show(index, direction) {
        var old = current;
        current = (index + slides.length) % slides.length;

        slides[old].classList.remove("is-active");
        slides[current].classList.add("is-active");

        dots.forEach(function (dot, i) {
            dot.classList.toggle("is-active", i === current);
            dot.setAttribute("aria-selected", i === current ? "true" : "false");
        });

        if (count) count.textContent = String(current + 1).padStart(2, "0");

        if (progress) {
            progress.classList.remove("is-running");
            void progress.offsetWidth;
            progress.classList.add("is-running");
        }
    }

    function start() {
        clearInterval(timer);
        timer = setInterval(function () {
            if (!paused) show(current + 1);
        }, duration);
    }

    function go(index) {
        show(index);
        start();
    }

    next.addEventListener("click", function () { go(current + 1); });
    prev.addEventListener("click", function () { go(current - 1); });

    dots.forEach(function (dot, i) {
        dot.addEventListener("click", function () { go(i); });
    });

    slider.addEventListener("mouseenter", function () { paused = true; });
    slider.addEventListener("mouseleave", function () { paused = false; });

    document.addEventListener("keydown", function (event) {
        if (event.key === "ArrowRight") go(current + 1);
        if (event.key === "ArrowLeft") go(current - 1);
    });

    // Touch swipe support.
    var touchStartX = 0;
    slider.addEventListener("touchstart", function (e) {
        touchStartX = e.changedTouches[0].screenX;
    }, {passive: true});
    slider.addEventListener("touchend", function (e) {
        var distance = e.changedTouches[0].screenX - touchStartX;
        if (Math.abs(distance) > 50) {
            go(distance < 0 ? current + 1 : current - 1);
        }
    }, {passive: true});

    // A short logo reveal makes the initial load feel intentional rather than abrupt.
    window.addEventListener("load", function () {
        setTimeout(function () {
            if (loader) loader.classList.add("is-hidden");
            show(0);
            start();
        }, 650);
    });

    // Fallback for cached/instant loads.
    setTimeout(function () {
        if (loader && !loader.classList.contains("is-hidden")) {
            loader.classList.add("is-hidden");
            show(0);
            start();
        }
    }, 1600);
})();
