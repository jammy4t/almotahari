export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    if (!url.pathname.startsWith("/bigfiles/")) {
      return new Response("🚫 غير مسموح", {
        status: 403,
        headers: { "Content-Type": "text/plain; charset=utf-8" }
      });
    }

    const ip = request.headers.get("cf-connecting-ip") || "unknown";
    const key = `mottahary:${ip}`;
    const current = await env.DOWNLOAD_LIMIT.get(key);
    const count = current ? parseInt(current) : 0;

    if (count >= 10) {
      return new Response("❌ لقد تجاوزت الحد المسموح به للتحميلات، حاول لاحقًا.", {
        status: 429,
        headers: { "Content-Type": "text/plain; charset=utf-8" }
      });
    }

    await env.DOWNLOAD_LIMIT.put(key, (count + 1).toString(), {
      expirationTtl: 3600
    });

    const filename = url.pathname.replace("/bigfiles/", "");
    const r2URL = `https://download.almotahari.com/bigfiles/${filename}`;
    return Response.redirect(r2URL, 302);
  }
}

