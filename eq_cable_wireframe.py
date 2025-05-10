import matplotlib.pyplot as plt

# Set up figure
fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')

# Wireframe structure as text
wireframe_text = """
EQ Cable Website Wireframe

[HEADER]
- Logo (top left)
- Navigation: Home | Shop | Boot Camps | Story | Contact | Cart | Wallet Connect (crypto)

[HERO SECTION]
- Full-width video background or static image (EarthTone Analog + Scott soldering)
- Tagline: “Precision Audio Cables Built to Perform”
- Call-to-Action: [Shop Now] [Join a Boot Camp]

[FEATURES SECTION]
- Icons or small visuals:
  - Handmade Craftsmanship
  - Trusted by 200+ Influencers
  - Built with Premium Soldering
  - Crypto & Genius Dollar Friendly

[PRODUCT SHOWCASE]
- Grid layout of cables with photos, prices, and “Add to Cart” buttons
- Filters: Type | Length | Color | Connector

[BOOT CAMP SECTION]
- Overview + Pricing tiers
- [Enroll Now] button
- Highlight video or testimonial carousel

[ABOUT / STORY SECTION]
- Scott’s Story Video
- Influencer montage
- “Why EQ Cable?” comparison chart

[LOYALTY & CRYPTO INTEGRATION]
- Genius Dollar info
- How to earn/redeem
- Token/NFT registry for limited edition cables

[FOOTER]
- Social links
- Contact info
- Quick links
- Crypto wallet integration
"""

# Add text to the plot
plt.text(0, 1, wireframe_text, fontsize=10, va='top', fontfamily='monospace')

# Layout adjustment
plt.tight_layout()

# Save the image
plt.savefig("eq_cable_wireframe.png")

# Optional: Display while debugging
# plt.show()


