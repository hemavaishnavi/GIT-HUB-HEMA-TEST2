	
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title> Balaji & Vaishu - A Magical Celebration</title>

    <!-- Open Graph / WhatsApp Preview Tags -->
    <meta property="og:title" content="Balaji & Vaishu - Wedding Invitation">
    <meta property="og: description" content=" Join us in our magical journey of love.">
    <meta property="og:image" content="https://theluxuryinvites.com/custom/K.Balaji_T.G.Hema Vaishnavi/img2.jpeg">
    <meta property="og:type" content="website">

    <link rel="icon" href="https://theluxuryinvites.com/custom/K.Balaji_T.G.Hema Vaishnavi/img2.jpeg" type="image/jpeg">

    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Outfit:wght@300;400;500;600&family=Pinyon+Script&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        script: ['"Pinyon Script"', 'cursive'],
                        serif: ['"Cinzel"', 'serif'],
                        sans: ['"Outfit"', 'sans-serif'],
                    },
                    colors: {
                        gold: '#FACC15',
                        glass: 'rgba(255, 255, 255, 0.1)',
                        glassBorder: 'rgba(255, 255, 255, 0.2)',
                    }
                }
            }
        }
    </script>
    <style>
        : root {
            --bg-color: #0b0914;
        }

        body {
            background-color: var(--bg-color);
            color: #ffffff;
            overflow-x: hidden;
            font-family: 'Outfit', sans-serif;
            perspective: 1000px; /* Global perspective for 3D */
            margin: 0;
            padding: 0;
        }

        /* --- DYNAMIC ANIMATED BACKGROUND --- */
        .bg-blobs {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            z-index: -2;
            overflow: hidden;
            background: var(--bg-color);
        }

        .blob {
            position: absolute;
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.6;
            animation: moveBlob 20s infinite alternate ease-in-out;
            will-change: transform;
        }

        .blob-1 { top: -10%; left: -10%; width: 50vw; height: 50vw; background: #ff007f; animation-delay: 0s; }
        .blob-2 { bottom: -20%; right: -10%; width: 60vw; height: 60vw; background: #7928ca; animation-delay: -5s; }
        .blob-3 { top: 40%; left: 30%; width: 40vw; height: 40vw; background: #ff4d4d; animation-delay: -10s; }
        .blob-4 { bottom: 10%; left: 10%; width: 45vw; height: 45vw; background: #4361ee; animation-delay: -15s; opacity: 0.4;}

        @keyframes moveBlob {
            0% { transform: translate(0, 0) scale(1); }
            33% { transform: translate(10vw, 15vh) scale(1.1); }
            66% { transform: translate(-10vw, -10vh) scale(0.9); }
            100% { transform: translate(5vw, -15vh) scale(1.05); }
        }

        #particles-canvas {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            z-index: -1;
            pointer-events: none;
        }

        /* --- 3D GLASSMORPHISM CARDS --- */
        .glass-panel {
            background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.03));
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.15);
            border-top: 1px solid rgba(255,255,255,0.3);
            border-left: 1px solid rgba(255,255,255,0.3);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
            border-radius: 24px;
            transform-style: preserve-3d;
            position: relative;
            transition: border 0.3s ease;
        }

        .glass-panel::before {
            content: '';
            position: absolute;
            inset: 0;
            border-radius: 24px;
            padding: 2px;
            background: linear-gradient(135deg, rgba(255,255,255,0.4), transparent, rgba(255,255,255,0.1));
            -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            pointer-events: none;
        }

        .tilt-wrapper {
            transform-style: preserve-3d;
            perspective: 1000px;
        }

        /* 3D Depth Elements */
        .depth-1 { transform: translateZ(20px); }
        .depth-2 { transform: translateZ(40px); }
        .depth-3 { transform: translateZ(60px); }
        .depth-text { 
            transform: translateZ(50px);
            text-shadow: 0 10px 20px rgba(0,0,0,0.4);
        }

        /* --- TEXT GRADIENTS --- */
        .text-gradient-gold {
            background: linear-gradient(to right, #bf953f, #fcf6ba, #b38728, #fbf5b7, #aa771c);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .text-gradient-pink {
            background: linear-gradient(135deg, #ff007f, #ff758c);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        /* --- 3D CAROUSEL --- */
        .carousel-container {
            perspective: 1200px;
            width: 100%;
            height: 400px;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 40px 0;
        }
        
        .carousel {
            width: 250px;
            height: 350px;
            position: relative;
            transform-style: preserve-3d;
            transition: transform 1s cubic-bezier(0.25, 1, 0.5, 1);
        }
        
        .carousel-item {
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
            border: 2px solid rgba(255,255,255,0.2);
            -webkit-box-reflect: below 10px linear-gradient(transparent, transparent, rgba(0,0,0,0.2));
        }

        .carousel-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        /* --- SCROLL REVEAL ANIMATIONS --- */
        .reveal-3d {
            opacity: 0;
            transform: rotateX(20deg) translateY(50px) scale(0.9);
            transition: opacity 1s ease-out, transform 1s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            will-change: opacity, transform;
        }

        .reveal-3d.visible {
            opacity: 1;
            transform: rotateX(0) translateY(0) scale(1);
        }

        .reveal-left { transform: rotateY(-30deg) translateX(-100px); }
        .reveal-right { transform: rotateY(30deg) translateX(100px); }
        .reveal-left.visible, .reveal-right.visible { transform: rotateY(0) translateX(0); }

        /* Floating Animation */
        @keyframes floating {
            0% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-15px) rotate(1deg); }
            100% { transform: translateY(0px) rotate(0deg); }
        }
        .animate-float { animation: floating 6s ease-in-out infinite; }
        
        @keyframes pulse-glow {
            0%, 100% { filter: drop-shadow(0 0 15px rgba(255, 0, 127, 0.4)); }
            50% { filter: drop-shadow(0 0 30px rgba(255, 0, 127, 0.8)); }
        }
        .animate-glow { animation: pulse-glow 3s infinite; }

        /* Audio Button */
        .audio-btn {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.2);
            box-shadow: 0 0 20px rgba(0,0,0,0.3);
            transition: all 0.3s;
        }
        .audio-btn:hover { background: rgba(255,255,255,0.2); transform: scale(1.1); }

        /* Intro Portal */
        #portal-intro {
            background: radial-gradient(circle at center, #1a0b2e 0%, #000000 100%);
        }
        .portal-ring {
            border: 2px solid rgba(255,255,255,0.1);
            border-radius: 50%;
            position: absolute;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            box-shadow: 0 0 40px rgba(255, 0, 127, 0.5), inset 0 0 40px rgba(121, 40, 202, 0.5);
            animation: ringSpin 10s linear infinite;
        }
        @keyframes ringSpin {
            0% { transform: translate(-50%, -50%) rotate(0deg) scale(1); }
            50% { transform: translate(-50%, -50%) rotate(180deg) scale(1.1); }
            100% { transform: translate(-50%, -50%) rotate(360deg) scale(1); }
        }
        .portal-text {
            text-shadow: 0 0 20px rgba(255,255,255,0.8);
            letter-spacing: 0.3em;
        }
    </style>
