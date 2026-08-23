/**
 * Affiliate Link Click Tracker
 * Auto-detects outbound affiliate links and fires Umami custom events.
 * Works retroactively on all existing + future review content.
 *
 * Attribution note (2026-08-24): Umami Cloud's /eventData API is broken
 * (Cloudflare worker "ReadableStream is disturbed" bug), so custom event
 * payloads (target/review/url) cannot be read back via API. To keep
 * attribution working, the affiliate target is encoded INTO THE EVENT NAME
 * (e.g. affiliate_click_tradingview) — the events endpoint still returns
 * eventName + urlPath reliably. Do not revert to payload-only tracking.
 */
(function() {
  'use strict';

  // Affiliate domains → event target name
  var domains = {
    'tradingview.com': 'tradingview',
    'okx.com': 'okx',
    'moomoo.com': 'moomoo',
    'coinbase.com': 'coinbase'
  };

  // Extract review slug from pathname (last non-empty segment)
  function getSlug() {
    var parts = window.location.pathname.split('/').filter(Boolean);
    if (parts.length === 0) return 'home';
    // Handle nested paths like /reviews/rsi/ → slug is last segment
    return parts[parts.length - 1] || parts[parts.length - 2] || 'unknown';
  }

  document.addEventListener('click', function(e) {
    var link = e.target.closest('a');
    if (!link) return;

    var href = link.getAttribute('href') || '';
    if (!href) return;

    for (var domain in domains) {
      if (href.indexOf(domain) !== -1) {
        var target = domains[domain];
        var slug = getSlug();

        // Umami custom event — uses sendBeacon, survives navigation.
        // Target is encoded in the event NAME for reliable attribution.
        if (typeof umami !== 'undefined' && umami.track) {
          try {
            umami.track('affiliate_click_' + target, {
              target: target,
              review: slug,
              url: href
            });
          } catch (err) {
            // Silent fail — never block navigation
          }
        }

        // Only track first matching domain per click
        break;
      }
    }
  }, { passive: true });
})();
