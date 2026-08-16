document.addEventListener('DOMContentLoaded', function () {
    var hero = document.getElementById('hero-content');

    if (hero){
        var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        if (reduceMotion) return;

        function onScroll() {
            var heroSection = hero.closest('section');
            var rect = heroSection.getBoundingClientRect();
            var heroHeight = heroSection.offsetHeight;
            // progress: 0 while hero is fully in view, 1 once it has scrolled fully past
            var progress = Math.min(Math.max(-rect.top / heroHeight, 0), 1);
            hero.style.opacity = String(1 - progress);
        }

        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();
    }

    
    // Play demo video if hovering on project
    const projects = document.querySelectorAll(".projecthover");

    if (projects){
        projects.forEach(ele => {
            const timeoutIn = 2200;     // In ms

            const thumbnail = ele.children[0];      // Get the thumbnail div
            const pbar = thumbnail.querySelector(".progressbar");   // Progress bar
            const img = thumbnail.querySelector(".projectimg");     // Image
            const video = thumbnail.querySelector(".projectvid");   // Video
            
            let timer;      // For preview
            let interval;   // For progress bar

            if (video){
                // Start timer when focused
                ele.addEventListener("mouseenter", function(e){
                    // Load progress bar
                    if (pbar){
                        pbar.style.width = "0%";
                        pbar.classList.remove("hidden");

                        const steps = 2;        // Step count
                        const iteration = (timeoutIn / (100/steps));    // each step in ms

                        let stopwatch = 0;

                        interval = setInterval(() => {      // Progress - 100%/2(each step) -> 50iteration -> 2000ms/50 = 40ms(each step)
                            if (stopwatch <= 100){
                                stopwatch += steps;
                                pbar.style.width = String(stopwatch) + "%";
                            }
                        }, iteration);
                    }


                    // Timer for preview
                    timer = setTimeout(() => {
                        startPreview();
                    }, timeoutIn);

                    // Demo video preview
                    function startPreview(){
                        if (img){
                            img.classList.add("hidden");
                        }
                        if (video){
                            video.classList.remove("hidden");
                            // console.log(i.readyState);

                            // Hide progress bar when video starts playing
                            if (pbar){
                                pbar.classList.add("hidden");
                                clearInterval(interval);
                            }
                        }
                    }
                });


                // End timer
                ele.addEventListener("mouseleave", function(e){     // Stop demo preview if left before 2s
                    if (timer){
                        clearTimeout(timer);
                        clearInterval(interval);
                        stopPreview();

                        // Stop preview
                        function stopPreview(){
                            if (img){
                                img.classList.remove("hidden");
                            }
                            if (video){
                                video.classList.add("hidden");
                            }
                        }

                        // Hide progress bar
                        if (pbar){
                            pbar.classList.add("hidden");

                        }
                    }
                });
            }   // If video ends
        })
    }



    // Read more button for desc
    const desc = document.getElementById("project_desc");
    const readmore = document.getElementById("desc_readmore");

    if (desc && readmore){
        const original_desc = desc.textContent
        if (desc.textContent.length > 350){
            // Slice string
            desc.textContent = original_desc.substring(0, 350);
            readmore.classList.remove("hidden");
        }

        // Show full content if read more is pressed
        readmore.addEventListener("click", function(){
            desc.textContent = original_desc;
            readmore.classList.add("hidden");
        })
    }
});