</head>

<body>

    <!-- DYNAMIC BACKGROUND -->
    <div class="bg-blobs">
        <div class="blob blob-1"></div>
        <div class="blob blob-2"></div>
        <div class="blob blob-3"></div>
        <div class="blob blob-4"></div>
    </div>
    <canvas id="particles-canvas"></canvas>

    <!-- INTRO PORTAL -->
    <div id="portal-intro" class="fixed inset-0 z-[100] flex items-center justify-center transition-all duration-1000 cursor-pointer">
        <div class="portal-ring w-[300px] h-[300px] md:w-[500px] md:h-[500px]"></div>
        <div class="portal-ring w-[280px] h-[280px] md:w-[460px] md:h-[460px]" style="animation-direction: reverse; border-color: rgba(255,255,255,0.3);"></div>
        <div class="z-10 flex flex-col items-center">
            <h1 class="font-script text-5xl md:text-7xl text-white mb-4 animate-glow">D & R</h1>
            <p class="portal-text font-sans text-xs md:text-sm uppercase text-white/80 animate-pulse">Tap to Enter</p>
        </div>
    </div>

    <!-- AUDIO TOGGLE -->
    <button id="audio-toggle" class="fixed bottom-6 right-6 md:bottom-8 md:right-8 z-50 audio-btn w-12 h-12 rounded-full flex items-center justify-center text-white outline-none">
        <svg id="icon-muted" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
            <line x1="23" y1="9" x2="17" y2="15"></line>
            <line x1="17" y1="9" x2="23" y2="15"></line>
        </svg>
        <svg id="icon-playing" class="hidden" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
            <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path>
        </svg>
    </button>

    <!-- MAIN CONTENT -->
    <main id="main-content" class="relative z-10 w-full max-w-7xl mx-auto px-4 sm:px-8 py-10 opacity-0 transition-opacity duration-1000" style="display:none;">

        <!-- HERO SECTION -->
        <section class="min-h-[90vh] flex flex-col items-center justify-center text-center relative pt-10">
            <div class="tilt-wrapper w-full max-w-3xl cursor-default animate-float">
                <div class="glass-panel p-10 md:p-16 flex flex-col items-center justify-center">
                    <p class="font-sans text-xs md:text-sm tracking-[0.3em] uppercase text-white/70 mb-6 depth-1">
                        Join us in the celebration of love
                    </p>
                    
                    <div class="relative w-full flex flex-col items-center depth-3">
                        <h1 class="font-script text-[5rem] sm:text-[7rem] md:text-[9rem] leading-none text-white drop-shadow-2xl animate-glow">
                            Balaji
                        </h1>
                        <span class="font-serif text-3xl md:text-5xl text-gold italic my-[-10px] md:my-[-20px] depth-2 z-10">&</span>
                        <h1 class="font-script text-[5rem] sm:text-[7rem] md:text-[9rem] leading-none text-white drop-shadow-2xl animate-glow">
                            Vaishu
                        </h1>
                    </div>
                    
                    <div class="w-24 h-[1px] bg-gradient-to-r from-transparent via-white to-transparent my-8 depth-1"></div>
                    
                    <p class="font-serif text-lg md:text-2xl text-white/90 depth-2">
                        August 31, 2026
                    </p>
                    <p class="font-sans text-xs md:text-sm tracking-widest uppercase text-white/60 mt-4 depth-1">
                        Chennai, Tamil Nadu
                    </p>
                </div>
            </div>
            
            <div class="absolute bottom-10 flex flex-col items-center gap-2 opacity-60 animate-bounce">
                <span class="text-[10px] tracking-widest uppercase font-sans">Scroll to discover</span>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 5v14M19 12l-7 7-7-7"/></svg>
            </div>
        </section>

        <!-- FAMILIES SECTION -->
        <section class="py-20 flex flex-col items-center text-center">
            <h2 class="font-serif text-3xl md:text-5xl text-gradient-gold mb-12 reveal-3d">Our Families</h2>
            
            <div class="flex flex-col md:flex-row gap-8 md:gap-12 w-full max-w-5xl">
                <!-- Groom's Family -->
                <div class="tilt-wrapper flex-1 reveal-3d reveal-right">
                    <div class="glass-panel p-8 h-full flex flex-col items-center justify-center">
                        <h3 class="font-script text-4xl md:text-5xl text-white mb-2 depth-2">K.Balaji</h3>
                        <p class="font-sans text-[10px] uppercase tracking-[0.2em] text-white/50 mb-4 depth-1">Son of</p>
                        <p class="font-serif text-lg md:text-xl text-white/90 depth-2">S.Karthikyeyan</p>
                        <p class="font-serif text-sm md:text-md text-white/70 italic mb-2 depth-1">&</p>
                        <p class="font-serif text-lg md:text-xl text-white/90 depth-2">K.Maha Lakshmi</p>
                    </div>
                </div>
                <!-- Bride's Family -->
                <div class="tilt-wrapper flex-1 reveal-3d reveal-left">
                    <div class="glass-panel p-8 h-full flex flex-col items-center justify-center">
                        <h3 class="font-script text-4xl md:text-5xl text-white mb-2 depth-2">T.G.Hema Vaishnavi</h3>
                        <p class="font-sans text-[10px] uppercase tracking-[0.2em] text-white/50 mb-4 depth-1">Daughter of</p>
                        <p class="font-serif text-lg md:text-xl text-white/90 depth-2">G. Vijayalakshmi</p>
                        <p class="font-serif text-sm md:text-md text-white/70 italic mb-2 depth-1">&</p>
                        <p class="font-serif text-lg md:text-xl text-white/90 depth-2">T.N.Gokula Krishnan</p>
                    </div>
                </div>

                <!-- Divider -->
                <div class="hidden md:flex items-center justify-center">
                    <div class="w-[1px] h-32 bg-gradient-to-b from-transparent via-white/50 to-transparent"></div>
                </div>

                
            </div>
        </section>

        <!-- VENUE SECTION -->
        <section id="venue-section" class="py-20 flex flex-col items-center text-center">
            <h3 class="font-sans text-[10px] md:text-xs tracking-[0.3em] uppercase text-white/60 mb-8 reveal-3d">The Celebration Takes Place At</h3>
            
            <div class="tilt-wrapper w-full max-w-4xl reveal-3d">
                <div class="glass-panel overflow-hidden p-2">
                    <div class="relative w-full aspect-[21/9] rounded-xl overflow-hidden group">
                        <!-- Using a subtle overlay on the venue image to make it blend with the theme -->
                        <div class="absolute inset-0 bg-gradient-to-tr from-[#7928ca]/40 to-[#ff007f]/40 mix-blend-overlay z-10"></div>
                        <img src="img2.png" alt="Venue Illustration" class="w-full h-full object-cover filter contrast-125 transition-transform duration-1000 group-hover:scale-110" />
                        
                        <div class="absolute inset-0 z-20 flex flex-col items-center justify-center bg-black/40 backdrop-blur-sm p-6">
                            <h1 class="font-serif text-3xl sm:text-5xl md:text-6xl text-white drop-shadow-xl depth-3 mb-4 text-center">
                                SWAPNA THIRUMANA MANDAPAM
                            </h1>
                            <a href="https://www.google.com/maps/place/SWAPNA+THIRUMANA+MANDAPAM/@12.8572783,80.067826,17z/data=!4m12!1m5!3m4!2zMTLCsDUxJzI2LjIiTiA4MMKwMDQnMTMuNCJF!8m2!3d12.8572783!4d80.0704009!3m5!1s0x3a52f7a1a1f741df:0x631537a44bcb105e!8m2!3d12.8569927!4d80.0693933!16s%2Fg%2F11f5jpwp8t?entry=ttu&g_ep=EgoyMDI2MDQyOS4wIKXMDSoASAFQAw%3D%3D" target="_blank" 
                               class="depth-2 inline-flex items-center gap-2 px-6 py-3 bg-white/10 hover:bg-white/20 border border-white/30 rounded-full backdrop-blur-md transition-all text-white text-sm uppercase tracking-wider">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                                Get Directions
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- EVENTS TIMELINE (3D Vertical Journey) -->
        <section class="py-20 relative w-full max-w-5xl mx-auto">
            <h2 class="font-serif text-4xl md:text-6xl text-center text-white mb-20 reveal-3d">Festivities</h2>
            
            <!-- Central Line -->
            <div class="absolute left-4 md:left-1/2 top-48 bottom-0 w-[2px] bg-gradient-to-b from-white/0 via-white/30 to-white/0 md:-ml-[1px]"></div>

            <div class="flex flex-col gap-12 md:gap-24">
                               
				<!-- Day 4 -->
                <div class="flex flex-col md:flex-row items-center w-full reveal-3d reveal-right">
                    <div class="hidden md:block w-1/2"></div>
                    <div class="w-full md:w-1/2 md:pl-12 flex justify-start pl-10 md:pl-0 relative">
                        <div class="absolute left-[-11px] md:left-[-6px] top-1/2 -translate-y-1/2 w-3 h-3 rounded-full bg-cyan-400 shadow-[0_0_15px_#22d3ee]"></div>
                        <div class="tilt-wrapper w-full max-w-md text-left">
                            <div class="glass-panel p-6 md:p-8">
                                <span class="font-sans text-xs font-bold tracking-widest text-cyan-400 uppercase depth-1">31 August 2026 | Monday</span>
                                <h4 class="font-script text-4xl text-white my-2 depth-2">Muhurtham</h4>
                                <p class="font-serif text-sm md:text-base text-white/80 depth-1">9:30 AM - 10:30 AM</p>
                                <p class="font-serif text-sm md:text-base font-semibold text-white mt-2 depth-2">Sri Padalathri Narasimhar Thirukovil (SP singaperumalkoil)</p>
                                <p class="font-sans text-[10px] text-white/50 uppercase tracking-widest mt-1 depth-1">Hinkal, Hunsur Road, Mysore</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Day 3 -->
                <div class="flex flex-col md:flex-row items-center w-full reveal-3d reveal-left">
                    <div class="w-full md:w-1/2 md:pr-12 flex justify-end pl-10 md:pl-0 relative">
                        <div class="absolute left-[-11px] md:right-[-6px] md:left-auto top-1/2 -translate-y-1/2 w-3 h-3 rounded-full bg-purple-500 shadow-[0_0_15px_#a855f7]"></div>
                        <div class="tilt-wrapper w-full max-w-md text-left md:text-right">
                            <div class="glass-panel p-6 md:p-8">
                                <span class="font-sans text-xs font-bold tracking-widest text-purple-400 uppercase depth-1">31 Auguest 2026 | Monday</span>
                                <h4 class="font-script text-4xl text-white my-2 depth-2">Reception</h4>
                                <p class="font-serif text-sm md:text-base text-white/80 depth-1">6:00 PM onwards</p>
                                <p class="font-serif text-sm md:text-base font-semibold text-white mt-2 depth-2">SWAPNA THIRUMANA MANDAPAM</p>
                                <p class="font-sans text-[10px] text-white/50 uppercase tracking-widest mt-1 depth-1">Swapna Thirumana Mandapam, 245, Grand Southern Trunk Road, Abnirami Nagar, Urapakkam, Chennai, Tamil Nadu 603210</p>
                            </div>
                        </div>
                    </div>
                    <div class="hidden md:block w-1/2"></div>
                </div>
				
            </div>
        </section>

        <!-- 3D MOMENTS CAROUSEL -->
        <section class="py-20 flex flex-col items-center w-full overflow-hidden reveal-3d">
            <h3 class="font-sans text-[10px] md:text-xs tracking-[0.3em] uppercase text-white/60 mb-2">Captured with love</h3>
            <h2 class="font-serif text-4xl md:text-6xl text-white mb-10">Moments</h2>
            
            <div class="carousel-container cursor-grab active:cursor-grabbing" id="carousel-container">
                <div class="carousel" id="carousel">
                    <!-- Javascript will populate this to handle dynamic rotation -->
                    <div class="carousel-item" style="transform: rotateY(0deg) translateZ(250px);"><img src="img1.jpeg" alt="Moment 1" /></div>
                    <div class="carousel-item" style="transform: rotateY(90deg) translateZ(250px);"><img src="https://uploads.onecompiler.io/44ndm3p3s/44ndm3z82/img1.jpeg.png" alt="Moment 2" /></div>
                    <div class="carousel-item" style="transform: rotateY(180deg) translateZ(250px);"><img src="img4.jpeg" alt="Moment 3" /></div>
                    <div class="carousel-item" style="transform: rotateY(270deg) translateZ(250px);"><img src="img6.jpeg" alt="Moment 4" /></div>
                </div>
            </div>
            
            <div class="flex gap-4 mt-8">
                <button id="car-prev" class="w-10 h-10 rounded-full glass-panel flex items-center justify-center text-white hover:bg-white/20 transition-all"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg></button>
                <button id="car-next" class="w-10 h-10 rounded-full glass-panel flex items-center justify-center text-white hover:bg-white/20 transition-all"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg></button>
            </div>
        </section>

        <!-- HASHTAG SECTION -->
        <section class="py-20 flex flex-col items-center text-center reveal-3d">
            <h3 class="font-sans text-[10px] md:text-xs tracking-[0.3em] uppercase text-white/60 mb-4">Share the love</h3>
            <h2 class="font-script text-[4rem] sm:text-[6rem] md:text-[8rem] text-gradient-pink leading-none drop-shadow-2xl animate-pulse">#Balshu</h2>
            <p class="font-serif text-lg text-white/80 mt-6 max-w-xl px-4">
                We'd love to see the wedding through your eyes.<br>Please tag us in your photos and videos!
            </p>
        </section>

        <!-- FOOTER / RSVP / BLESSINGS -->
        <section class="py-20 flex flex-col items-center justify-center w-full">
            <div class="tilt-wrapper w-full max-w-4xl reveal-3d">
                <div class="glass-panel p-8 md:p-16 text-center flex flex-col items-center">
                    
                    <h2 class="font-serif text-3xl md:text-5xl text-gold mb-8 depth-3">Warm Regards</h2>
                    <p class="font-sans text-xs uppercase tracking-widest text-white/50 mb-6 depth-1">With the Blessings of</p>
                    
                    <div class="flex flex-col md:flex-row gap-8 md:gap-16 justify-center w-full font-serif text-sm md:text-lg text-white/90 mb-12 depth-2">
                        <div class="flex-1 text-center md:text-right">
                            <p>Smt. DhanaLakshmi & Sri Ramesh .N.Gowda</p>
                            <p class="text-white/60 text-sm mt-1">Mrs. Sangeetha & Mrs. Rekha</p>
                        </div>
                        <div class="hidden md:block w-[1px] bg-white/20"></div>
                        <div class="flex-1 text-center md:text-left">
                            <p>Smt. M.S. Shobharani & Sri. B. Venkatram</p>
                            <p class="text-white/60 text-sm mt-1">Kum. Vaishnavi. V, B.E., Civil</p>
                        </div>
                    </div>
                    <p class="font-serif text-xl font-bold text-white depth-3 mb-16">Family & Friends</p>

                    <div class="w-full h-[1px] bg-gradient-to-r from-transparent via-white/30 to-transparent mb-16 depth-1"></div>

                    <h2 class="font-serif text-3xl md:text-5xl text-white mb-6 depth-3">RSVP</h2>
                    <p class="font-sans text-sm text-white/70 mb-8 depth-2 max-w-md text-center">Please feel free to contact us for any assistance or to confirm your arrival.</p>
                    
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 w-full max-w-2xl depth-3">
                        <a href="https://wa.me/919916779020" target="_blank" class="glass-panel p-4 hover:bg-white/10 transition-colors flex justify-between items-center group">
                            <span class="font-serif">Ramesh.N</span>
                            <span class="font-sans text-sm text-gold group-hover:text-white transition-colors">9916779020</span>
                        </a>
                        <a href="https://wa.me/918310744590" target="_blank" class="glass-panel p-4 hover:bg-white/10 transition-colors flex justify-between items-center group">
                            <span class="font-serif">T.G.Hema Vaishnavi R</span>
                            <span class="font-sans text-sm text-gold group-hover:text-white transition-colors">8310744590</span>
                        </a>
                        <a href="https://wa.me/919449076225" target="_blank" class="glass-panel p-4 hover:bg-white/10 transition-colors flex justify-between items-center group">
                            <span class="font-serif">B. Venkatram</span>
                            <span class="font-sans text-sm text-gold group-hover:text-white transition-colors">9449076225</span>
                        </a>
                        <a href="https://wa.me/919880382803" target="_blank" class="glass-panel p-4 hover:bg-white/10 transition-colors flex justify-between items-center group">
                            <span class="font-serif">K.Balaji</span>
                            <span class="font-sans text-sm text-gold group-hover:text-white transition-colors">9880382803</span>
                        </a>
                    </div>

                    <h3 class="font-script text-5xl md:text-7xl text-white mt-20 depth-3 animate-glow">Thank You</h3>
                </div>
            </div>

            <div class="mt-16 text-center">
                <p class="text-[10px] md:text-[12px] font-sans tracking-[0.2em] uppercase text-white/40">
                    Made With Love ❤️ by <a href="https://theluxuryinvites.com/" target="_blank" class="text-white hover:text-pink-400 font-bold transition-colors">The Luxury Invites</a>
                </p>
            </div>
        </section>

    </main>

    <audio id="bg-music" loop preload="auto">
        <source src="music.mp3" type="audio/mp3">
    </audio>

    <script>
        document.addEventListener('DOMContentLoaded', () => {

            // --- INTRO PORTAL LOGIC ---
            const portal = document.getElementById('portal-intro');
            const mainContent = document.getElementById('main-content');
            let isEntered = false;

            portal.addEventListener('click', () => {
                if(isEntered) return;
                isEntered = true;
                
                // Portal exit animation
                portal.style.transform = 'scale(5) translateZ(500px)';
                portal.style.opacity = '0';
                
                setTimeout(() => {
                    portal.style.display = 'none';
                    mainContent.style.display = 'block';
                    // Trigger reflow
                    void mainContent.offsetWidth;
                    mainContent.style.opacity = '1';
                    
                    // Attempt auto-play audio
                    toggleAudio();
                }, 800);
            });

            // --- AUDIO LOGIC ---
            const audio = document.getElementById('bg-music');
            const audioBtn = document.getElementById('audio-toggle');
            const iconMuted = document.getElementById('icon-muted');
            const iconPlaying = document.getElementById('icon-playing');
            let isPlaying = false;

            function toggleAudio(e) {
                if(e) e.stopPropagation();
                if(isPlaying) {
                    audio.pause();
                    isPlaying = false;
                    iconPlaying.classList.add('hidden');
                    iconMuted.classList.remove('hidden');
                } else {
                    const playPromise = audio.play();
                    if (playPromise !== undefined) {
                        playPromise.then(() => {
                            isPlaying = true;
                            iconMuted.classList.add('hidden');
                            iconPlaying.classList.remove('hidden');
                        }).catch(err => console.log("Audio requires interaction"));
                    }
                }
            }
            audioBtn.addEventListener('click', toggleAudio);

            // --- 3D TILT EFFECT ON MOUSE MOVE ---
            const tiltWrappers = document.querySelectorAll('.tilt-wrapper');
            
            tiltWrappers.forEach(wrapper => {
                const inner = wrapper.querySelector('.glass-panel');
                
                wrapper.addEventListener('mousemove', (e) => {
                    const rect = wrapper.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    
                    const centerX = rect.width / 2;
                    const centerY = rect.height / 2;
                    
                    const rotateX = ((y - centerY) / centerY) * -10; // Max 10 deg
                    const rotateY = ((x - centerX) / centerX) * 10;
                    
                    inner.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
                });

                wrapper.addEventListener('mouseleave', () => {
                    inner.style.transform = `rotateX(0deg) rotateY(0deg)`;
                    inner.style.transition = 'transform 0.5s cubic-bezier(0.25, 1, 0.5, 1)';
                });
                
                wrapper.addEventListener('mouseenter', () => {
                    inner.style.transition = 'none'; // remove transition for smooth tracking
                });
            });

            // DEVICE ORIENTATION FOR MOBILE TILT
            if (window.DeviceOrientationEvent) {
                window.addEventListener('deviceorientation', (e) => {
                    if(!e.gamma || !e.beta) return;
                    // Gamma is left/right (-90 to 90)
                    // Beta is front/back (-180 to 180)
                    let rotateY = Math.max(-15, Math.min(15, e.gamma / 3));
                    let rotateX = Math.max(-15, Math.min(15, (e.beta - 45) / 3)); 
                    
                    tiltWrappers.forEach(wrapper => {
                        const inner = wrapper.querySelector('.glass-panel');
                        // Add transition for gyro to make it smooth
                        inner.style.transition = 'transform 0.2s ease-out';
                        inner.style.transform = `rotateX(${-rotateX}deg) rotateY(${rotateY}deg)`;
                    });
                });
            }

            // --- SCROLL REVEAL (INTERSECTION OBSERVER) ---
            const revealElements = document.querySelectorAll('.reveal-3d');
            const revealOptions = {
                threshold: 0.15,
                rootMargin: "0px 0px -50px 0px"
            };

            const revealObserver = new IntersectionObserver(function(entries, observer) {
                entries.forEach(entry => {
                    if (!entry.isIntersecting) return;
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                });
            }, revealOptions);

            revealElements.forEach(el => revealObserver.observe(el));

            // --- 3D CAROUSEL LOGIC ---
            const carousel = document.getElementById('carousel');
            let currDeg = 0;
            
            document.getElementById('car-next').addEventListener('click', () => {
                currDeg -= 90;
                carousel.style.transform = `rotateY(${currDeg}deg)`;
            });
            
            document.getElementById('car-prev').addEventListener('click', () => {
                currDeg += 90;
                carousel.style.transform = `rotateY(${currDeg}deg)`;
            });
            
            // Auto rotate carousel
            setInterval(() => {
                if(isEntered && document.visibilityState === 'visible') {
                    currDeg -= 90;
                    carousel.style.transform = `rotateY(${currDeg}deg)`;
                }
            }, 4000);

            // --- CUSTOM CANVAS PARTICLES ---
            const canvas = document.getElementById('particles-canvas');
            const ctx = canvas.getContext('2d');
            let particlesArray = [];
            
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;

            window.addEventListener('resize', () => {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
                initParticles();
            });

            class Particle {
                constructor() {
                    this.x = Math.random() * canvas.width;
                    this.y = Math.random() * canvas.height;
                    this.size = Math.random() * 2 + 0.5;
                    this.speedY = Math.random() * -1 - 0.5;
                    this.speedX = Math.random() * 1 - 0.5;
                    // Random bright colors
                    const colors = ['rgba(255, 0, 127, 0.8)', 'rgba(121, 40, 202, 0.8)', 'rgba(255, 215, 0, 0.8)', 'rgba(255, 255, 255, 0.5)'];
                    this.color = colors[Math.floor(Math.random() * colors.length)];
                }
                update() {
                    this.y += this.speedY;
                    this.x += this.speedX + Math.sin(this.y * 0.01) * 0.5; // Wobble
                    if (this.y < 0) {
                        this.y = canvas.height;
                        this.x = Math.random() * canvas.width;
                    }
                }
                draw() {
                    ctx.fillStyle = this.color;
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                    ctx.fill();
                    // Glow effect
                    ctx.shadowBlur = 10;
                    ctx.shadowColor = this.color;
                }
            }

            function initParticles() {
                particlesArray = [];
                let numberOfParticles = (canvas.width * canvas.height) / 9000;
                for (let i = 0; i < numberOfParticles; i++) {
                    particlesArray.push(new Particle());
                }
            }

            function animateParticles() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                for (let i = 0; i < particlesArray.length; i++) {
                    particlesArray[i].update();
                    particlesArray[i].draw();
                }
                requestAnimationFrame(animateParticles);
            }

            initParticles();
            animateParticles();
        });
    </script>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v8c78df7c7c0f484497ecbca7046644da1771523124516" integrity="sha512-8DS7rgIrAmghBFwoOTujcf6D9rXvH8xm8JQ1Ja01h9QX8EzXldiszufYa4IFfKdLUKTTrnSFXLDkUEOTrZQ8Qg==" data-cf-beacon='{"version": "2024.11.0", "token": "dbb40e3b27694109914698e84f8a92c5", "r":1, "server_timing":{"name":{"cfCacheStatus": true, "cfEdge": true, "cfExtPri": true, "cfL4": true, "cfOrigin": true, "cfSpeedBrain": true}, "location_startswith": null}}' crossorigin=" anonymous"></script>
</body>
</html>
