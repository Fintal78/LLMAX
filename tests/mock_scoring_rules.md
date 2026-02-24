{
  "test_1_true_positive": {
    "source_link": "https://www.dxomark.com/apple-iphone-15-pro-max-camera-test/",
    "observed_justification": "The smart HDR feature helped produce very natural and pleasant colors, even in very challenging light conditions."
  },
  "test_2_true_negative_content_mismatch": {
    "source_link": "https://www.dxomark.com/apple-iphone-15-pro-max-camera-test/",
    "observed_justification": "The smart HDR feature helped produce very unnatural and awful colors, even in very challenging light conditions."
  },
  "test_3_true_negative_dead_link": {
    "source": "https://petapixel.com/2023/09/22/why-apple-chose-24mp-as-the-new-default-for-iphone-15-photos/",
    "exact_extract": "This link is a 404, so it should hard fail and not be masked."
  },
  "test_4_true_negative_placeholder": {
    "source": "https://...",
    "exact_extract": "This should fail because it is an abstract placeholder."
  },
  "test_5_managed_exception_bot_shield": {
    "unaccounted_feature": "Macrumors aggressively blocks bots, let's test a loose URL",
    "unaccounted_reason": "Testing the inline link (Source: https://www.macrumors.com/2023/09/20/apple-explains-iphone-15-24mp-photos/)"
  }
}
