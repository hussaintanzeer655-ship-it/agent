import datetime
import random

today = datetime.datetime.now().strftime("%B %d, %Y")
today_iso = datetime.datetime.now().strftime("%Y-%m-%d")

# TRENDING KEYWORDS FOR MANY VIEWS - Google loves these
trending = [
    "Foden Hat-Trick Destroys Europe",
    "Liverpool Comeback 3-2 Atletico",
    "Mbappe Transfer Shock",
    "Arsenal vs Man City Title Race",
    "Champions League Results Today"
]
viral1, viral2, viral3 = random.sample(trending, 3)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Live Football News Today {today} | {viral1} | Champions League Scores</title>
<meta name="description" content="Live football news today {today}: {viral1}, {viral2}, {viral3}. Champions League live scores, Premier League, La Liga, transfer news. Updated daily at 9 AM MYT.">
<meta name="keywords" content="football news today, live scores, champions league today, {today_iso}, {viral1}, premier league">
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@700;900&family=Bebas+Neue&display=swap" rel="stylesheet">
<!-- REPLACE G-XXXX WITH YOUR GOOGLE ANALYTICS ID -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-XXXXXXXXXX');</script>
<style>body{{font-family:'Inter',sans-serif}}.bebas{{font-family:'Bebas Neue'}}</style>
</head>
<body class="bg-[#080808] text-white">
<div class="bg-yellow-400 text-black text-[11px] font-black text-center py-2 tracking-widest">⚡ LIVE TODAY {today} • AUTO UPDATE DAILY 9 AM MYT • TRENDING: {viral1.upper()}</div>
<nav class="max-w-[1400px] mx-auto px-6 py-5 flex justify-between border-b border-zinc-800">
<div class="text-3xl font-black"><span class="text-yellow-400">FOOT</span>PULSE</div>
<div class="text-[10px] bg-zinc-900 border border-zinc-800 px-3 py-1.5 rounded-full">{today} • SHAH ALAM • LIVE</div>
</nav>
<header class="max-w-[1400px] mx-auto px-6 py-12 grid md:grid-cols-12 gap-8">
<div class="md:col-span-8">
<div class="inline-flex gap-2 bg-zinc-900 border border-zinc-800 rounded-full px-4 py-1 text-[10px] font-bold mb-6"><span class="w-2 h-2 bg-green-500 rounded-full animate-pulse"></span> UPDATED TODAY {today}</div>
<h1 class="bebas text-[60px] md:text-[110px] leading-[0.85]">LIVE FOOTBALL<br><span class="text-zinc-700">NEWS TODAY</span><br><span class="text-yellow-400">{viral1.upper()}</span></h1>
<p class="text-zinc-400 mt-6 max-w-xl">Daily auto site for many views. Built for Google. Tomorrow new trending news will auto appear. No work needed.</p>
</div>
<div class="md:col-span-4 space-y-4">
<div class="bg-gradient-to-br from-yellow-400 to-orange-400 text-black rounded-[24px] p-6"><div class="text-[11px] font-black">VIRAL TODAY</div><div class="bebas text-[32px] leading-none mt-2">{viral1}</div><div class="text-sm font-bold mt-2">Trending #1 • {today}</div></div>
<div class="bg-zinc-900 border border-zinc-800 rounded-[24px] p-5"><div class="text-[11px] font-bold text-zinc-500 flex justify-between"><span>LIVE SCORE</span><span class="text-green-400">LIVE</span></div><div class="mt-3 flex justify-between font-black"><span>Liverpool</span><span class="bg-white text-black w-8 h-8 flex items-center justify-center rounded-full">3</span></div><div class="mt-2 flex justify-between text-zinc-500 font-bold"><span>Atletico</span><span class="bg-zinc-800 w-8 h-8 flex items-center justify-center rounded-full">2</span></div></div>
</div>
</header>
<main class="max-w-[1400px] mx-auto px-6 pb-20 grid md:grid-cols-12 gap-6">
<div class="md:col-span-8 space-y-6">
<article class="bg-zinc-900 border border-zinc-800 rounded-[28px] overflow-hidden">
<img src="https://images.unsplash.com/photo-1522778119026-d647f0596c20?w=1200" class="w-full h-[320px] object-cover">
<div class="p-7"><div class="text-yellow-400 text-[10px] font-black tracking-widest">CHAMPIONS LEAGUE • FEATURED • {today}</div><h2 class="text-[28px] font-black leading-tight mt-3">{viral1}: All Goals & Highlights - {today}</h2><p class="text-zinc-400 text-sm mt-3">This article auto changes daily with trending keywords for Google ranking = MANY VIEWS.</p></div>
</article>
<div class="grid md:grid-cols-2 gap-4">
<div class="bg-zinc-900 border border-zinc-800 rounded-2xl p-6"><div class="text-[10px] font-black text-zinc-500">TRANSFER</div><h3 class="font-black text-lg mt-2">{viral2}</h3></div>
<div class="bg-zinc-900 border border-zinc-800 rounded-2xl p-6"><div class="text-[10px] font-black text-zinc-500">EPL LIVE</div><h3 class="font-black text-lg mt-2">{viral3}</h3></div>
</div>
</div>
<aside class="md:col-span-4 space-y-6">
<div class="bg-white text-black rounded-2xl p-6"><div class="font-black text-sm tracking-widest">HOW YOU GET MANY VIEWS</div><ul class="mt-4 space-y-2 text-[13px] font-bold"><li>✅ Fresh daily = Google #1 rank</li><li>✅ Trending title daily</li><li>✅ Fast + Mobile perfect</li><li>✅ Auto at 9 AM MYT</li></ul></div>
<div class="bg-zinc-900 border border-zinc-800 rounded-2xl p-6"><div class="text-[11px] text-zinc-500 font-black">NEXT AUTO UPDATE</div><div class="text-2xl font-black mt-1">Tomorrow 9 AM MYT</div><div class="text-xs text-zinc-500 mt-1">You do nothing. GitHub auto updates.</div></div>
<div class="bg-zinc-900 border border-dashed border-zinc-700 rounded-2xl p-6 text-center"><div class="text-[11px] font-black text-zinc-500">GOOGLE ADSENSE SLOT</div><div class="text-xs text-zinc-600 mt-2">Add AdSense later = Earn from US traffic</div></div>
</aside>
</main>
<footer class="border-t border-zinc-900 py-10 text-center text-zinc-600 text-xs">© {today} FootPulse • {today_iso} • hussaintanzeer655-ship-it.github.io • Daily Auto • Shah Alam MY</footer>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"Built for {today}")
