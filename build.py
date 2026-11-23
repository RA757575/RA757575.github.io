import os

html_content = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="description" content="رامي أمين قاسم - مهندس أمن سيبراني ومطور تطبيقات سحابية وموبايل | طالب مستوى رابع - جامعة تعز">
    <meta name="author" content="Rami Amin Qasem">
    <meta name="theme-color" content="#050811">
    <title>رامي أمين قاسم | Rami Amin Qasem - Cybersecurity Engineer & Full-Stack Developer</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&family=Poppins:wght@300;400;500;600;700;800;900&family=Fira+Code:wght@400;500;600&display=swap" rel="stylesheet">

    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        'cairo': ['Cairo', 'sans-serif'],
                        'poppins': ['Poppins', 'sans-serif'],
                        'mono': ['Fira Code', 'monospace'],
                    },
                    colors: {
                        cyber: {
                            cyan: '#00d4ff',
                            blue: '#1a6fff',
                            purple: '#b026ff',
                            emerald: '#00ff9d',
                            dark: '#050811',
                            card: '#0a1022',
                            cardLight: '#ffffff',
                            border: 'rgba(0, 212, 255, 0.18)',
                        }
                    }
                }
            }
        }
    </script>

    <style>
        :root {
            --bg-dark: #050811;
            --bg-light: #f5f7fb;
            --text-dark: #e6f1ff;
            --text-light: #0f172a;
            --cyber-cyan: #00d4ff;
            --cyber-blue: #1a6fff;
            --cyber-purple: #b026ff;
            --cyber-emerald: #00ff9d;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body {
            font-family: 'Cairo', 'Poppins', sans-serif;
            overflow-x: hidden;
            transition: background-color 0.4s ease, color 0.4s ease;
        }
        html[dir="ltr"] body { font-family: 'Poppins', 'Cairo', sans-serif; }

        body.dark { background-color: var(--bg-dark); color: var(--text-dark); }
        body.light { background-color: var(--bg-light); color: var(--text-light); }

        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: rgba(5, 8, 17, 0.8); }
        ::-webkit-scrollbar-thumb { background: linear-gradient(180deg, var(--cyber-cyan), var(--cyber-blue)); border-radius: 4px; }

        /* Background Animated Orbs */
        .animated-bg { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; overflow: hidden; pointer-events: none; }
        .animated-bg .orb { position: absolute; border-radius: 50%; filter: blur(90px); opacity: 0.35; animation: float 14s ease-in-out infinite; }
        .orb-1 { width: 450px; height: 450px; background: rgba(0, 212, 255, 0.25); top: -120px; right: -100px; }
        .orb-2 { width: 400px; height: 400px; background: rgba(176, 38, 255, 0.2); bottom: -80px; left: -80px; animation-delay: -5s; }
        .orb-3 { width: 350px; height: 350px; background: rgba(0, 255, 157, 0.15); top: 45%; left: 35%; animation-delay: -8s; }
        @keyframes float { 0%, 100% { transform: translateY(0) scale(1); } 50% { transform: translateY(-25px) scale(1.04); } }

        /* Grid Pattern Overlay */
        .cyber-grid {
            position: fixed; inset: 0; pointer-events: none; z-index: -1;
            background-size: 40px 40px;
            background-image: linear-gradient(to right, rgba(0, 212, 255, 0.03) 1px, transparent 1px),
                              linear-gradient(to bottom, rgba(0, 212, 255, 0.03) 1px, transparent 1px);
        }
        body.light .cyber-grid {
            background-image: linear-gradient(to right, rgba(26, 111, 255, 0.04) 1px, transparent 1px),
                              linear-gradient(to bottom, rgba(26, 111, 255, 0.04) 1px, transparent 1px);
        }

        /* Glassmorphism */
        .glass {
            background: rgba(10, 16, 34, 0.72);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            border: 1px solid rgba(0, 212, 255, 0.14);
        }
        body.light .glass {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            border: 1px solid rgba(26, 111, 255, 0.15);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
        }

        .glass-card {
            background: rgba(10, 16, 34, 0.65);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(0, 212, 255, 0.12);
            transition: all 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
        }
        body.light .glass-card {
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(26, 111, 255, 0.12);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
        }
        .glass-card:hover {
            transform: translateY(-6px);
            border-color: rgba(0, 212, 255, 0.45);
            box-shadow: 0 12px 35px rgba(0, 212, 255, 0.15);
        }
        body.light .glass-card:hover {
            box-shadow: 0 14px 35px rgba(26, 111, 255, 0.15);
        }

        /* Neon Glow & Text */
        .neon-border { border-color: var(--cyber-cyan); box-shadow: 0 0 15px rgba(0, 212, 255, 0.3); }
        .neon-text-cyan { text-shadow: 0 0 12px rgba(0, 212, 255, 0.6); }
        .neon-text-green { text-shadow: 0 0 12px rgba(0, 255, 157, 0.6); }

        /* Buttons */
        .btn-cyber {
            background: linear-gradient(135deg, #00d4ff, #1a6fff);
            color: #ffffff;
            font-weight: 700;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }
        .btn-cyber::before {
            content: '';
            position: absolute; top: 0; left: -100%; width: 100%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.35), transparent);
            transition: left 0.5s ease;
        }
        .btn-cyber:hover::before { left: 100%; }
        .btn-cyber:hover { transform: translateY(-3px); box-shadow: 0 8px 25px rgba(0, 212, 255, 0.45); }
        .btn-cyber:active { transform: translateY(0); }

        .btn-outline-cyber {
            background: rgba(0, 212, 255, 0.06);
            border: 1px solid rgba(0, 212, 255, 0.35);
            color: #00d4ff;
            transition: all 0.3s ease;
        }
        body.light .btn-outline-cyber {
            background: rgba(26, 111, 255, 0.06);
            border-color: rgba(26, 111, 255, 0.4);
            color: #1a6fff;
        }
        .btn-outline-cyber:hover {
            background: rgba(0, 212, 255, 0.15);
            border-color: #00d4ff;
            box-shadow: 0 0 20px rgba(0, 212, 255, 0.25);
            transform: translateY(-3px);
        }

        /* Cursor */
        .cursor-dot, .cursor-outline { position: fixed; top: 0; left: 0; transform: translate(-50%, -50%); border-radius: 50%; z-index: 9999; pointer-events: none; }
        .cursor-dot { width: 8px; height: 8px; background: linear-gradient(135deg, var(--cyber-cyan), var(--cyber-emerald)); }
        .cursor-outline { width: 38px; height: 38px; border: 2px solid rgba(0, 212, 255, 0.4); transition: width 0.2s, height 0.2s, border-color 0.2s; }
        .cursor-outline.hover { width: 56px; height: 56px; border-color: var(--cyber-cyan); background: rgba(0, 212, 255, 0.08); }
        @media (max-width: 768px) { .cursor-dot, .cursor-outline { display: none; } }

        /* Scroll Progress */
        .scroll-progress { position: fixed; top: 0; left: 0; height: 3px; background: linear-gradient(90deg, #00d4ff, #1a6fff, #00ff9d); z-index: 1000; transition: width 0.1s; }

        /* Loader */
        .loading-screen { position: fixed; inset: 0; background: var(--bg-dark); z-index: 10000; display: flex; flex-direction: column; justify-content: center; align-items: center; transition: opacity 0.4s ease, visibility 0.4s; }
        .loading-screen.hidden { opacity: 0; visibility: hidden; pointer-events: none; }
        .cyber-spinner {
            width: 65px; height: 65px;
            border: 4px solid rgba(0, 212, 255, 0.15);
            border-top: 4px solid var(--cyber-cyan);
            border-right: 4px solid var(--cyber-emerald);
            border-radius: 50%;
            animation: spin 0.9s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;
        }
        @keyframes spin { 100% { transform: rotate(360deg); } }

        /* Typing cursor */
        .typing-cursor::after { content: '_'; animation: blink 0.8s infinite; color: var(--cyber-cyan); font-weight: 700; }
        @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }

        /* Timeline */
        .timeline-box { position: relative; }
        .timeline-box::before {
            content: ''; position: absolute; top: 0; bottom: 0; width: 2px;
            background: linear-gradient(180deg, var(--cyber-cyan), var(--cyber-blue), transparent);
        }
        html[dir="rtl"] .timeline-box::before { right: 18px; left: auto; }
        html[dir="ltr"] .timeline-box::before { left: 18px; right: auto; }

        /* Terminal styling */
        .terminal-window {
            font-family: 'Fira Code', monospace;
            background: #02050e;
            border: 1px solid rgba(0, 212, 255, 0.25);
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.6), 0 0 30px rgba(0, 212, 255, 0.1);
        }

        /* Filter Tab Active */
        .filter-btn.active {
            background: linear-gradient(135deg, #00d4ff, #1a6fff);
            color: #ffffff;
            box-shadow: 0 4px 18px rgba(0, 212, 255, 0.4);
        }

        /* Project Modal */
        .modal-overlay {
            position: fixed; inset: 0; background: rgba(2, 5, 14, 0.85);
            backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
            z-index: 9999; display: flex; align-items: center; justify-content: center;
            opacity: 0; pointer-events: none; transition: all 0.35s ease;
        }
        .modal-overlay.active { opacity: 1; pointer-events: auto; }
        .modal-content {
            background: #070d1e; border: 1px solid rgba(0, 212, 255, 0.3);
            box-shadow: 0 25px 60px rgba(0,0,0,0.8), 0 0 40px rgba(0, 212, 255, 0.15);
            transform: scale(0.92) translateY(20px); transition: all 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
        }
        body.light .modal-content {
            background: #ffffff; border-color: rgba(26, 111, 255, 0.3);
            box-shadow: 0 25px 60px rgba(0,0,0,0.15);
        }
        .modal-overlay.active .modal-content { transform: scale(1) translateY(0); }

        /* Floating action buttons */
        .fab-container { position: fixed; bottom: 25px; z-index: 40; display: flex; gap: 12px; }
        html[dir="rtl"] .fab-container { left: 25px; }
        html[dir="ltr"] .fab-container { right: 25px; }
        .fab-action-btn {
            width: 48px; height: 48px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            background: rgba(10, 16, 34, 0.8);
            border: 1px solid rgba(0, 212, 255, 0.3);
            color: var(--cyber-cyan);
            backdrop-filter: blur(10px);
            cursor: pointer; transition: all 0.3s ease;
            box-shadow: 0 6px 20px rgba(0, 212, 255, 0.2);
        }
        body.light .fab-action-btn {
            background: rgba(255, 255, 255, 0.9);
            border-color: rgba(26, 111, 255, 0.3);
            color: var(--cyber-blue);
            box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        }
        .fab-action-btn:hover { transform: translateY(-4px) scale(1.05); box-shadow: 0 8px 25px rgba(0, 212, 255, 0.4); }

        /* Mobile Drawer */
        .mobile-drawer {
            position: fixed; top: 0; bottom: 0; width: 300px; max-width: 85vw;
            background: rgba(6, 11, 26, 0.96); backdrop-filter: blur(25px);
            z-index: 999; display: flex; flex-direction: column;
            transition: transform 0.35s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 0 50px rgba(0,0,0,0.7);
        }
        body.light .mobile-drawer { background: rgba(255, 255, 255, 0.97); box-shadow: 0 0 40px rgba(0,0,0,0.12); }
        html[dir="rtl"] .mobile-drawer { right: 0; transform: translateX(100%); border-left: 1px solid rgba(0, 212, 255, 0.15); }
        html[dir="rtl"] .mobile-drawer.open { transform: translateX(0); }
        html[dir="ltr"] .mobile-drawer { left: 0; transform: translateX(-100%); border-right: 1px solid rgba(0, 212, 255, 0.15); }
        html[dir="ltr"] .mobile-drawer.open { transform: translateX(0); }

        .drawer-overlay {
            position: fixed; inset: 0; background: rgba(0,0,0,0.6);
            backdrop-filter: blur(4px); z-index: 998; opacity: 0; pointer-events: none;
            transition: opacity 0.35s ease;
        }
        .drawer-overlay.open { opacity: 1; pointer-events: auto; }
    </style>
</head>
<body class="dark">

    <!-- Loading Screen -->
    <div class="loading-screen" id="loadingScreen">
        <div class="cyber-spinner mb-4"></div>
        <div class="text-center font-mono">
            <span class="text-cyber-cyan text-lg font-bold tracking-widest">[SYSTEM_INITIALIZATION]</span>
            <p class="text-xs text-gray-400 mt-1" data-i18n="loader_status">جارٍ تحميل محفظة رامي أمين قاسم...</p>
        </div>
    </div>

    <!-- Scroll Progress -->
    <div class="scroll-progress" id="scrollProgress"></div>

    <!-- Custom Cursor -->
    <div class="cursor-dot" id="cursorDot"></div>
    <div class="cursor-outline" id="cursorOutline"></div>

    <!-- Animated Background -->
    <div class="animated-bg">
        <div class="orb orb-1"></div>
        <div class="orb orb-2"></div>
        <div class="orb orb-3"></div>
    </div>
    <div class="cyber-grid"></div>

    <!-- Particles Canvas -->
    <canvas id="particles-canvas" style="position:fixed;top:0;left:0;width:100%;height:100%;z-index:-1;pointer-events:none;"></canvas>

    <!-- ================= NAVBAR ================= -->
    <nav class="fixed top-0 left-0 w-full z-50 glass" id="navbar">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 py-3.5 flex justify-between items-center">
            <a href="#hero" class="flex items-center gap-2 group">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-cyber-cyan via-cyber-blue to-cyber-purple flex items-center justify-center text-white font-mono font-black text-lg shadow-lg shadow-cyber-cyan/20 group-hover:scale-105 transition-transform">
                    <i class="fas fa-shield-halved text-sm"></i>
                </div>
                <div class="flex flex-col">
                    <span class="font-bold text-lg leading-tight tracking-wide font-mono bg-gradient-to-r from-cyber-cyan to-cyber-blue bg-clip-text text-transparent">
                        &lt;Rami.Sec/&gt;
                    </span>
                    <span class="text-[10px] text-gray-400 font-cairo tracking-wider" data-i18n="nav_role_sub">أمن سيبراني & هندسة برمجيات</span>
                </div>
            </a>

            <!-- Desktop Nav Links -->
            <div class="hidden lg:flex items-center gap-7">
                <a href="#about" class="nav-link text-sm font-semibold hover:text-cyber-cyan transition-colors" data-i18n="nav_about">عنّي</a>
                <a href="#academics" class="nav-link text-sm font-semibold hover:text-cyber-cyan transition-colors" data-i18n="nav_academics">التخصص والجامعة</a>
                <a href="#skills" class="nav-link text-sm font-semibold hover:text-cyber-cyan transition-colors" data-i18n="nav_skills">المهارات التقنية</a>
                <a href="#projects" class="nav-link text-sm font-semibold hover:text-cyber-cyan transition-colors" data-i18n="nav_projects">المشاريع والأبحاث</a>
                <a href="#terminal" class="nav-link text-sm font-semibold hover:text-cyber-cyan transition-colors" data-i18n="nav_terminal">الطرفية التفاعلية</a>
                <a href="#journey" class="nav-link text-sm font-semibold hover:text-cyber-cyan transition-colors" data-i18n="nav_journey">المسيرة</a>
                <a href="#contact" class="nav-link text-sm font-semibold hover:text-cyber-cyan transition-colors" data-i18n="nav_contact">تواصل معي</a>
            </div>

            <!-- Controls (Theme + Lang + Menu) -->
            <div class="flex items-center gap-3">
                <button class="w-10 h-10 rounded-xl glass flex items-center justify-center hover:border-cyber-cyan transition-all lang-toggle" aria-label="Toggle language">
                    <span class="lang-label text-xs font-bold text-cyber-cyan font-mono">EN</span>
                </button>
                <button class="w-10 h-10 rounded-xl glass flex items-center justify-center hover:border-cyber-cyan transition-all theme-toggle" aria-label="Toggle theme">
                    <i class="fas fa-sun text-yellow-400 theme-icon"></i>
                </button>
                <button class="lg:hidden w-10 h-10 rounded-xl glass flex items-center justify-center text-cyber-cyan" id="mobileMenuBtn" aria-label="Open menu">
                    <i class="fas fa-bars-staggered"></i>
                </button>
            </div>
        </div>
    </nav>

    <!-- Mobile Drawer Overlay -->
    <div class="drawer-overlay" id="drawerOverlay"></div>

    <!-- Mobile Drawer -->
    <aside class="mobile-drawer" id="mobileDrawer">
        <div class="p-6 border-b border-cyber-cyan/15 flex justify-between items-center">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-cyber-cyan to-cyber-blue flex items-center justify-center text-white">
                    <i class="fas fa-user-shield"></i>
                </div>
                <div>
                    <h3 class="font-bold text-sm">رامي أمين قاسم</h3>
                    <p class="text-[11px] text-cyber-cyan font-mono" data-i18n="drawer_status">مستوى رابع - أمن سيبراني</p>
                </div>
            </div>
            <button class="w-9 h-9 rounded-lg glass flex items-center justify-center text-gray-400 hover:text-white" id="closeDrawerBtn">
                <i class="fas fa-xmark"></i>
            </button>
        </div>
        <div class="p-6 flex flex-col gap-4 flex-1 overflow-y-auto font-medium text-sm">
            <a href="#about" class="drawer-link flex items-center gap-3 py-2 text-gray-300 hover:text-cyber-cyan"><i class="fas fa-user-astronaut text-cyber-cyan w-5"></i><span data-i18n="nav_about">عنّي</span></a>
            <a href="#academics" class="drawer-link flex items-center gap-3 py-2 text-gray-300 hover:text-cyber-cyan"><i class="fas fa-graduation-cap text-cyber-blue w-5"></i><span data-i18n="nav_academics">التخصص والجامعة</span></a>
            <a href="#skills" class="drawer-link flex items-center gap-3 py-2 text-gray-300 hover:text-cyber-cyan"><i class="fas fa-microchip text-cyber-purple w-5"></i><span data-i18n="nav_skills">المهارات التقنية</span></a>
            <a href="#projects" class="drawer-link flex items-center gap-3 py-2 text-gray-300 hover:text-cyber-cyan"><i class="fas fa-folder-tree text-cyber-emerald w-5"></i><span data-i18n="nav_projects">المشاريع والأبحاث</span></a>
            <a href="#terminal" class="drawer-link flex items-center gap-3 py-2 text-gray-300 hover:text-cyber-cyan"><i class="fas fa-terminal text-cyber-cyan w-5"></i><span data-i18n="nav_terminal">الطرفية التفاعلية</span></a>
            <a href="#journey" class="drawer-link flex items-center gap-3 py-2 text-gray-300 hover:text-cyber-cyan"><i class="fas fa-timeline text-cyber-purple w-5"></i><span data-i18n="nav_journey">المسيرة</span></a>
            <a href="#contact" class="drawer-link flex items-center gap-3 py-2 text-gray-300 hover:text-cyber-cyan"><i class="fas fa-envelope text-cyber-blue w-5"></i><span data-i18n="nav_contact">تواصل معي</span></a>
        </div>
        <div class="p-6 border-t border-cyber-cyan/15 flex justify-center gap-4 text-lg">
            <a href="https://github.com/RA757575" target="_blank" class="w-10 h-10 rounded-xl glass flex items-center justify-center hover:text-cyber-cyan"><i class="fab fa-github"></i></a>
            <a href="mailto:ramyamyn41@gmail.com" class="w-10 h-10 rounded-xl glass flex items-center justify-center hover:text-cyber-cyan"><i class="fas fa-envelope"></i></a>
        </div>
    </aside>

    <!-- Floating Action Buttons -->
    <div class="fab-container">
        <button class="fab-action-btn theme-toggle" title="تبديل المظهر"><i class="fas fa-sun theme-icon"></i></button>
        <button class="fab-action-btn lang-toggle" title="تبديل اللغة"><span class="lang-label font-bold text-xs">EN</span></button>
        <a href="#hero" class="fab-action-btn" title="إلى الأعلى"><i class="fas fa-chevron-up"></i></a>
    </div>

    <!-- ================= HERO SECTION ================= -->
    <section id="hero" class="min-h-screen pt-28 pb-16 px-4 sm:px-6 lg:px-8 flex items-center relative">
        <div class="max-w-7xl mx-auto w-full grid lg:grid-cols-12 gap-12 items-center">
            <div class="lg:col-span-7 space-y-6 text-center lg:text-right rtl:lg:text-right ltr:lg:text-left">
                <!-- Academic Status Badge -->
                <div class="inline-flex items-center gap-2.5 px-4 py-2 rounded-full glass border border-cyber-emerald/40 text-xs sm:text-sm font-semibold">
                    <span class="w-2.5 h-2.5 rounded-full bg-cyber-emerald animate-pulse"></span>
                    <span class="text-cyber-emerald font-mono font-bold" data-i18n="hero_status_badge">مستوى رابع (سنة التخرج) · قسم الأمن السيبراني · جامعة تعز</span>
                </div>

                <h1 class="text-3xl sm:text-5xl lg:text-6xl font-extrabold leading-tight">
                    <span class="block text-gray-300 text-lg sm:text-2xl font-normal mb-2" data-i18n="hero_greeting">مرحباً بك، أنا</span>
                    <span class="bg-gradient-to-r from-white via-cyber-cyan to-cyber-blue bg-clip-text text-transparent">
                        رامي أمين قاسم علي سعيد
                    </span>
                </h1>

                <!-- Dynamic Typing -->
                <div class="h-10 sm:h-12 flex items-center justify-center lg:justify-start font-mono text-lg sm:text-2xl text-cyber-cyan font-bold">
                    <span class="text-gray-400 text-sm sm:text-base mr-2 rtl:ml-2">&gt;</span>
                    <span id="typingText"></span>
                    <span class="typing-cursor"></span>
                </div>

                <p class="text-gray-300 dark:text-gray-300 text-sm sm:text-base leading-relaxed max-w-2xl mx-auto lg:mx-0" data-i18n="hero_desc">
                    مهندس أمن سيبراني ومطور أنظمة وتطبيقات متكاملة. أجمع بين الرؤية الدفاعية المتقدمة (SOC، كشف الشذوذ بالـ AI، ومراقبة الشبكات) وبين هندسة البرمجيات المتينة باستخدام Flutter (Clean Architecture) والأنظمة السحابية الموزعة (Supabase, PostgreSQL RLS, Firebase). شغفي بناء أنظمة برمجية آمنة وموثوقة من سطر الكود الأول حتى البنية التحتية.
                </p>

                <!-- Actions -->
                <div class="flex flex-wrap gap-4 justify-center lg:justify-start pt-2">
                    <a href="#projects" class="btn-cyber px-6 py-3.5 rounded-xl flex items-center gap-2.5 text-sm sm:text-base shadow-lg shadow-cyber-cyan/20">
                        <i class="fas fa-shield-virus"></i>
                        <span data-i18n="btn_view_projects">استكشف المشاريع والأبحاث</span>
                    </a>
                    <a href="#terminal" class="btn-outline-cyber px-6 py-3.5 rounded-xl flex items-center gap-2.5 text-sm sm:text-base">
                        <i class="fas fa-terminal"></i>
                        <span data-i18n="btn_try_terminal">تشغيل الطرفية السيبرانية</span>
                    </a>
                    <a href="mailto:ramyamyn41@gmail.com" class="px-5 py-3.5 rounded-xl glass hover:border-cyber-cyan transition-all flex items-center gap-2 text-sm text-gray-300 hover:text-white">
                        <i class="fas fa-envelope text-cyber-cyan"></i>
                        <span data-i18n="btn_contact_me">تواصل مباشر</span>
                    </a>
                </div>

                <!-- Fast Info Badges -->
                <div class="pt-6 grid grid-cols-2 sm:grid-cols-4 gap-3 text-center font-mono">
                    <div class="glass p-3 rounded-xl">
                        <span class="block text-xl sm:text-2xl font-black text-cyber-cyan">مستوى 4</span>
                        <span class="text-[11px] text-gray-400" data-i18n="metric_level">جامعة تعز</span>
                    </div>
                    <div class="glass p-3 rounded-xl">
                        <span class="block text-xl sm:text-2xl font-black text-cyber-emerald">+10</span>
                        <span class="text-[11px] text-gray-400" data-i18n="metric_projects">مشاريع ومختبرات</span>
                    </div>
                    <div class="glass p-3 rounded-xl">
                        <span class="block text-xl sm:text-2xl font-black text-cyber-purple">2</span>
                        <span class="text-[11px] text-gray-400" data-i18n="metric_ai">نماذج AI وبحوث</span>
                    </div>
                    <div class="glass p-3 rounded-xl">
                        <span class="block text-xl sm:text-2xl font-black text-cyber-blue">100%</span>
                        <span class="text-[11px] text-gray-400" data-i18n="metric_security">تصميم دفاعي</span>
                    </div>
                </div>
            </div>

            <!-- Hero Graphic / Interactive Cyber Card -->
            <div class="lg:col-span-5">
                <div class="glass-card rounded-2xl p-6 relative overflow-hidden border border-cyber-cyan/30">
                    <div class="flex items-center justify-between pb-4 mb-4 border-b border-cyber-cyan/15 font-mono text-xs">
                        <div class="flex items-center gap-2">
                            <span class="w-3 h-3 rounded-full bg-red-500/80 inline-block"></span>
                            <span class="w-3 h-3 rounded-full bg-yellow-500/80 inline-block"></span>
                            <span class="w-3 h-3 rounded-full bg-green-500/80 inline-block"></span>
                            <span class="text-gray-400 ml-2">cyber-telemetry-feed.log</span>
                        </div>
                        <span class="text-cyber-emerald flex items-center gap-1.5"><i class="fas fa-circle text-[8px] animate-ping"></i> LIVE</span>
                    </div>

                    <!-- Telemetry Items -->
                    <div class="space-y-3 font-mono text-xs">
                        <div class="p-2.5 rounded-lg bg-cyber-dark/80 border border-cyber-cyan/10">
                            <div class="flex justify-between text-gray-400">
                                <span>[DEFENSE] SIEM ELK Stack</span>
                                <span class="text-cyber-emerald">ACTIVE</span>
                            </div>
                            <p class="text-cyber-cyan mt-1 text-[11px]">300+ Event Logs Parsed via Docker Compose</p>
                        </div>

                        <div class="p-2.5 rounded-lg bg-cyber-dark/80 border border-cyber-cyan/10">
                            <div class="flex justify-between text-gray-400">
                                <span>[GRAD_RESEARCH] Digital Twin IDS</span>
                                <span class="text-cyber-purple">PROPOSED</span>
                            </div>
                            <p class="text-gray-300 mt-1 text-[11px]">Hybrid XAI (Autoencoder + IsoForest + LSTM + SHAP)</p>
                        </div>

                        <div class="p-2.5 rounded-lg bg-cyber-dark/80 border border-cyber-cyan/10">
                            <div class="flex justify-between text-gray-400">
                                <span>[SUH] Smart University Handbook</span>
                                <span class="text-cyber-cyan">COMPLETED</span>
                            </div>
                            <p class="text-gray-300 mt-1 text-[11px]">Fine-Tuned LLaMA 3 AI + Flutter Client + Firebase</p>
                        </div>

                        <div class="p-2.5 rounded-lg bg-cyber-dark/80 border border-cyber-cyan/10">
                            <div class="flex justify-between text-gray-400">
                                <span>[APP] Souq Yemen Multi-Vendor</span>
                                <span class="text-cyber-emerald">OFFLINE-FIRST</span>
                            </div>
                            <p class="text-gray-300 mt-1 text-[11px]">Clean Architecture, Hive Cache, Supabase PostgreSQL RLS</p>
                        </div>
                    </div>

                    <!-- Footer Info -->
                    <div class="mt-5 pt-3 border-t border-cyber-cyan/15 flex items-center justify-between text-xs font-mono text-gray-400">
                        <span>Host: Taiz Univ · Cybersecurity</span>
                        <a href="https://github.com/RA757575" target="_blank" class="text-cyber-cyan hover:underline flex items-center gap-1">
                            <span>github.com/RA757575</span> <i class="fas fa-arrow-up-right-from-square text-[10px]"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ================= ABOUT ME SECTION ================= -->
    <section id="about" class="py-20 px-4 sm:px-6 lg:px-8 relative border-t border-cyber-cyan/10">
        <div class="max-w-7xl mx-auto">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <span class="text-cyber-cyan font-mono text-sm tracking-wider uppercase font-bold" data-i18n="about_badge">// من أنا ورؤيتي الهندسية</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold mt-2" data-i18n="about_title">الأمن المضمن وهندسة النظم</h2>
            </div>

            <div class="grid lg:grid-cols-12 gap-10 items-center">
                <div class="lg:col-span-6 space-y-5 text-sm sm:text-base text-gray-300 leading-relaxed">
                    <p data-i18n="about_p1">
                        أنا <strong class="text-white">رامي أمين قاسم علي سعيد</strong>، مهندس أمن سيبراني ومطور أنظمة برمجية في السنة النهائية (مستوى رابع) بكلية العلوم التطبيقية في جامعة تعز.
                    </p>
                    <p data-i18n="about_p2">
                        خلال مسيرتي الأكاديمية والعملية، ركزتُ على دمج مفهوم <span class="text-cyber-cyan font-semibold">Security by Design</span>؛ حيث لا يُعامل الأمان كطبقة إضافية بعد انتهاء البرمجة، بل كحجر زاوية يبدأ من تصميم قاعدة البيانات، وفصل الطبقات بالمعمارية النظيفة، وضبط أمان السحابة بـ RLS، وحتى تطبيق الذكاء الاصطناعي للتنبؤ بالهجمات وكشف التسلل.
                    </p>
                    <p data-i18n="about_p3">
                        قمت بتطوير وإطلاق مشاريع حقيقية كبرى تشمل منصات التجارة الإلكترونية ذات المعمارية النظيفة مع دعم العمل دون اتصال، وتدريب نماذج ذكاء اصطناعي لغوية (LLaMA 3) لدعم الخدمات الجامعية، وإجراء أبحاث متقدمة في اكتشاف الهجمات بالتوأم الرقمي والذكاء الاصطناعي القابل للتفسير.
                    </p>
                </div>

                <div class="lg:col-span-6 grid sm:grid-cols-2 gap-4">
                    <div class="glass-card p-5 rounded-2xl">
                        <div class="w-10 h-10 rounded-xl bg-cyber-cyan/15 text-cyber-cyan flex items-center justify-center text-lg mb-3">
                            <i class="fas fa-university"></i>
                        </div>
                        <h4 class="font-bold text-white text-sm" data-i18n="about_card1_title">الجامعة والمستوى</h4>
                        <p class="text-xs text-gray-400 mt-1" data-i18n="about_card1_desc">جامعة تعز · كلية العلوم التطبيقية · قسم الأمن السيبراني (مستوى رابع / تخرج).</p>
                    </div>

                    <div class="glass-card p-5 rounded-2xl">
                        <div class="w-10 h-10 rounded-xl bg-cyber-emerald/15 text-cyber-emerald flex items-center justify-center text-lg mb-3">
                            <i class="fas fa-user-ninja"></i>
                        </div>
                        <h4 class="font-bold text-white text-sm" data-i18n="about_card2_title">التحليل الأمني والـ SOC</h4>
                        <p class="text-xs text-gray-400 mt-1" data-i18n="about_card2_desc">محلل مركز عمليات أمني، هندسة الكشف عن التهديدات، وتجميع سجلات SIEM.</p>
                    </div>

                    <div class="glass-card p-5 rounded-2xl">
                        <div class="w-10 h-10 rounded-xl bg-cyber-blue/15 text-cyber-blue flex items-center justify-center text-lg mb-3">
                            <i class="fas fa-cubes"></i>
                        </div>
                        <h4 class="font-bold text-white text-sm" data-i18n="about_card3_title">Clean Architecture</h4>
                        <p class="text-xs text-gray-400 mt-1" data-i18n="about_card3_desc">معمارية برمجية متقدمة في Flutter تضمن فصل منطق العمل عن واجهات العرض.</p>
                    </div>

                    <div class="glass-card p-5 rounded-2xl">
                        <div class="w-10 h-10 rounded-xl bg-cyber-purple/15 text-cyber-purple flex items-center justify-center text-lg mb-3">
                            <i class="fas fa-network-wired"></i>
                        </div>
                        <h4 class="font-bold text-white text-sm" data-i18n="about_card4_title">هندسة الشبكات والسحابة</h4>
                        <p class="text-xs text-gray-400 mt-1" data-i18n="about_card4_desc">محاكاة عبر GNS3 و Packet Tracer، وتكوين راوترات MikroTik وحاويات Docker.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ================= ACADEMICS & PILLARS SECTION ================= -->
    <section id="academics" class="py-20 px-4 sm:px-6 lg:px-8 relative border-t border-cyber-cyan/10">
        <div class="max-w-7xl mx-auto">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <span class="text-cyber-cyan font-mono text-sm tracking-wider uppercase font-bold" data-i18n="academics_badge">// المسار الأكاديمي والتخصص</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold mt-2" data-i18n="academics_title">جامعة تعز · كلية العلوم التطبيقية</h2>
                <p class="text-gray-400 mt-3 text-sm sm:text-base" data-i18n="academics_desc">
                    طالب في السنة النهائية (مستوى رابع) بقسم الأمن السيبراني. دراسة أكاديمية وتطبيقية مكثفة تربط بين النظريات العميقة للأمن السيبراني، البروتوكولات الشبكية، وبناء البرمجيات المتينة.
                </p>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- Pillar 1 -->
                <div class="glass-card rounded-2xl p-6 border-t-2 border-t-cyber-cyan">
                    <div class="w-12 h-12 rounded-xl bg-cyber-cyan/15 text-cyber-cyan flex items-center justify-center text-xl mb-4">
                        <i class="fas fa-shield-halved"></i>
                    </div>
                    <h3 class="text-lg font-bold mb-2" data-i18n="pillar1_title">أمن العمليات و الـ SOC</h3>
                    <p class="text-xs text-gray-400 leading-relaxed" data-i18n="pillar1_desc">
                        تحليل السجلات ومراقبة التهديدات باستخدام ELK Stack في Docker، رصد حزم البيانات عبر Zeek و Suricata، واختبار الثغرات باستخدام Kali Linux و OWASP ZAP.
                    </p>
                    <div class="mt-4 flex flex-wrap gap-1.5 font-mono text-[11px]">
                        <span class="px-2 py-0.5 rounded bg-cyber-cyan/10 text-cyber-cyan">SIEM</span>
                        <span class="px-2 py-0.5 rounded bg-cyber-cyan/10 text-cyber-cyan">ELK</span>
                        <span class="px-2 py-0.5 rounded bg-cyber-cyan/10 text-cyber-cyan">Zeek</span>
                    </div>
                </div>

                <!-- Pillar 2 -->
                <div class="glass-card rounded-2xl p-6 border-t-2 border-t-cyber-blue">
                    <div class="w-12 h-12 rounded-xl bg-cyber-blue/15 text-cyber-blue flex items-center justify-center text-xl mb-4">
                        <i class="fas fa-mobile-screen-button"></i>
                    </div>
                    <h3 class="text-lg font-bold mb-2" data-i18n="pillar2_title">تطبيقات الموبايل المتقدمة</h3>
                    <p class="text-xs text-gray-400 leading-relaxed" data-i18n="pillar2_desc">
                        تطوير تطبيقات Flutter متعددة المنصات بالاعتماد على Clean Architecture، التخزين المحلي Offline-First عبر Hive، وإدارة الحالة وحقن الاعتماديات باحترافية.
                    </p>
                    <div class="mt-4 flex flex-wrap gap-1.5 font-mono text-[11px]">
                        <span class="px-2 py-0.5 rounded bg-cyber-blue/10 text-cyber-blue">Flutter</span>
                        <span class="px-2 py-0.5 rounded bg-cyber-blue/10 text-cyber-blue">Hive</span>
                        <span class="px-2 py-0.5 rounded bg-cyber-blue/10 text-cyber-blue">Dart</span>
                    </div>
                </div>

                <!-- Pillar 3 -->
                <div class="glass-card rounded-2xl p-6 border-t-2 border-t-cyber-purple">
                    <div class="w-12 h-12 rounded-xl bg-cyber-purple/15 text-cyber-purple flex items-center justify-center text-xl mb-4">
                        <i class="fas fa-cloud"></i>
                    </div>
                    <h3 class="text-lg font-bold mb-2" data-i18n="pillar3_title">الأنظمة السحابية و SaaS</h3>
                    <p class="text-xs text-gray-400 leading-relaxed" data-i18n="pillar3_desc">
                        تصميم وتطوير منصات SaaS متعددة المستأجرين (Multi-Tenant) مع عزل بيانات صارم عبر PostgreSQL RLS، واجهات React و TanStack، وتكاملات Supabase و Firebase.
                    </p>
                    <div class="mt-4 flex flex-wrap gap-1.5 font-mono text-[11px]">
                        <span class="px-2 py-0.5 rounded bg-cyber-purple/10 text-cyber-purple">PostgreSQL</span>
                        <span class="px-2 py-0.5 rounded bg-cyber-purple/10 text-cyber-purple">RLS</span>
                        <span class="px-2 py-0.5 rounded bg-cyber-purple/10 text-cyber-purple">SaaS</span>
                    </div>
                </div>

                <!-- Pillar 4 -->
                <div class="glass-card rounded-2xl p-6 border-t-2 border-t-cyber-emerald">
                    <div class="w-12 h-12 rounded-xl bg-cyber-emerald/15 text-cyber-emerald flex items-center justify-center text-xl mb-4">
                        <i class="fas fa-brain"></i>
                    </div>
                    <h3 class="text-lg font-bold mb-2" data-i18n="pillar4_title">الذكاء الاصطناعي والأبحاث</h3>
                    <p class="text-xs text-gray-400 leading-relaxed" data-i18n="pillar4_desc">
                        تخصيص وتدريب النماذج اللغوية الكبيرة (LLaMA 3 Fine-Tuning)، وتطبيق تقنيات الذكاء الاصطناعي القابل للتفسير (XAI / SHAP) والتعلم العميق في كشف التسلل.
                    </p>
                    <div class="mt-4 flex flex-wrap gap-1.5 font-mono text-[11px]">
                        <span class="px-2 py-0.5 rounded bg-cyber-emerald/10 text-cyber-emerald">LLaMA 3</span>
                        <span class="px-2 py-0.5 rounded bg-cyber-emerald/10 text-cyber-emerald">SHAP</span>
                        <span class="px-2 py-0.5 rounded bg-cyber-emerald/10 text-cyber-emerald">XAI</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ================= SKILLS MATRIX SECTION ================= -->
    <section id="skills" class="py-20 px-4 sm:px-6 lg:px-8 relative border-t border-cyber-cyan/10">
        <div class="max-w-7xl mx-auto">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <span class="text-cyber-cyan font-mono text-sm tracking-wider uppercase font-bold" data-i18n="skills_badge">// مصفوفة القدرات والخبرات</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold mt-2" data-i18n="skills_title">الترسانة التقنية والأدوات المتقنة</h2>
                <p class="text-gray-400 mt-3 text-sm sm:text-base" data-i18n="skills_desc">
                    مهارات عملية مطبقة في مشاريع ومختبرات حقيقية تشمل الأمن الدفاعي، الأطر السحابية، لغات البرمجة، وقواعد البيانات.
                </p>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Skill Group 1 -->
                <div class="glass-card rounded-2xl p-7">
                    <div class="flex items-center gap-3 mb-6">
                        <div class="w-12 h-12 rounded-xl bg-cyber-cyan/15 text-cyber-cyan flex items-center justify-center text-xl">
                            <i class="fas fa-lock"></i>
                        </div>
                        <div>
                            <h3 class="font-bold text-lg" data-i18n="skill_g1_title">الأمن السيبراني والـ SOC</h3>
                            <span class="text-xs text-gray-400 font-mono">Defensive & SecOps</span>
                        </div>
                    </div>
                    <div class="space-y-4 font-mono text-xs">
                        <div>
                            <div class="flex justify-between mb-1"><span>SIEM / ELK Stack (Docker)</span><span class="text-cyber-cyan">92%</span></div>
                            <div class="w-full h-2 rounded-full bg-gray-700/50 overflow-hidden"><div class="h-full bg-gradient-to-r from-cyber-cyan to-cyber-blue rounded-full" style="width: 92%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between mb-1"><span>Network Monitoring (Zeek / Suricata)</span><span class="text-cyber-cyan">88%</span></div>
                            <div class="w-full h-2 rounded-full bg-gray-700/50 overflow-hidden"><div class="h-full bg-gradient-to-r from-cyber-cyan to-cyber-blue rounded-full" style="width: 88%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between mb-1"><span>Pen-testing (Kali Linux / Metasploit)</span><span class="text-cyber-cyan">85%</span></div>
                            <div class="w-full h-2 rounded-full bg-gray-700/50 overflow-hidden"><div class="h-full bg-gradient-to-r from-cyber-cyan to-cyber-blue rounded-full" style="width: 85%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between mb-1"><span>App Sec (OWASP ZAP / SonarQube)</span><span class="text-cyber-cyan">90%</span></div>
                            <div class="w-full h-2 rounded-full bg-gray-700/50 overflow-hidden"><div class="h-full bg-gradient-to-r from-cyber-cyan to-cyber-blue rounded-full" style="width: 90%"></div></div>
                        </div>
                    </div>
                </div>

                <!-- Skill Group 2 -->
                <div class="glass-card rounded-2xl p-7">
                    <div class="flex items-center gap-3 mb-6">
                        <div class="w-12 h-12 rounded-xl bg-cyber-blue/15 text-cyber-blue flex items-center justify-center text-xl">
                            <i class="fas fa-code"></i>
                        </div>
                        <div>
                            <h3 class="font-bold text-lg" data-i18n="skill_g2_title">تطوير البرمجيات والموبايل</h3>
                            <span class="text-xs text-gray-400 font-mono">Mobile & Frontend</span>
                        </div>
                    </div>
                    <div class="space-y-4 font-mono text-xs">
                        <div>
                            <div class="flex justify-between mb-1"><span>Flutter & Dart (Clean Architecture)</span><span class="text-cyber-blue">94%</span></div>
                            <div class="w-full h-2 rounded-full bg-gray-700/50 overflow-hidden"><div class="h-full bg-gradient-to-r from-cyber-blue to-cyber-purple rounded-full" style="width: 94%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between mb-1"><span>Offline-First (Hive & Sync)</span><span class="text-cyber-blue">90%</span></div>
                            <div class="w-full h-2 rounded-full bg-gray-700/50 overflow-hidden"><div class="h-full bg-gradient-to-r from-cyber-blue to-cyber-purple rounded-full" style="width: 90%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between mb-1"><span>React / TypeScript / Tailwind</span><span class="text-cyber-blue">88%</span></div>
                            <div class="w-full h-2 rounded-full bg-gray-700/50 overflow-hidden"><div class="h-full bg-gradient-to-r from-cyber-blue to-cyber-purple rounded-full" style="width: 88%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between mb-1"><span>C++ & Data Structures (Abu-Hadhoud)</span><span class="text-cyber-blue">91%</span></div>
                            <div class="w-full h-2 rounded-full bg-gray-700/50 overflow-hidden"><div class="h-full bg-gradient-to-r from-cyber-blue to-cyber-purple rounded-full" style="width: 91%"></div></div>
                        </div>
                    </div>
                </div>

                <!-- Skill Group 3 -->
                <div class="glass-card rounded-2xl p-7">
                    <div class="flex items-center gap-3 mb-6">
                        <div class="w-12 h-12 rounded-xl bg-cyber-emerald/15 text-cyber-emerald flex items-center justify-center text-xl">
                            <i class="fas fa-server"></i>
                        </div>
                        <div>
                            <h3 class="font-bold text-lg" data-i18n="skill_g3_title">السحابة وقواعد البيانات والشبكات</h3>
                            <span class="text-xs text-gray-400 font-mono">Backend, Cloud & Infra</span>
                        </div>
                    </div>
                    <div class="space-y-4 font-mono text-xs">
                        <div>
                            <div class="flex justify-between mb-1"><span>Supabase & PostgreSQL (RLS)</span><span class="text-cyber-emerald">93%</span></div>
                            <div class="w-full h-2 rounded-full bg-gray-700/50 overflow-hidden"><div class="h-full bg-gradient-to-r from-cyber-emerald to-cyber-cyan rounded-full" style="width: 93%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between mb-1"><span>Firebase (Firestore, Auth, Functions)</span><span class="text-cyber-emerald">90%</span></div>
                            <div class="w-full h-2 rounded-full bg-gray-700/50 overflow-hidden"><div class="h-full bg-gradient-to-r from-cyber-emerald to-cyber-cyan rounded-full" style="width: 90%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between mb-1"><span>GNS3 / Cisco Packet Tracer / MikroTik</span><span class="text-cyber-emerald">89%</span></div>
                            <div class="w-full h-2 rounded-full bg-gray-700/50 overflow-hidden"><div class="h-full bg-gradient-to-r from-cyber-emerald to-cyber-cyan rounded-full" style="width: 89%"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between mb-1"><span>Docker & Containerization</span><span class="text-cyber-emerald">87%</span></div>
                            <div class="w-full h-2 rounded-full bg-gray-700/50 overflow-hidden"><div class="h-full bg-gradient-to-r from-cyber-emerald to-cyber-cyan rounded-full" style="width: 87%"></div></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ================= FEATURED PROJECTS SECTION ================= -->
    <section id="projects" class="py-20 px-4 sm:px-6 lg:px-8 relative border-t border-cyber-cyan/10">
        <div class="max-w-7xl mx-auto">
            <div class="text-center max-w-3xl mx-auto mb-12">
                <span class="text-cyber-cyan font-mono text-sm tracking-wider uppercase font-bold" data-i18n="projects_badge">// معرض المشاريع والابتكارات</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold mt-2" data-i18n="projects_title">أبرز الأبحاث والأنظمة المنفذة</h2>
                <p class="text-gray-400 mt-3 text-sm sm:text-base" data-i18n="projects_desc">
                    مشاريع متكاملة صُممت وطُبقت بأعلى المعايير الهندسية والأمنية، يمكن النقر على أي مشروع لاستعراض التفاصيل المعمارية والتقنية.
                </p>
            </div>

            <!-- Filter Tabs -->
            <div class="flex flex-wrap justify-center gap-2.5 mb-12">
                <button class="filter-btn active px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold glass transition-all" data-filter="all" data-i18n="filter_all">الكل</button>
                <button class="filter-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold glass transition-all" data-filter="sec" data-i18n="filter_sec">الأمن السيبراني & SOC</button>
                <button class="filter-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold glass transition-all" data-filter="mobile" data-i18n="filter_mobile">تطبيقات الموبايل (Flutter)</button>
                <button class="filter-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold glass transition-all" data-filter="cloud" data-i18n="filter_cloud">الأنظمة السحابية & SaaS</button>
                <button class="filter-btn px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold glass transition-all" data-filter="ai" data-i18n="filter_ai">الأبحاث والـ AI</button>
            </div>

            <!-- Projects Grid -->
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-7" id="projectsContainer">

                <!-- Project 1: Smart University Handbook -->
                <div class="project-item glass-card rounded-2xl overflow-hidden flex flex-col" data-category="mobile ai">
                    <div class="p-6 bg-gradient-to-br from-cyber-cyan/15 via-cyber-blue/10 to-transparent border-b border-cyber-cyan/15 relative">
                        <div class="flex justify-between items-start mb-3">
                            <span class="px-2.5 py-1 rounded-md text-[11px] font-mono font-bold bg-cyber-cyan/20 text-cyber-cyan">مشروع تخرج رسمي</span>
                            <span class="text-xs text-gray-400 font-mono">جامعة تعز</span>
                        </div>
                        <h3 class="text-xl font-bold text-white mb-1" data-i18n="proj1_name">دليل الجامعة الذكي (SUH)</h3>
                        <p class="text-xs text-cyber-cyan font-mono">Smart University Handbook</p>
                    </div>
                    <div class="p-6 flex-1 flex flex-col justify-between">
                        <p class="text-xs text-gray-300 leading-relaxed mb-4" data-i18n="proj1_summary">
                            منصة وتطبيق جوال متعدد المنصات لجامعة تعز. يدمج نموذج ذكاء اصطناعي لغوي كبير (LLaMA 3 Fine-Tuned) كمرشد أكاديمي ذكي، مع Firebase و Flutter ونظام صلاحيات RBAC دقيق.
                        </p>
                        <div>
                            <div class="flex flex-wrap gap-1.5 mb-5 font-mono text-[10px]">
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">Flutter</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">LLaMA 3</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">Firebase</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">Hugging Face</span>
                            </div>
                            <button class="w-full py-2.5 rounded-xl btn-outline-cyber text-xs font-bold open-modal-btn" data-project="suh">
                                <i class="fas fa-circle-info mr-1 rtl:ml-1"></i> <span data-i18n="btn_details">تفاصيل المشروع الكاملة</span>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Project 2: Digital Twin IDS & XAI -->
                <div class="project-item glass-card rounded-2xl overflow-hidden flex flex-col" data-category="sec ai">
                    <div class="p-6 bg-gradient-to-br from-cyber-purple/15 via-cyber-blue/10 to-transparent border-b border-cyber-purple/15 relative">
                        <div class="flex justify-between items-start mb-3">
                            <span class="px-2.5 py-1 rounded-md text-[11px] font-mono font-bold bg-cyber-purple/20 text-cyber-purple">بحث علمي متقدم</span>
                            <span class="text-xs text-gray-400 font-mono">XAI NIDS</span>
                        </div>
                        <h3 class="text-xl font-bold text-white mb-1" data-i18n="proj2_name">كشف الهجمات بالتوأم الرقمي والـ XAI</h3>
                        <p class="text-xs text-cyber-purple font-mono">Hybrid Explainable AI NIDS</p>
                    </div>
                    <div class="p-6 flex-1 flex flex-col justify-between">
                        <p class="text-xs text-gray-300 leading-relaxed mb-4" data-i18n="proj2_summary">
                            نظام هجين لاكتشاف الشذوذ والتنبؤ المبكر بالهجمات السيبرانية يجمع Autoencoders و Isolation Forest مع LSTM و XGBoost، ويفسر القرارات بمؤشرات SHAP داخل بيئة GNS3.
                        </p>
                        <div>
                            <div class="flex flex-wrap gap-1.5 mb-5 font-mono text-[10px]">
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">Autoencoders</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">SHAP (XAI)</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">Zeek / Suricata</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">GNS3 Lab</span>
                            </div>
                            <button class="w-full py-2.5 rounded-xl btn-outline-cyber text-xs font-bold open-modal-btn" data-project="xai_nids">
                                <i class="fas fa-circle-info mr-1 rtl:ml-1"></i> <span data-i18n="btn_details">تفاصيل المشروع الكاملة</span>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Project 3: Souq Yemen E-Commerce -->
                <div class="project-item glass-card rounded-2xl overflow-hidden flex flex-col" data-category="mobile cloud">
                    <div class="p-6 bg-gradient-to-br from-cyber-emerald/15 via-cyber-cyan/10 to-transparent border-b border-cyber-emerald/15 relative">
                        <div class="flex justify-between items-start mb-3">
                            <span class="px-2.5 py-1 rounded-md text-[11px] font-mono font-bold bg-cyber-emerald/20 text-cyber-emerald">منصة إنتاجية</span>
                            <span class="text-xs text-gray-400 font-mono">Multi-Vendor</span>
                        </div>
                        <h3 class="text-xl font-bold text-white mb-1" data-i18n="proj3_name">منصة سوق اليمن للتجارة الإلكترونية</h3>
                        <p class="text-xs text-cyber-emerald font-mono">Souq Yemen Platform & Admin</p>
                    </div>
                    <div class="p-6 flex-1 flex flex-col justify-between">
                        <p class="text-xs text-gray-300 leading-relaxed mb-4" data-i18n="proj3_summary">
                            منصة تجارة إلكترونية جماعية للمحافظات اليمنية مبنية بـ Flutter Clean Architecture مع دعم الأوفلاين (Hive Offline-First) وخلفية Supabase PostgreSQL RLS ولوحة تحكم متقدمة.
                        </p>
                        <div>
                            <div class="flex flex-wrap gap-1.5 mb-5 font-mono text-[10px]">
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">Flutter 3.11+</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">Clean Arch</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">Supabase RLS</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">Hive Cache</span>
                            </div>
                            <button class="w-full py-2.5 rounded-xl btn-outline-cyber text-xs font-bold open-modal-btn" data-project="souq">
                                <i class="fas fa-circle-info mr-1 rtl:ml-1"></i> <span data-i18n="btn_details">تفاصيل المشروع الكاملة</span>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Project 4: GigatopX EduCloud -->
                <div class="project-item glass-card rounded-2xl overflow-hidden flex flex-col" data-category="cloud">
                    <div class="p-6 bg-gradient-to-br from-cyber-blue/15 via-cyber-purple/10 to-transparent border-b border-cyber-blue/15 relative">
                        <div class="flex justify-between items-start mb-3">
                            <span class="px-2.5 py-1 rounded-md text-[11px] font-mono font-bold bg-cyber-blue/20 text-cyber-blue">منصة SaaS سحابية</span>
                            <span class="text-xs text-gray-400 font-mono">Multi-Tenant</span>
                        </div>
                        <h3 class="text-xl font-bold text-white mb-1" data-i18n="proj4_name">منصة التعليم السحابية (EduCloud)</h3>
                        <p class="text-xs text-cyber-blue font-mono">Oasis Learning Nexus / GigatopX</p>
                    </div>
                    <div class="p-6 flex-1 flex flex-col justify-between">
                        <p class="text-xs text-gray-300 leading-relaxed mb-4" data-i18n="proj4_summary">
                            منصة إدارة المؤسسات التعليمية (جامعات، مدارس، معاهد) متعددة المستأجرين مع عزل بيانات مشدد على مستوى قاعدة بيانات PostgreSQL باستخدام سياسات RLS وواجهات React حديثة.
                        </p>
                        <div>
                            <div class="flex flex-wrap gap-1.5 mb-5 font-mono text-[10px]">
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">React / Vite</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">Drizzle ORM</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">PostgreSQL RLS</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">Tailwind</span>
                            </div>
                            <button class="w-full py-2.5 rounded-xl btn-outline-cyber text-xs font-bold open-modal-btn" data-project="educloud">
                                <i class="fas fa-circle-info mr-1 rtl:ml-1"></i> <span data-i18n="btn_details">تفاصيل المشروع الكاملة</span>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Project 5: ELK SOC Lab -->
                <div class="project-item glass-card rounded-2xl overflow-hidden flex flex-col" data-category="sec">
                    <div class="p-6 bg-gradient-to-br from-cyber-cyan/15 via-cyber-emerald/10 to-transparent border-b border-cyber-cyan/15 relative">
                        <div class="flex justify-between items-start mb-3">
                            <span class="px-2.5 py-1 rounded-md text-[11px] font-mono font-bold bg-cyber-cyan/20 text-cyber-cyan">مختبر أمني عملي</span>
                            <span class="text-xs text-gray-400 font-mono">SIEM & Log Analysis</span>
                        </div>
                        <h3 class="text-xl font-bold text-white mb-1" data-i18n="proj5_name">مختبر مركز العمليات الأمني (ELK Stack)</h3>
                        <p class="text-xs text-cyber-cyan font-mono">SOC Threat Analysis Lab</p>
                    </div>
                    <div class="p-6 flex-1 flex flex-col justify-between">
                        <p class="text-xs text-gray-300 leading-relaxed mb-4" data-i18n="proj5_summary">
                            مختبر عملي متكامل لتجميع وفهرسة وتحليل سجلات التهديدات السيبرانية باستخدام Elasticsearch و Kibana و Logstash عبر بيئات Docker Compose وبناء لوحات متابعة لحظية.
                        </p>
                        <div>
                            <div class="flex flex-wrap gap-1.5 mb-5 font-mono text-[10px]">
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">Elasticsearch</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">Kibana</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">Docker Compose</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">SIEM</span>
                            </div>
                            <button class="w-full py-2.5 rounded-xl btn-outline-cyber text-xs font-bold open-modal-btn" data-project="elklab">
                                <i class="fas fa-circle-info mr-1 rtl:ml-1"></i> <span data-i18n="btn_details">تفاصيل المشروع الكاملة</span>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Project 6: Secure Employee Management -->
                <div class="project-item glass-card rounded-2xl overflow-hidden flex flex-col" data-category="sec cloud">
                    <div class="p-6 bg-gradient-to-br from-cyber-purple/15 via-red-500/10 to-transparent border-b border-cyber-purple/15 relative">
                        <div class="flex justify-between items-start mb-3">
                            <span class="px-2.5 py-1 rounded-md text-[11px] font-mono font-bold bg-cyber-purple/20 text-cyber-purple">تدقيق أمني وهندسي</span>
                            <span class="text-xs text-gray-400 font-mono">DevSecOps Audit</span>
                        </div>
                        <h3 class="text-xl font-bold text-white mb-1" data-i18n="proj6_name">نظام إدارة الموظفين المحمي (Flask)</h3>
                        <p class="text-xs text-cyber-purple font-mono">Secure Employee System (OWASP/Sonar)</p>
                    </div>
                    <div class="p-6 flex-1 flex flex-col justify-between">
                        <p class="text-xs text-gray-300 leading-relaxed mb-4" data-i18n="proj6_summary">
                            نظام إدارة موظفين محمي تم تطويره بإطار Flask، خضع لاختبارات اختراق وتقييم ثغرات ديناميكية بواسطة OWASP ZAP وفحص كود أمني شامل بواسطة SonarQube.
                        </p>
                        <div>
                            <div class="flex flex-wrap gap-1.5 mb-5 font-mono text-[10px]">
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">Python Flask</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">OWASP ZAP</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">SonarQube</span>
                                <span class="px-2 py-0.5 rounded bg-gray-800 text-gray-300">Patching</span>
                            </div>
                            <button class="w-full py-2.5 rounded-xl btn-outline-cyber text-xs font-bold open-modal-btn" data-project="secure_emp">
                                <i class="fas fa-circle-info mr-1 rtl:ml-1"></i> <span data-i18n="btn_details">تفاصيل المشروع الكاملة</span>
                            </button>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- ================= INTERACTIVE CYBER TERMINAL SECTION ================= -->
    <section id="terminal" class="py-20 px-4 sm:px-6 lg:px-8 relative border-t border-cyber-cyan/10">
        <div class="max-w-5xl mx-auto">
            <div class="text-center max-w-2xl mx-auto mb-10">
                <span class="text-cyber-cyan font-mono text-sm tracking-wider uppercase font-bold" data-i18n="term_badge">// الطرفية السيبرانية التفاعلية</span>
                <h2 class="text-3xl font-extrabold mt-2" data-i18n="term_title">Rami CLI Environment</h2>
                <p class="text-gray-400 mt-2 text-xs sm:text-sm" data-i18n="term_desc">
                    يمكنك تشغيل أوامر حقيقية لاستعراض ملفاتي ومشاريعي ومؤشرات الـ SOC أو النقر على الأزرار السريعة.
                </p>
            </div>

            <!-- Terminal Window -->
            <div class="terminal-window rounded-2xl overflow-hidden shadow-2xl">
                <!-- Bar -->
                <div class="bg-gray-900/90 px-4 py-3 border-b border-cyber-cyan/20 flex items-center justify-between">
                    <div class="flex items-center gap-2">
                        <span class="w-3 h-3 rounded-full bg-red-500 cursor-pointer" onclick="clearTerminal()"></span>
                        <span class="w-3 h-3 rounded-full bg-yellow-500"></span>
                        <span class="w-3 h-3 rounded-full bg-green-500"></span>
                        <span class="text-xs text-gray-400 ml-2 font-mono">guest@rami-security-workstation:~$</span>
                    </div>
                    <span class="text-[11px] text-cyber-cyan font-mono">bash v5.2</span>
                </div>

                <!-- Quick Buttons -->
                <div class="p-3 bg-gray-950/80 border-b border-gray-800/80 flex flex-wrap gap-2 text-xs font-mono">
                    <span class="text-gray-500 self-center text-[11px]" data-i18n="quick_cmd_lbl">أوامر سريعة:</span>
                    <button class="px-2.5 py-1 rounded bg-cyber-cyan/10 text-cyber-cyan hover:bg-cyber-cyan/20 transition-all" onclick="runCommand('whoami')">whoami</button>
                    <button class="px-2.5 py-1 rounded bg-cyber-blue/10 text-cyber-blue hover:bg-cyber-blue/20 transition-all" onclick="runCommand('academics')">academics</button>
                    <button class="px-2.5 py-1 rounded bg-cyber-purple/10 text-cyber-purple hover:bg-cyber-purple/20 transition-all" onclick="runCommand('projects')">projects</button>
                    <button class="px-2.5 py-1 rounded bg-cyber-emerald/10 text-cyber-emerald hover:bg-cyber-emerald/20 transition-all" onclick="runCommand('soc-status')">soc-status</button>
                    <button class="px-2.5 py-1 rounded bg-yellow-500/10 text-yellow-400 hover:bg-yellow-500/20 transition-all" onclick="runCommand('contact')">contact</button>
                    <button class="px-2.5 py-1 rounded bg-red-500/10 text-red-400 hover:bg-red-500/20 transition-all" onclick="runCommand('clear')">clear</button>
                </div>

                <!-- Output Area -->
                <div class="p-5 font-mono text-xs sm:text-sm text-gray-200 min-h-[260px] max-h-[380px] overflow-y-auto space-y-3 leading-relaxed" id="terminalOutput">
                    <p class="text-gray-400">مرحباً بك في المحطة الطرفية لموقع رامي أمين قاسم. اكتب <span class="text-cyber-cyan font-bold">help</span> لعرض كافة الأوامر المتاحة.</p>
                </div>

                <!-- Input Row -->
                <div class="px-5 py-3.5 bg-gray-950/90 border-t border-gray-800 flex items-center gap-2 font-mono text-sm">
                    <span class="text-cyber-cyan font-bold">&gt;</span>
                    <input type="text" id="terminalInput" class="w-full bg-transparent text-cyber-cyan outline-none font-mono placeholder-gray-600" placeholder="اكتب أمراً مثل 'help' أو 'whoami' واضغط Enter..." autocomplete="off">
                </div>
            </div>
        </div>
    </section>

    <!-- ================= JOURNEY TIMELINE ================= -->
    <section id="journey" class="py-20 px-4 sm:px-6 lg:px-8 relative border-t border-cyber-cyan/10">
        <div class="max-w-4xl mx-auto">
            <div class="text-center max-w-2xl mx-auto mb-16">
                <span class="text-cyber-cyan font-mono text-sm tracking-wider uppercase font-bold" data-i18n="journey_badge">// المسيرة والنمو الأكاديمي</span>
                <h2 class="text-3xl font-extrabold mt-2" data-i18n="journey_title">المحطات المفصلية</h2>
            </div>

            <div class="timeline-box space-y-10 pl-10 pr-0 rtl:pr-10 rtl:pl-0">

                <!-- Milestone 1 -->
                <div class="relative glass-card p-6 rounded-2xl border-r-4 rtl:border-r-4 rtl:border-l-0 ltr:border-l-4 ltr:border-r-0 border-cyber-cyan">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-2 font-mono">
                        <span class="text-xs text-cyber-cyan font-bold">2026 - الحاضر</span>
                        <span class="px-2 py-0.5 rounded text-[11px] bg-cyber-emerald/15 text-cyber-emerald">مستوى رابع (Senior)</span>
                    </div>
                    <h3 class="text-lg font-bold" data-i18n="mile1_title">السنة النهائية في قسم الأمن السيبراني – جامعة تعز</h3>
                    <p class="text-xs text-gray-300 mt-2 leading-relaxed" data-i18n="mile1_desc">
                        التركيز على هندسة الكشف عن التهديدات المتقدمة، مشاريع التخرج، ومحاكاة سيناريوهات الاختراق والدفاع المؤسسي عبر التوأم الرقمي ونماذج الذكاء الاصطناعي.
                    </p>
                </div>

                <!-- Milestone 2 -->
                <div class="relative glass-card p-6 rounded-2xl border-r-4 rtl:border-r-4 rtl:border-l-0 ltr:border-l-4 ltr:border-r-0 border-cyber-purple">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-2 font-mono">
                        <span class="text-xs text-cyber-purple font-bold">2024 - 2026</span>
                        <span class="px-2 py-0.5 rounded text-[11px] bg-cyber-purple/15 text-cyber-purple">هندسة التطبيقات والذكاء الاصطناعي</span>
                    </div>
                    <h3 class="text-lg font-bold" data-i18n="mile2_title">بناء منصة سوق اليمن وتدريب LLaMA 3 لدليل الجامعة</h3>
                    <p class="text-xs text-gray-300 mt-2 leading-relaxed" data-i18n="mile2_desc">
                        تطوير تطبيق وتجارة إلكترونية متكاملة بـ Flutter Clean Architecture مع عزل بيانات مشدد في Supabase، وتدريب نموذج ذكي مخصص للجامعة على Google Colab و Hugging Face.
                    </p>
                </div>

                <!-- Milestone 3 -->
                <div class="relative glass-card p-6 rounded-2xl border-r-4 rtl:border-r-4 rtl:border-l-0 ltr:border-l-4 ltr:border-r-0 border-cyber-blue">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-2 font-mono">
                        <span class="text-xs text-cyber-blue font-bold">2023 - 2024</span>
                        <span class="px-2 py-0.5 rounded text-[11px] bg-cyber-blue/15 text-cyber-blue">مختبرات الـ SOC والشبكات</span>
                    </div>
                    <h3 class="text-lg font-bold" data-i18n="mile3_title">إتقان أدوات مركز العمليات (SIEM / ELK) وتوبولوجيا GNS3</h3>
                    <p class="text-xs text-gray-300 mt-2 leading-relaxed" data-i18n="mile3_desc">
                        بناء مختبرات ELK Stack لفحص سجلات الهجمات، إعداد وتأمين راوترات MikroTik، وتصميم توبولوجيا شبكات افتراضية معقدة عبر GNS3 و Cisco Packet Tracer.
                    </p>
                </div>

                <!-- Milestone 4 -->
                <div class="relative glass-card p-6 rounded-2xl border-r-4 rtl:border-r-4 rtl:border-l-0 ltr:border-l-4 ltr:border-r-0 border-cyber-emerald">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-2 font-mono">
                        <span class="text-xs text-cyber-emerald font-bold">2022 - 2023</span>
                        <span class="px-2 py-0.5 rounded text-[11px] bg-cyber-emerald/15 text-cyber-emerald">الأساس البرمجي المتين</span>
                    </div>
                    <h3 class="text-lg font-bold" data-i18n="mile4_title">الخوارزميات وهياكل البيانات بلغة C++</h3>
                    <p class="text-xs text-gray-300 mt-2 leading-relaxed" data-i18n="mile4_desc">
                        دراسة عميقة لمفاهيم البرمجة الكائنية المتقدمة وتطبيق هياكل البيانات يدوياً (القوائم المترابطة، الطوابير، المكدسات) مستنداً لمسار المهندس محمد أبو هدهود.
                    </p>
                </div>

            </div>
        </div>
    </section>

    <!-- ================= CONTACT SECTION ================= -->
    <section id="contact" class="py-20 px-4 sm:px-6 lg:px-8 relative border-t border-cyber-cyan/10">
        <div class="max-w-6xl mx-auto">
            <div class="text-center max-w-2xl mx-auto mb-16">
                <span class="text-cyber-cyan font-mono text-sm tracking-wider uppercase font-bold" data-i18n="contact_badge">// قنوات التواصل المباشر</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold mt-2" data-i18n="contact_title">لنبنِ حلولاً آمنة ومبتكرة معاً</h2>
                <p class="text-gray-400 mt-3 text-sm sm:text-base" data-i18n="contact_desc">
                    منفتح للتعاون في المشاريع التقنية، الأبحاث الأمنية، والفرص النوعية في تطوير البرمجيات والأمن السيبراني.
                </p>
            </div>

            <div class="grid lg:grid-cols-12 gap-8 items-start">
                <!-- Contact Info Cards -->
                <div class="lg:col-span-5 space-y-4">
                    <div class="glass-card p-6 rounded-2xl flex items-center gap-4">
                        <div class="w-12 h-12 rounded-xl bg-cyber-cyan/15 text-cyber-cyan flex items-center justify-center text-xl shrink-0">
                            <i class="fas fa-envelope"></i>
                        </div>
                        <div>
                            <span class="text-xs text-gray-400 font-mono" data-i18n="lbl_email">البريد الإلكتروني المباشر</span>
                            <a href="mailto:ramyamyn41@gmail.com" class="block font-mono font-bold text-sm sm:text-base text-white hover:text-cyber-cyan transition-colors">ramyamyn41@gmail.com</a>
                        </div>
                    </div>

                    <div class="glass-card p-6 rounded-2xl flex items-center gap-4">
                        <div class="w-12 h-12 rounded-xl bg-cyber-purple/15 text-cyber-purple flex items-center justify-center text-xl shrink-0">
                            <i class="fab fa-github"></i>
                        </div>
                        <div>
                            <span class="text-xs text-gray-400 font-mono" data-i18n="lbl_github">مستودع الأكواد (GitHub)</span>
                            <a href="https://github.com/RA757575" target="_blank" class="block font-mono font-bold text-sm sm:text-base text-white hover:text-cyber-purple transition-colors">github.com/RA757575</a>
                        </div>
                    </div>

                    <div class="glass-card p-6 rounded-2xl flex items-center gap-4">
                        <div class="w-12 h-12 rounded-xl bg-cyber-emerald/15 text-cyber-emerald flex items-center justify-center text-xl shrink-0">
                            <i class="fas fa-location-dot"></i>
                        </div>
                        <div>
                            <span class="text-xs text-gray-400 font-mono" data-i18n="lbl_location">الموقع والجامعة</span>
                            <p class="font-bold text-sm sm:text-base text-white" data-i18n="lbl_location_val">تعز، الجمهورية اليمنية · جامعة تعز</p>
                        </div>
                    </div>

                    <!-- Fast CV Download -->
                    <div class="p-6 rounded-2xl glass border border-cyber-cyan/25 text-center">
                        <h4 class="font-bold text-sm mb-2" data-i18n="cv_box_title">السيرة الذاتية المهنية والأكاديمية</h4>
                        <p class="text-xs text-gray-400 mb-4" data-i18n="cv_box_desc">يمكنك حفظ صفحة السيرة أو التواصل المباشر لطلب النسخة الأكاديمية الرسمية.</p>
                        <a href="javascript:window.print()" class="w-full py-3 rounded-xl btn-cyber block text-xs font-bold font-mono">
                            <i class="fas fa-file-arrow-down mr-1 rtl:ml-1"></i> <span data-i18n="btn_print_cv">طباعة / حفظ السيرة الذاتية (PDF)</span>
                        </a>
                    </div>
                </div>

                <!-- Contact Form -->
                <div class="lg:col-span-7">
                    <form class="glass-card p-8 rounded-2xl space-y-4" id="contactForm">
                        <div class="grid sm:grid-cols-2 gap-4">
                            <div>
                                <label class="block text-xs font-mono text-gray-400 mb-1" data-i18n="form_name_lbl">الاسم الكريم</label>
                                <input type="text" required class="w-full px-4 py-3 rounded-xl bg-gray-900/60 border border-cyber-cyan/20 text-white outline-none focus:border-cyber-cyan transition-all text-sm font-cairo" placeholder="مثال: د. عزالدين / م. أحمد">
                            </div>
                            <div>
                                <label class="block text-xs font-mono text-gray-400 mb-1" data-i18n="form_email_lbl">البريد الإلكتروني</label>
                                <input type="email" required class="w-full px-4 py-3 rounded-xl bg-gray-900/60 border border-cyber-cyan/20 text-white outline-none focus:border-cyber-cyan transition-all text-sm font-mono" placeholder="name@example.com">
                            </div>
                        </div>
                        <div>
                            <label class="block text-xs font-mono text-gray-400 mb-1" data-i18n="form_subject_lbl">موضوع الرسالة</label>
                            <input type="text" required class="w-full px-4 py-3 rounded-xl bg-gray-900/60 border border-cyber-cyan/20 text-white outline-none focus:border-cyber-cyan transition-all text-sm font-cairo" placeholder="بشأن مشروع / فرصة عمل / استشارة أمنية">
                        </div>
                        <div>
                            <label class="block text-xs font-mono text-gray-400 mb-1" data-i18n="form_msg_lbl">نص الرسالة</label>
                            <textarea rows="4" required class="w-full px-4 py-3 rounded-xl bg-gray-900/60 border border-cyber-cyan/20 text-white outline-none focus:border-cyber-cyan transition-all text-sm font-cairo" placeholder="اكتب تفاصيل استفسارك أو مشروعك هنا..."></textarea>
                        </div>
                        <button type="submit" class="w-full py-3.5 rounded-xl btn-cyber text-sm font-bold flex items-center justify-center gap-2">
                            <i class="fas fa-paper-plane"></i>
                            <span data-i18n="btn_send_msg">إرسال الرسالة فوراً</span>
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- ================= FOOTER ================= -->
    <footer class="py-10 px-4 sm:px-6 border-t border-cyber-cyan/15 text-center font-mono text-xs text-gray-400">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-4">
            <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-cyber-emerald"></span>
                <span>Rami Amin Qasem Ali Saeed &copy; 2026</span>
            </div>
            <p data-i18n="footer_credits">قسم الأمن السيبراني · كلية العلوم التطبيقية · جامعة تعز</p>
            <div class="flex gap-4 text-base">
                <a href="https://github.com/RA757575" target="_blank" class="hover:text-cyber-cyan"><i class="fab fa-github"></i></a>
                <a href="mailto:ramyamyn41@gmail.com" class="hover:text-cyber-cyan"><i class="fas fa-envelope"></i></a>
            </div>
        </div>
    </footer>

    <!-- ================= PROJECT DETAIL MODAL ================= -->
    <div class="modal-overlay" id="projectModalOverlay">
        <div class="modal-content rounded-2xl w-full max-w-3xl max-h-[90vh] overflow-y-auto m-4 p-6 sm:p-8 relative">
            <button class="absolute top-5 left-5 rtl:left-5 rtl:right-auto ltr:right-5 ltr:left-auto w-9 h-9 rounded-xl glass flex items-center justify-center text-gray-400 hover:text-white" id="closeModalBtn">
                <i class="fas fa-xmark"></i>
            </button>
            <div id="modalBody">
                <!-- Dynamically populated via JS -->
            </div>
        </div>
    </div>

    <!-- ================= SCRIPTS & I18N ================= -->
    <script>
    /* Project Detailed Data */
    const projectsData = {
        suh: {
            title_ar: 'دليل الجامعة الذكي (Smart University Handbook - SUH)',
            title_en: 'Smart University Handbook (SUH)',
            subtitle_ar: 'مشروع بحثي وتطبيقي لجامعة تعز مع نموذج LLaMA 3 مخصص',
            subtitle_en: 'Research & Applied System for Taiz University with Fine-Tuned LLaMA 3',
            desc_ar: `منظومة مركزية ذكية صُممت لحل مشكلة تشتت المعلومات الأكاديمية والمالية والإدارية لطلبة جامعة تعز.
            <br><br>
            <strong>المكونات المعمارية الرئيسية:</strong>
            <ul class="list-disc list-inside mt-2 space-y-1 text-gray-300">
                <li><strong>تطبيق المستخدم:</strong> واجهات مستخدم متعددة المنصات بإطار Flutter (Dart) لشاشات الطلبة ولوحات الإدارة.</li>
                <li><strong>محرك الذكاء الاصطناعي:</strong> تخصيص وتدريب نموذج LLaMA 3 على Google Colab واستضافته على Hugging Face كمرشد أكاديمي ذكي.</li>
                <li><strong>الخادم السحابي:</strong> Firebase Cloud Firestore لقواعد البيانات الآنية، و Cloud Functions كوسيط آمن ومشفر.</li>
                <li><strong>الأمان:</strong> نموذج التحكم بالوصول القائم على الأدوار (RBAC) وقواعد حماية صارمة.</li>
                <li><strong>الفريق والإشراف:</strong> رامي أمين قاسم، ربيع محمد ناجي، إيهاب فتحي — بإشراف الدكتور عزالدين المخلافي.</li>
            </ul>`,
            desc_en: `A centralized smart ecosystem designed to resolve fragmented academic, financial, and administrative procedures for Taiz University students.
            <br><br>
            <strong>Key Architecture Highlights:</strong>
            <ul class="list-disc list-inside mt-2 space-y-1 text-gray-300">
                <li><strong>Cross-Platform Client:</strong> Built using Flutter & Dart for both students and administrator panels.</li>
                <li><strong>Conversational AI Engine:</strong> Custom fine-tuned LLaMA 3 on Google Colab, hosted on Hugging Face as an academic advisor.</li>
                <li><strong>Backend:</strong> Firebase Cloud Firestore for real-time synchronization, and Cloud Functions as a secure proxy.</li>
                <li><strong>Security:</strong> Role-Based Access Control (RBAC) and strict security rules.</li>
                <li><strong>Team & Supervisor:</strong> Rami Amin Qasem, Rabie Mohammed Naji, Ehab Fathi — Supervised by Dr. Ezzeldeen Al-Mikhlafi.</li>
            </ul>`,
            tags: ['Flutter', 'Dart', 'LLaMA 3', 'Firebase', 'Hugging Face', 'RBAC', 'Taiz University']
        },
        xai_nids: {
            title_ar: 'كشف الهجمات بالتوأم الرقمي والذكاء الاصطناعي القابل للتفسير (XAI NIDS)',
            title_en: 'Digital Twin Cyberattack Detection with Explainable AI (XAI NIDS)',
            subtitle_ar: 'نظام هجين لاكتشاف الشذوذ والتنبؤ المبكر بالهجمات السيبرانية',
            subtitle_en: 'Hybrid System for Anomaly Detection & Early Prediction with XAI',
            desc_ar: `بحث متقدم يقدم إطاراً دفاعياً متكاملاً يتغلب على ثغرات أنظمة كشف التسلل التقليدية (كثرة الإنذارات الكاذبة وانعدام التفسير).
            <br><br>
            <strong>خط الأنابيب الهجين (Hybrid Pipeline):</strong>
            <ul class="list-disc list-inside mt-2 space-y-1 text-gray-300">
                <li><strong>اكتشاف الشذوذ:</strong> دمج Autoencoder و Isolation Forest في معامل شذوذ موحد (Anomaly Score).</li>
                <li><strong>التنبؤ الزمني:</strong> استخدام شبكات LSTM أو TCN لتقدير احتمالية الهجوم خلال نافذة زمنية (5-15 دقيقة قادمة).</li>
                <li><strong>معامل حساسية الأصول (Asset Sensitivity):</strong> ترجيح خطورة التهديد بناءً على أهمية الخادم المستهدف في شبكة المنشأة.</li>
                <li><strong>مصنف القرار النهائي:</strong> نموذج XGBoost رباعي الحالات (طبيعي، مشبوه، تمهيد لهجوم، هجوم فعلي).</li>
                <li><strong>الذكاء الاصطناعي القابل للتفسير:</strong> تطبيق قيم SHAP لتفسير أسباب التنبيه لمحلل الـ SOC.</li>
                <li><strong>التحقق المخبري:</strong> محاكاة توبولوجيا شبكة كاملة في مختبر GNS3 مع مجسات Zeek و Suricata.</li>
            </ul>`,
            desc_en: `Advanced research proposing an end-to-end defensive framework addressing high false positives, lack of prediction, and lack of explainability.
            <br><br>
            <strong>Hybrid Pipeline Highlights:</strong>
            <ul class="list-disc list-inside mt-2 space-y-1 text-gray-300">
                <li><strong>Anomaly Detection:</strong> Fuses Autoencoder reconstruction error with Isolation Forest into a unified Anomaly Score.</li>
                <li><strong>Temporal Prediction:</strong> LSTM / TCN sequence modeling predicting attack probability within a 5-15 min window.</li>
                <li><strong>Asset Sensitivity Weighting:</strong> Weights flows by the target host's business criticality.</li>
                <li><strong>Decision Layer:</strong> XGBoost classifier categorizing into Normal, Suspicious, Pre-Attack, and Attack.</li>
                <li><strong>Explainable AI:</strong> Uses SHAP (SHapley Additive exPlanations) for analyst-grade interpretability.</li>
                <li><strong>Lab Validation:</strong> Validated inside a GNS3 enterprise virtual laboratory with Zeek & Suricata sensors.</li>
            </ul>`,
            tags: ['Autoencoders', 'LSTM', 'XGBoost', 'SHAP (XAI)', 'GNS3', 'Zeek', 'Suricata', 'CICIDS2017']
        },
        souq: {
            title_ar: 'منصة سوق اليمن للتجارة الإلكترونية (Souq Yemen Platform & Admin)',
            title_en: 'Souq Yemen E-Commerce Platform & Admin',
            subtitle_ar: 'تطبيق تجارة إلكترونية متعدد المتاجر معمارية نظيفة ودعم الأوفلاين',
            subtitle_en: 'Multi-vendor e-commerce with Clean Architecture & Offline-First Sync',
            desc_ar: `منصة تجارة إلكترونية جماعية متقدمة تخدم المدن والمحافظات اليمنية، تمكن التجار من إدارة المتاجر والطلبات بسلاسة.
            <br><br>
            <strong>الميزات الهندسية:</strong>
            <ul class="list-disc list-inside mt-2 space-y-1 text-gray-300">
                <li><strong>Clean Architecture:</strong> فصل تام للطبقات (Presentation, Domain, Data) لضمان قابلية التوسع والصيانة.</li>
                <li><strong>Offline-First:</strong> استخدام قاعدة بيانات Hive للتخزين المؤقت وطابور PendingActionsService لمزامنة العمليات تلقائياً عند عودة الاتصال.</li>
                <li><strong>Backend:</strong> منصة Supabase السحابية مع قواعد بيانات PostgreSQL وسياسات أمان Row Level Security (RLS).</li>
                <li><strong>المصادقة:</strong> تسجيل الدخول الأصلي Google Sign-In المدمج مع Android Credential Manager.</li>
                <li><strong>لوحة تحكم إدارية مستقلة:</strong> souq_admin لإدارة المتاجر والمراجعات ونظام فحص الصور.</li>
            </ul>`,
            desc_en: `Comprehensive multi-vendor digital commerce platform built for Yemeni governorates with resilient offline handling.
            <br><br>
            <strong>Engineering Highlights:</strong>
            <ul class="list-disc list-inside mt-2 space-y-1 text-gray-300">
                <li><strong>Clean Architecture:</strong> Strict separation of presentation, domain, and data layers.</li>
                <li><strong>Offline-First:</strong> High-performance Hive caching with PendingActionsService for seamless synchronization.</li>
                <li><strong>Backend:</strong> Supabase PostgreSQL with robust Row Level Security (RLS) isolation.</li>
                <li><strong>Authentication:</strong> Native Google Sign-In with Android Credential Manager.</li>
                <li><strong>Dedicated Admin Portal:</strong> souq_admin companion app for vendor validation and image moderation.</li>
            </ul>`,
            tags: ['Flutter', 'Clean Architecture', 'Supabase', 'PostgreSQL RLS', 'Hive', 'Google Sign-In']
        },
        educloud: {
            title_ar: 'منصة التعليم السحابية متعددة المستأجرين (GigatopX EduCloud)',
            title_en: 'GigatopX EduCloud / Oasis Learning Nexus',
            subtitle_ar: 'نظام SaaS متكامل لإدارة الجامعات والمدارس والمعاهد مع عزل RLS صارم',
            subtitle_en: 'Multi-Tenant Educational SaaS with strict PostgreSQL RLS isolation',
            desc_ar: `منصة سحابية متطورة لإدارة المنظومة التعليمية الكاملة (جامعات، مدارس، معاهد).
            <br><br>
            <strong>أبرز المميزات:</strong>
            <ul class="list-disc list-inside mt-2 space-y-1 text-gray-300">
                <li><strong>عزل بيانات متعدد المستأجرين (Multi-Tenancy):</strong> عزل أمني صارم عبر دوال PostgreSQL RLS المخصصة.</li>
                <li><strong>واجهة متطورة:</strong> مبنية بـ React, TypeScript, Vite, TanStack Router/Query, و Tailwind CSS.</li>
                <li><strong>إدارة متكاملة:</strong> لوحة تحكم للجامعات والمدارس، إدارة الطلاب، الفصول الافتراضية، الاختبارات، والفواتير المالية.</li>
            </ul>`,
            desc_en: `Commercial multi-tenant educational SaaS platform supporting universities, schools, and training institutes.
            <br><br>
            <strong>Key Features:</strong>
            <ul class="list-disc list-inside mt-2 space-y-1 text-gray-300">
                <li><strong>Strict Tenant Isolation:</strong> Custom PostgreSQL Row Level Security (RLS) helper functions.</li>
                <li><strong>Modern Stack:</strong> React, TypeScript, Vite, TanStack Query, Drizzle ORM, and Tailwind CSS.</li>
                <li><strong>Modules:</strong> Multi-institution management, courses, quizzes, virtual classrooms, and fee invoices.</li>
            </ul>`,
            tags: ['React', 'TypeScript', 'Drizzle ORM', 'Supabase RLS', 'Multi-Tenant', 'Tailwind']
        },
        elklab: {
            title_ar: 'مختبر مركز العمليات الأمني العملي (ELK Stack SOC Lab)',
            title_en: 'ELK Stack Hands-On SOC Lab',
            subtitle_ar: 'تجميع السجلات والتحليل الأمني ورصد التهديدات في بيئة Docker',
            subtitle_en: 'Log aggregation, threat hunting, and SIEM dashboards in Docker',
            desc_ar: `مختبر عملي لتشغيل مركز عمليات أمني حقيقي لتحليل السجلات واكتشاف محاولات الاختراق.
            <br><br>
            <strong>المكونات:</strong>
            <ul class="list-disc list-inside mt-2 space-y-1 text-gray-300">
                <li>تشغيل Elasticsearch 9200 و Kibana 5601 و Logstash عبر Docker Compose.</li>
                <li>تحليل 300+ سجل تجريبي ورصد سلوكيات التسلل.</li>
                <li>بناء لوحات مراقبة Kibana Data Views ومتابعة الإنذارات الأمنية.</li>
            </ul>`,
            desc_en: `Hands-on practical security operations center lab for log parsing and real-time threat hunting.
            <br><br>
            <strong>Components:</strong>
            <ul class="list-disc list-inside mt-2 space-y-1 text-gray-300">
                <li>Elasticsearch, Kibana, and Logstash running via Docker Compose.</li>
                <li>Parsing and indexing 300+ threat logs.</li>
                <li>Custom Kibana visualizations, dashboards, and event telemetry.</li>
            </ul>`,
            tags: ['Elasticsearch', 'Kibana', 'Logstash', 'Docker', 'SIEM', 'Threat Hunting']
        },
        secure_emp: {
            title_ar: 'نظام إدارة الموظفين المحمي واختبارات الاختراق',
            title_en: 'Secure Employee Management System',
            subtitle_ar: 'تدقيق أمني شامل عبر OWASP ZAP و SonarQube وإصلاح الثغرات',
            subtitle_en: 'Security audit & vulnerability patching via OWASP ZAP & SonarQube',
            desc_ar: `تطبيق ويب مبني بإطار Flask تم إخضاعه لتدقيق واختبارات أمنية مكثفة.
            <br><br>
            <strong>أبرز ما تم إنجازه:</strong>
            <ul class="list-disc list-inside mt-2 space-y-1 text-gray-300">
                <li>إجراء فحص اختراق ديناميكي بواسطة OWASP ZAP واستخراج تقرير تقييم الثغرات.</li>
                <li>فحص ثابت لجودة وأمان الكود عبر SonarQube.</li>
                <li>إصلاح وترقيع الثغرات الأمنية في النسخة المحدثة (employee_system_secure_patched_v3).</li>
            </ul>`,
            desc_en: `Web application developed in Python Flask that underwent rigorous security hardening.
            <br><br>
            <strong>Key Activities:</strong>
            <ul class="list-disc list-inside mt-2 space-y-1 text-gray-300">
                <li>Dynamic vulnerability scanning and penetration test using OWASP ZAP.</li>
                <li>Static code analysis and vulnerability detection via SonarQube.</li>
                <li>Patching security vulnerabilities and verifying the patched release.</li>
            </ul>`,
            tags: ['Python Flask', 'OWASP ZAP', 'SonarQube', 'Vulnerability Assessment', 'Security Patching']
        }
    };

    /* Translation Dictionary */
    const translations = {
        ar: {
            loader_status: 'جارٍ تحميل محفظة رامي أمين قاسم...',
            nav_role_sub: 'أمن سيبراني & هندسة برمجيات',
            nav_about: 'عنّي',
            nav_academics: 'التخصص والجامعة',
            nav_skills: 'المهارات التقنية',
            nav_projects: 'المشاريع والأبحاث',
            nav_terminal: 'الطرفية التفاعلية',
            nav_journey: 'المسيرة',
            nav_contact: 'تواصل معي',
            drawer_status: 'مستوى رابع - أمن سيبراني',
            hero_status_badge: 'مستوى رابع (سنة التخرج) · قسم الأمن السيبراني · جامعة تعز',
            hero_greeting: 'مرحباً بك، أنا',
            hero_desc: 'مهندس أمن سيبراني ومطور أنظمة وتطبيقات متكاملة. أجمع بين الرؤية الدفاعية المتقدمة (SOC، كشف الشذوذ بالـ AI، ومراقبة الشبكات) وبين هندسة البرمجيات المتينة باستخدام Flutter (Clean Architecture) والأنظمة السحابية الموزعة (Supabase, PostgreSQL RLS, Firebase). شغفي بناء أنظمة برمجية آمنة وموثوقة من سطر الكود الأول حتى البنية التحتية.',
            btn_view_projects: 'استكشف المشاريع والأبحاث',
            btn_try_terminal: 'تشغيل الطرفية السيبرانية',
            btn_contact_me: 'تواصل مباشر',
            metric_level: 'جامعة تعز',
            metric_projects: 'مشاريع ومختبرات',
            metric_ai: 'نماذج AI وبحوث',
            metric_security: 'تصميم دفاعي',
            about_badge: '// من أنا ورؤيتي الهندسية',
            about_title: 'الأمن المضمن وهندسة النظم',
            about_p1: 'أنا رامي أمين قاسم علي سعيد، مهندس أمن سيبراني ومطور أنظمة برمجية في السنة النهائية (مستوى رابع) بكلية العلوم التطبيقية في جامعة تعز.',
            about_p2: 'خلال مسيرتي الأكاديمية والعملية، ركزتُ على دمج مفهوم Security by Design؛ حيث لا يُعامل الأمان كطبقة إضافية بعد انتهاء البرمجة، بل كحجر زاوية يبدأ من تصميم قاعدة البيانات، وفصل الطبقات بالمعمارية النظيفة، وضبط أمان السحابة بـ RLS، وحتى تطبيق الذكاء الاصطناعي للتنبؤ بالهجمات وكشف التسلل.',
            about_p3: 'قمت بتطوير وإطلاق مشاريع حقيقية كبرى تشمل منصات التجارة الإلكترونية ذات المعمارية النظيفة مع دعم العمل دون اتصال، وتدريب نماذج ذكاء اصطناعي لغوية (LLaMA 3) لدعم الخدمات الجامعية، وإجراء أبحاث متقدمة في اكتشاف الهجمات بالتوأم الرقمي والذكاء الاصطناعي القابل للتفسير.',
            about_card1_title: 'الجامعة والمستوى',
            about_card1_desc: 'جامعة تعز · كلية العلوم التطبيقية · قسم الأمن السيبراني (مستوى رابع / تخرج).',
            about_card2_title: 'التحليل الأمني والـ SOC',
            about_card2_desc: 'محلل مركز عمليات أمني، هندسة الكشف عن التهديدات، وتجميع سجلات SIEM.',
            about_card3_title: 'Clean Architecture',
            about_card3_desc: 'معمارية برمجية متقدمة في Flutter تضمن فصل منطق العمل عن واجهات العرض.',
            about_card4_title: 'هندسة الشبكات والسحابة',
            about_card4_desc: 'محاكاة عبر GNS3 و Packet Tracer، وتكوين راوترات MikroTik وحاويات Docker.',
            academics_badge: '// المسار الأكاديمي والتخصص',
            academics_title: 'جامعة تعز · كلية العلوم التطبيقية',
            academics_desc: 'طالب في السنة النهائية (مستوى رابع) بقسم الأمن السيبراني. دراسة أكاديمية وتطبيقية مكثفة تربط بين النظريات العميقة للأمن السيبراني، البروتوكولات الشبكية، وبناء البرمجيات المتينة.',
            pillar1_title: 'أمن العمليات و الـ SOC',
            pillar1_desc: 'تحليل السجلات ومراقبة التهديدات باستخدام ELK Stack في Docker، رصد حزم البيانات عبر Zeek و Suricata، واختبار الثغرات باستخدام Kali Linux و OWASP ZAP.',
            pillar2_title: 'تطبيقات الموبايل المتقدمة',
            pillar2_desc: 'تطوير تطبيقات Flutter متعددة المنصات بالاعتماد على Clean Architecture، التخزين المحلي Offline-First عبر Hive، وإدارة الحالة وحقن الاعتماديات باحترافية.',
            pillar3_title: 'الأنظمة السحابية و SaaS',
            pillar3_desc: 'تصميم وتطوير منصات SaaS متعددة المستأجرين (Multi-Tenant) مع عزل بيانات صارم عبر PostgreSQL RLS، واجهات React و TanStack، وتكاملات Supabase و Firebase.',
            pillar4_title: 'الذكاء الاصطناعي والأبحاث',
            pillar4_desc: 'تخصيص وتدريب النماذج اللغوية الكبيرة (LLaMA 3 Fine-Tuning)، وتطبيق تقنيات الذكاء الاصطناعي القابل للتفسير (XAI / SHAP) والتعلم العميق في كشف التسلل.',
            skills_badge: '// مصفوفة القدرات والخبرات',
            skills_title: 'الترسانة التقنية والأدوات المتقنة',
            skills_desc: 'مهارات عملية مطبقة في مشاريع ومختبرات حقيقية تشمل الأمن الدفاعي، الأطر السحابية، لغات البرمجة، وقواعد البيانات.',
            skill_g1_title: 'الأمن السيبراني والـ SOC',
            skill_g2_title: 'تطوير البرمجيات والموبايل',
            skill_g3_title: 'السحابة وقواعد البيانات والشبكات',
            projects_badge: '// معرض المشاريع والابتكارات',
            projects_title: 'أبرز الأبحاث والأنظمة المنفذة',
            projects_desc: 'مشاريع متكاملة صُممت وطُبقت بأعلى المعايير الهندسية والأمنية، يمكن النقر على أي مشروع لاستعراض التفاصيل المعمارية والتقنية.',
            filter_all: 'الكل',
            filter_sec: 'الأمن السيبراني & SOC',
            filter_mobile: 'تطبيقات الموبايل (Flutter)',
            filter_cloud: 'الأنظمة السحابية & SaaS',
            filter_ai: 'الأبحاث والـ AI',
            btn_details: 'تفاصيل المشروع الكاملة',
            term_badge: '// الطرفية السيبرانية التفاعلية',
            term_title: 'Rami CLI Environment',
            term_desc: 'يمكنك تشغيل أوامر حقيقية لاستعراض ملفاتي ومشاريعي ومؤشرات الـ SOC أو النقر على الأزرار السريعة.',
            quick_cmd_lbl: 'أوامر سريعة:',
            journey_badge: '// المسيرة والنمو الأكاديمي',
            journey_title: 'المحطات المفصلية',
            mile1_title: 'السنة النهائية في قسم الأمن السيبراني – جامعة تعز',
            mile1_desc: 'التركيز على هندسة الكشف عن التهديدات المتقدمة، مشاريع التخرج، ومحاكاة سيناريوهات الاختراق والدفاع المؤسسي عبر التوأم الرقمي ونماذج الذكاء الاصطناعي.',
            mile2_title: 'بناء منصة سوق اليمن وتدريب LLaMA 3 لدليل الجامعة',
            mile2_desc: 'تطوير تطبيق وتجارة إلكترونية متكاملة بـ Flutter Clean Architecture مع عزل بيانات مشدد في Supabase، وتدريب نموذج ذكي مخصص للجامعة على Google Colab و Hugging Face.',
            mile3_title: 'إتقان أدوات مركز العمليات (SIEM / ELK) وتوبولوجيا GNS3',
            mile3_desc: 'بناء مختبرات ELK Stack لفحص سجلات الهجمات، إعداد وتأمين راوترات MikroTik، وتصميم توبولوجيا شبكات افتراضية معقدة عبر GNS3 و Cisco Packet Tracer.',
            mile4_title: 'الخوارزميات وهياكل البيانات بلغة C++',
            mile4_desc: 'دراسة عميقة لمفاهيم البرمجة الكائنية المتقدمة وتطبيق هياكل البيانات يدوياً (القوائم المترابطة، الطوابير، المكدسات) مستنداً لمسار المهندس محمد أبو هدهود.',
            contact_badge: '// قنوات التواصل المباشر',
            contact_title: 'لنبنِ حلولاً آمنة ومبتكرة معاً',
            contact_desc: 'منفتح للتعاون في المشاريع التقنية، الأبحاث الأمنية، والفرص النوعية في تطوير البرمجيات والأمن السيبراني.',
            lbl_email: 'البريد الإلكتروني المباشر',
            lbl_github: 'مستودع الأكواد (GitHub)',
            lbl_location: 'الموقع والجامعة',
            lbl_location_val: 'تعز، الجمهورية اليمنية · جامعة تعز',
            cv_box_title: 'السيرة الذاتية المهنية والأكاديمية',
            cv_box_desc: 'يمكنك حفظ صفحة السيرة أو التواصل المباشر لطلب النسخة الأكاديمية الرسمية.',
            btn_print_cv: 'طباعة / حفظ السيرة الذاتية (PDF)',
            form_name_lbl: 'الاسم الكريم',
            form_email_lbl: 'البريد الإلكتروني',
            form_subject_lbl: 'موضوع الرسالة',
            form_msg_lbl: 'نص الرسالة',
            btn_send_msg: 'إرسال الرسالة فوراً',
            footer_credits: 'قسم الأمن السيبراني · كلية العلوم التطبيقية · جامعة تعز'
        },
        en: {
            loader_status: 'Loading Rami Amin Qasem Portfolio...',
            nav_role_sub: 'Cybersecurity & Software Engineering',
            nav_about: 'About',
            nav_academics: 'Academics',
            nav_skills: 'Skills',
            nav_projects: 'Projects & Research',
            nav_terminal: 'Interactive CLI',
            nav_journey: 'Journey',
            nav_contact: 'Contact',
            drawer_status: 'Level 4 Senior · Cybersecurity',
            hero_status_badge: 'Level 4 Senior Student · Cybersecurity Dept · Taiz University',
            hero_greeting: "Hello, I'm",
            hero_desc: 'Cybersecurity Engineer and Full-Stack / Mobile Developer. I bridge the gap between advanced defensive security (SOC operations, AI anomaly detection, network telemetry) and robust software engineering using Flutter (Clean Architecture) and distributed cloud platforms (Supabase, PostgreSQL RLS, Firebase). Passionate about building secure, resilient systems from code to cloud.',
            btn_view_projects: 'Explore Projects & Research',
            btn_try_terminal: 'Launch Cyber CLI',
            btn_contact_me: 'Get In Touch',
            metric_level: 'Taiz University',
            metric_projects: 'Projects & Labs',
            metric_ai: 'AI Models & Research',
            metric_security: 'Defensive Design',
            about_badge: '// Who I Am & Vision',
            about_title: 'Embedded Security & Systems Engineering',
            about_p1: 'I am Rami Amin Qasem Ali Saeed, a Cybersecurity Engineer and Software Developer in my final year (Level 4 Senior) at the Faculty of Applied Sciences, Taiz University.',
            about_p2: 'Throughout my academic and engineering journey, I have practiced "Security by Design". Security is not a superficial afterthought; it is woven into the database schema, Clean Architecture layer separation, cloud PostgreSQL RLS, and AI-driven predictive intrusion detection.',
            about_p3: 'I have designed and engineered production-grade mobile platforms with offline-first synchronization, fine-tuned large language models (LLaMA 3) for higher education services, and conducted cutting-edge research in digital-twin-based intrusion detection using Explainable AI (XAI).',
            about_card1_title: 'University & Academic Standing',
            about_card1_desc: 'Taiz University · Faculty of Applied Sciences · Cybersecurity Department (Level 4 Senior).',
            about_card2_title: 'SOC & SecOps Analysis',
            about_card2_desc: 'Security Operations Center analyst, threat detection engineering, and SIEM log aggregation.',
            about_card3_title: 'Clean Architecture',
            about_card3_desc: 'Advanced software design in Flutter separating business logic, state, and UI presentation.',
            about_card4_title: 'Networks & Cloud Infrastructure',
            about_card4_desc: 'Simulation via GNS3 and Cisco Packet Tracer, MikroTik routing, and Docker containerization.',
            academics_badge: '// Academic Specialization',
            academics_title: 'Taiz University · Faculty of Applied Sciences',
            academics_desc: 'Senior student (Level 4) in the Cybersecurity Department. Intensive applied and theoretical curriculum connecting deep security theory, network protocols, and robust software engineering.',
            pillar1_title: 'SOC & SecOps Engineering',
            pillar1_desc: 'Log aggregation & threat hunting using ELK Stack in Docker, network flow monitoring via Zeek & Suricata, and vulnerability assessment with Kali Linux & OWASP ZAP.',
            pillar2_title: 'Resilient Mobile Engineering',
            pillar2_desc: 'Cross-platform Flutter applications built on Clean Architecture, Offline-First caching with Hive, and modular state management.',
            pillar3_title: 'Cloud & Multi-Tenant SaaS',
            pillar3_desc: 'Designing and engineering multi-tenant SaaS platforms with strict PostgreSQL Row Level Security (RLS) isolation, modern React/TanStack frontends, and Supabase.',
            pillar4_title: 'AI & Security Research',
            pillar4_desc: 'Custom fine-tuning of Large Language Models (LLaMA 3), Explainable AI (SHAP), and deep learning sequence models for network anomaly prediction.',
            skills_badge: '// Capability Matrix',
            skills_title: 'Technical Arsenal & Proficiencies',
            skills_desc: 'Hands-on applied skills demonstrated across real production code, research models, and laboratory environments.',
            skill_g1_title: 'Cybersecurity & SOC',
            skill_g2_title: 'Software & Mobile Dev',
            skill_g3_title: 'Cloud, Databases & Infra',
            projects_badge: '// Featured Works',
            projects_title: 'Key Research & Systems Built',
            projects_desc: 'Production systems and cutting-edge research built to the highest architectural standards. Click any card for in-depth technical breakdowns.',
            filter_all: 'All',
            filter_sec: 'Cybersecurity & SOC',
            filter_mobile: 'Mobile Apps (Flutter)',
            filter_cloud: 'Cloud Systems & SaaS',
            filter_ai: 'AI & Research',
            btn_details: 'Full Project Breakdown',
            term_badge: '// Interactive Security Terminal',
            term_title: 'Rami CLI Environment',
            term_desc: 'Run real interactive commands to inspect my background, view live SOC metrics, or click quick command shortcuts.',
            quick_cmd_lbl: 'Quick commands:',
            journey_badge: '// Growth & Milestones',
            journey_title: 'Key Milestones',
            mile1_title: 'Senior Year at Cybersecurity Dept – Taiz University',
            mile1_desc: 'Focusing on advanced threat detection engineering, graduation thesis, and simulating enterprise cyberattacks via Digital Twins and Explainable AI.',
            mile2_title: 'Souq Yemen E-Commerce & LLaMA 3 University Chatbot',
            mile2_desc: 'Built Souq Yemen with Flutter Clean Architecture and Supabase PostgreSQL RLS; fine-tuned LLaMA 3 on Google Colab and Hugging Face for SUH.',
            mile3_title: 'SOC Labs (SIEM / ELK) & GNS3 Virtual Topologies',
            mile3_desc: 'Configured Dockerized ELK Stack threat labs, deployed MikroTik router security, and modeled enterprise networks in GNS3 and Cisco Packet Tracer.',
            mile4_title: 'C++ Foundations, Algorithms & Data Structures',
            mile4_desc: 'Deep study of advanced OOP and manual implementation of linked lists, queues, and stacks following Mohammed Abu-Hadhoud curriculum.',
            contact_badge: '// Direct Communication',
            contact_title: "Let's Build Secure, Innovative Solutions",
            contact_desc: 'Open for collaborations on technical projects, cybersecurity research, and high-impact engineering opportunities.',
            lbl_email: 'Direct Email',
            lbl_github: 'Code Repositories (GitHub)',
            lbl_location: 'Location & University',
            lbl_location_val: 'Taiz, Yemen · Taiz University',
            cv_box_title: 'Professional & Academic CV',
            cv_box_desc: 'Save or print this portfolio page or contact me directly for the official PDF resume.',
            btn_print_cv: 'Print / Save CV (PDF)',
            form_name_lbl: 'Your Name',
            form_email_lbl: 'Email Address',
            form_subject_lbl: 'Subject',
            form_msg_lbl: 'Message',
            btn_send_msg: 'Send Message Now',
            footer_credits: 'Cybersecurity Department · Faculty of Applied Sciences · Taiz University'
        }
    };

    const typingRoles = {
        ar: [
            'مهندس أمن سيبراني ومحلل SOC',
            'طالب مستوى رابع - جامعة تعز',
            'مطور تطبيقات Flutter و Clean Architecture',
            'باحث في كشف الهجمات بالتوأم الرقمي والـ XAI',
            'مهندس أنظمة سحابية سداسية الطبقات و SaaS'
        ],
        en: [
            'Cybersecurity Engineer & SOC Analyst',
            'Level 4 Senior · Taiz University',
            'Flutter & Clean Architecture Developer',
            'Digital Twin & Explainable AI Researcher',
            'Multi-Tenant Cloud & SaaS Engineer'
        ]
    };

    /* Language Switcher */
    let currentLang = localStorage.getItem('rami_portfolio_lang') || 'ar';

    function setLanguage(lang) {
        currentLang = lang;
        document.documentElement.lang = lang;
        document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';

        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (translations[lang] && translations[lang][key]) {
                el.textContent = translations[lang][key];
            }
        });

        document.querySelectorAll('.lang-label').forEach(el => {
            el.textContent = lang === 'ar' ? 'EN' : 'عربي';
        });

        localStorage.setItem('rami_portfolio_lang', lang);
        restartTyping();
    }

    document.querySelectorAll('.lang-toggle').forEach(btn => {
        btn.addEventListener('click', () => {
            setLanguage(currentLang === 'ar' ? 'en' : 'ar');
        });
    });

    /* Theme Toggle */
    const body = document.body;
    if (localStorage.getItem('rami_portfolio_theme') === 'light') {
        body.classList.remove('dark');
        body.classList.add('light');
    }

    function updateThemeIcons() {
        const isLight = body.classList.contains('light');
        document.querySelectorAll('.theme-icon').forEach(icon => {
            icon.classList.toggle('fa-sun', !isLight);
            icon.classList.toggle('text-yellow-400', !isLight);
            icon.classList.toggle('fa-moon', isLight);
            icon.classList.toggle('text-gray-700', isLight);
        });
    }

    function toggleTheme() {
        body.classList.toggle('dark');
        body.classList.toggle('light');
        updateThemeIcons();
        localStorage.setItem('rami_portfolio_theme', body.classList.contains('light') ? 'light' : 'dark');
    }

    document.querySelectorAll('.theme-toggle').forEach(btn => {
        btn.addEventListener('click', toggleTheme);
    });
    updateThemeIcons();

    /* Dynamic Typing */
    const typingElement = document.getElementById('typingText');
    let roleIdx = 0, charIdx = 0, isDeleting = false, typingTimer = null;

    function typeEffect() {
        const list = typingRoles[currentLang] || typingRoles.ar;
        const currentText = list[roleIdx % list.length];
        
        if (isDeleting) {
            typingElement.textContent = currentText.substring(0, charIdx - 1);
            charIdx--;
        } else {
            typingElement.textContent = currentText.substring(0, charIdx + 1);
            charIdx++;
        }

        let speed = isDeleting ? 40 : 80;
        if (!isDeleting && charIdx === currentText.length) {
            speed = 2200;
            isDeleting = true;
        } else if (isDeleting && charIdx === 0) {
            isDeleting = false;
            roleIdx = (roleIdx + 1) % list.length;
            speed = 400;
        }
        typingTimer = setTimeout(typeEffect, speed);
    }

    function restartTyping() {
        clearTimeout(typingTimer);
        roleIdx = 0; charIdx = 0; isDeleting = false;
        if (typingElement) {
            typingElement.textContent = '';
            typeEffect();
        }
    }

    /* Scroll Progress & Navbar styling */
    const navbar = document.getElementById('navbar');
    const scrollProgress = document.getElementById('scrollProgress');

    window.addEventListener('scroll', () => {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
        if (scrollProgress) scrollProgress.style.width = pct + '%';
        if (navbar) navbar.classList.toggle('shadow-2xl', scrollTop > 25);
    });

    /* Custom Cursor */
    const cursorDot = document.getElementById('cursorDot');
    const cursorOutline = document.getElementById('cursorOutline');
    if (window.matchMedia('(hover: hover)').matches) {
        window.addEventListener('mousemove', (e) => {
            if (cursorDot) {
                cursorDot.style.left = e.clientX + 'px';
                cursorDot.style.top = e.clientY + 'px';
            }
            if (cursorOutline) {
                cursorOutline.animate({ left: e.clientX + 'px', top: e.clientY + 'px' }, { duration: 450, fill: 'forwards' });
            }
        });
        document.querySelectorAll('a, button, .glass-card, input, textarea').forEach(el => {
            el.addEventListener('mouseenter', () => cursorOutline && cursorOutline.classList.add('hover'));
            el.addEventListener('mouseleave', () => cursorOutline && cursorOutline.classList.remove('hover'));
        });
    }

    /* Mobile Drawer */
    const mobileDrawer = document.getElementById('mobileDrawer');
    const drawerOverlay = document.getElementById('drawerOverlay');
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const closeDrawerBtn = document.getElementById('closeDrawerBtn');

    function openDrawer() {
        mobileDrawer.classList.add('open');
        drawerOverlay.classList.add('open');
        document.body.style.overflow = 'hidden';
    }
    function closeDrawer() {
        mobileDrawer.classList.remove('open');
        drawerOverlay.classList.remove('open');
        document.body.style.overflow = '';
    }

    if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', openDrawer);
    if (closeDrawerBtn) closeDrawerBtn.addEventListener('click', closeDrawer);
    if (drawerOverlay) drawerOverlay.addEventListener('click', closeDrawer);
    document.querySelectorAll('.drawer-link').forEach(link => link.addEventListener('click', closeDrawer));

    /* Filter Projects */
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectItems = document.querySelectorAll('.project-item');

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.getAttribute('data-filter');
            projectItems.forEach(item => {
                const categories = item.getAttribute('data-category').split(' ');
                if (filter === 'all' || categories.includes(filter)) {
                    item.style.display = 'flex';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });

    /* Project Modal */
    const modalOverlay = document.getElementById('projectModalOverlay');
    const modalBody = document.getElementById('modalBody');
    const closeModalBtn = document.getElementById('closeModalBtn');

    document.querySelectorAll('.open-modal-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const projKey = btn.getAttribute('data-project');
            const data = projectsData[projKey];
            if (!data) return;

            const isAr = currentLang === 'ar';
            const title = isAr ? data.title_ar : data.title_en;
            const subtitle = isAr ? data.subtitle_ar : data.subtitle_en;
            const desc = isAr ? data.desc_ar : data.desc_en;

            modalBody.innerHTML = `
                <div class="mb-4">
                    <span class="text-xs font-mono text-cyber-cyan font-bold tracking-wider">// PROJECT_DEEP_DIVE</span>
                    <h3 class="text-2xl font-extrabold text-white mt-1">${title}</h3>
                    <p class="text-sm text-cyber-blue font-mono mt-1">${subtitle}</p>
                </div>
                <div class="text-sm leading-relaxed text-gray-200 border-t border-b border-gray-700/50 py-4 my-4">
                    ${desc}
                </div>
                <div class="mt-4">
                    <span class="block text-xs font-mono text-gray-400 mb-2 font-bold">${isAr ? 'التقنيات المستخدمة في المشروع:' : 'Core Tech Stack:'}</span>
                    <div class="flex flex-wrap gap-2 font-mono text-xs">
                        ${data.tags.map(t => `<span class="px-3 py-1 rounded-lg bg-cyber-dark text-cyber-cyan border border-cyber-cyan/30">${t}</span>`).join('')}
                    </div>
                </div>
                <div class="mt-6 pt-4 flex flex-wrap justify-between items-center gap-3">
                    <a href="https://github.com/RA757575" target="_blank" class="px-5 py-2.5 rounded-xl btn-cyber text-xs font-bold inline-flex items-center gap-2">
                        <i class="fab fa-github"></i> <span>${isAr ? 'معاينة المستودع عبر GitHub' : 'View on GitHub'}</span>
                    </a>
                    <button class="px-4 py-2.5 rounded-xl glass text-xs text-gray-300 hover:text-white" onclick="closeModal()">
                        ${isAr ? 'إغلاق النافذة' : 'Close Window'}
                    </button>
                </div>
            `;
            modalOverlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    });

    function closeModal() {
        modalOverlay.classList.remove('active');
        document.body.style.overflow = '';
    }
    if (closeModalBtn) closeModalBtn.addEventListener('click', closeModal);
    if (modalOverlay) modalOverlay.addEventListener('click', (e) => {
        if (e.target === modalOverlay) closeModal();
    });

    /* Interactive Terminal CLI */
    const terminalInput = document.getElementById('terminalInput');
    const terminalOutput = document.getElementById('terminalOutput');

    const commands = {
        help: `الأوامر المتاحة في الطرفية:
  • <span class="text-cyber-cyan font-bold">whoami</span>       : عرض الهوية والتخصص الحالي
  • <span class="text-cyber-cyan font-bold">academics</span>    : تفاصيل دراسة الأمن السيبراني وجامعة تعز
  • <span class="text-cyber-cyan font-bold">projects</span>     : قائمة المشاريع البارزة المكتملة
  • <span class="text-cyber-cyan font-bold">soc-status</span>   : فحص حالة مجسات مركز العمليات ومختبر ELK
  • <span class="text-cyber-cyan font-bold">ai-models</span>    : النماذج الذكية المطورة (LLaMA 3 / XAI SHAP)
  • <span class="text-cyber-cyan font-bold">skills</span>       : ملخص الحزمة التقنية واللغات
  • <span class="text-cyber-cyan font-bold">contact</span>      : قنوات التواصل والبريد والـ GitHub
  • <span class="text-cyber-cyan font-bold">clear</span>        : مسح شاشة الطرفية`,

        whoami: `<span class="text-cyber-emerald font-bold">[IDENTITY_REPORT]</span>
الاسم: رامي أمين قاسم علي سعيد
التخصص: هندسة الأمن السيبراني (مستوى رابع - سنة التخرج)
الكلية: كلية العلوم التطبيقية — جامعة تعز
المسار: أمن سيبراني دفاعي (SOC/SIEM) + تطوير أنظمة سحابية وتطبيقات فلاتر (Clean Architecture)`,

        academics: `<span class="text-cyber-blue font-bold">[ACADEMIC_PROFILE]</span>
الجامعة: جامعة تعز (Taiz University)
المستوى: السنة الرابعة (المستوى الرابع)
المشروع البحثي: دليل الجامعة الذكي (SUH) بإشراف د. عزالدين المخلافي
أبحاث التخرج المتقدمة: نظام كشف الهجمات بالتوأم الرقمي والـ Explainable AI (XAI NIDS)`,

        projects: `<span class="text-cyber-cyan font-bold">[PORTFOLIO_PROJECTS]</span>
1. Smart University Handbook (Flutter + Fine-Tuned LLaMA 3 + Firebase)
2. Hybrid XAI NIDS (Autoencoder + LSTM + XGBoost + SHAP in GNS3)
3. Souq Yemen E-Commerce Platform & Admin (Flutter Clean Arch + Supabase RLS + Offline-First)
4. GigatopX EduCloud (Multi-Tenant SaaS with PostgreSQL RLS + React)
5. ELK Stack SOC Lab (Elasticsearch, Kibana, Docker Compose, Threat Logs)
6. Secure Employee Management (Python Flask, OWASP ZAP, SonarQube)`,

        'soc-status': `<span class="text-cyber-emerald font-bold">[SOC_SECURITY_TELEMETRY]</span>
[+] Elasticsearch Cluster : GREEN (Active on Port 9200)
[+] Kibana Dashboard      : RUNNING (Port 5601)
[+] Zeek & Suricata IDS   : CAPTURING (Packet stream normal)
[+] Anomaly Score Model   : 0.018 (Baseline Benign)
[+] Security Posture      : HARDENED (No Active Compromises)`,

        'ai-models': `<span class="text-cyber-purple font-bold">[AI_INNOVATION_MODULES]</span>
1. LLaMA 3 Fine-Tuned: نموذج ذكاء اصطناعي لغوي تم تدريبه على بيانات وأنظمة جامعة تعز (Google Colab & Hugging Face).
2. XAI SHAP Model: نظام تفسير قرارات كشف التسلل الشبكي وتحليل مساهمة الخصائص الرياضية لمحلل الـ SOC.`,

        skills: `<span class="text-cyber-cyan font-bold">[TECHNICAL_ARSENAL]</span>
Cybersecurity: SIEM, ELK Stack, Zeek, Suricata, Kali Linux, Metasploit, OWASP ZAP, SonarQube, RBAC
Development  : Flutter, Dart, Clean Architecture, Hive, React, TypeScript, Python (Flask), C++
Cloud & DB   : PostgreSQL (Row Level Security), Supabase, Firebase, Docker Compose, GNS3, MikroTik`,

        contact: `<span class="text-yellow-400 font-bold">[CONTACT_CHANNELS]</span>
Email  : ramyamyn41@gmail.com
GitHub : https://github.com/RA757575
Location: Taiz, Yemen (جامعة تعز)`
    };

    function runCommand(cmd) {
        cmd = cmd.trim().toLowerCase();
        if (cmd === 'clear') {
            terminalOutput.innerHTML = '';
            return;
        }

        const promptLine = document.createElement('div');
        promptLine.className = 'text-gray-400 mt-2 font-mono';
        promptLine.innerHTML = `<span class="text-cyber-cyan">guest@rami:~$</span> ${cmd}`;
        terminalOutput.appendChild(promptLine);

        const responseLine = document.createElement('div');
        responseLine.className = 'mt-1 text-gray-200';

        if (commands[cmd]) {
            responseLine.innerHTML = commands[cmd];
        } else {
            responseLine.innerHTML = `<span class="text-red-400">الأمر غير معروف: '${cmd}'. اكتب <span class="text-cyber-cyan font-bold">help</span> لعرض الأوامر.</span>`;
        }
        terminalOutput.appendChild(responseLine);
        terminalOutput.scrollTop = terminalOutput.scrollHeight;
    }

    function clearTerminal() {
        terminalOutput.innerHTML = '<p class="text-gray-400">تم مسح الشاشة. اكتب <span class="text-cyber-cyan font-bold">help</span> للمساعدة.</p>';
    }

    if (terminalInput) {
        terminalInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                const val = terminalInput.value;
                if (val.trim()) {
                    runCommand(val);
                    terminalInput.value = '';
                }
            }
        });
    }

    /* Contact Form Submission */
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const isAr = currentLang === 'ar';
            alert(isAr ? 'شكراً لتواصلك يا رامي! تم استلام رسالتك بنجاح وسأعاود الرد عليك قريباً عبر البريد الإلكتروني.' : 'Thank you for reaching out! Your message has been received successfully.');
            contactForm.reset();
        });
    }

    /* Background Particles */
    const canvas = document.getElementById('particles-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);

        const particles = [];
        for (let i = 0; i < 45; i++) {
            particles.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: Math.random() * 2 + 1,
                vx: (Math.random() - 0.5) * 0.7,
                vy: (Math.random() - 0.5) * 0.7,
                color: Math.random() > 0.5 ? 'rgba(0, 212, 255, 0.4)' : 'rgba(0, 255, 157, 0.3)'
            });
        }

        function drawParticles() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particles.forEach(p => {
                p.x += p.vx;
                p.y += p.vy;
                if (p.x < 0) p.x = canvas.width;
                if (p.x > canvas.width) p.x = 0;
                if (p.y < 0) p.y = canvas.height;
                if (p.y > canvas.height) p.y = 0;

                ctx.fillStyle = p.color;
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                ctx.fill();
            });

            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < 130) {
                        ctx.strokeStyle = `rgba(0, 212, 255, ${0.12 * (1 - dist / 130)})`;
                        ctx.lineWidth = 0.8;
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.stroke();
                    }
                }
            }
            requestAnimationFrame(drawParticles);
        }
        drawParticles();
    }

    /* Loader Fade Out */
    window.addEventListener('load', () => {
        setTimeout(() => {
            const loader = document.getElementById('loadingScreen');
            if (loader) loader.classList.add('hidden');
        }, 500);
    });

    /* Init Language & Typing */
    setLanguage(currentLang);
    </script>
</body>
</html>
'''

# 1. Write to Desktop folder
desktop_path = r'C:\Users\rami\Desktop\rami_portfolio\index.html'
with open(desktop_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# 2. Write to Downloads folder
downloads_path = r'C:\Users\rami\Downloads\rami-portfolio.html'
with open(downloads_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('SUCCESS')
print('Desktop:', desktop_path)
print('Downloads:', downloads_path)
