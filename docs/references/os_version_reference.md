# Operating System Version Reference (Canonical Source of Truth)

> [!IMPORTANT]
> This file is the **single canonical reference** for all operating system version labels and version ranges used across the entire database.
> All subsections in `scoring_rules.md`, `proposed_data_structure.md`, and `scoring_constants.md` that reference OS versions **MUST** use
> the exact version labels and ranges defined in this file to ensure absolute traceability and consistency.
>
> **Consumers of this file:**
> - §5.1 Support Longevity (OS cadence calculations)
> - §5.2 System Cleanliness & Control (skin lookup)
> - §6.3 GPU Performance → API Modifier (Ambiguous API Resolution Matrices 1, 2, 3)
> - §6.4 AI System → Software Stack Scoring (OS-based boolean rules)
> - §8.1 Battery Endurance → Layer C: Software Optimization Index (OS Power Management Architecture)

---

## 1. iOS (Apple iPhone)

Covers all iPhone models from the latest iOS (2026+) to the original iPhone OS 1 (2007) in descending chronological order.

> [!NOTE]
> In 2025, Apple changed its iOS versioning: the successor to iOS 18 is **iOS 26** (not iOS 19). This aligns iOS version numbers with the calendar year across all Apple platforms. There is no iOS 19 through iOS 25.

| Canonical OS Version Label | Release Year(s) | Operating System Family | Underlying Platform & Kernel | Hardware / Silicon Baseline |
| :------------------------- | :-------------- | :---------------------- | :--------------------------- | :-------------------------- |
| **iOS 27+**                | 2026+           | Apple iOS               | Darwin/XNU                   | Future Apple                |
| **iOS 26.x**               | 2025–2026       | Apple iOS               | Darwin/XNU                   | Apple A16–A19, M5           |
| **iOS 18.x**               | 2024–2025       | Apple iOS               | Darwin/XNU                   | Apple A14–A18, M4           |
| **iOS 17.x**               | 2023–2024       | Apple iOS               | Darwin/XNU                   | Apple A12–A17, M3           |
| **iOS 16.x**               | 2022–2023       | Apple iOS               | Darwin/XNU                   | Apple A11–A16, M2           |
| **iOS 15.x**               | 2021–2022       | Apple iOS               | Darwin/XNU                   | Apple A9–A15, M1            |
| **iOS 14.x**               | 2020–2021       | Apple iOS               | Darwin/XNU                   | Apple A9–A14                |
| **iOS 13.x**               | 2019–2020       | Apple iOS               | Darwin/XNU                   | Apple A9–A13                |
| **iOS 12.x**               | 2018–2019       | Apple iOS               | Darwin/XNU                   | Apple A7–A12                |
| **iOS 11.x**               | 2017–2018       | Apple iOS               | Darwin/XNU                   | Apple A9–A11                |
| **iOS 10.x**               | 2016–2017       | Apple iOS               | Darwin/XNU                   | Apple A7–A10                |
| **iOS 9.x**                | 2015–2016       | Apple iOS               | Darwin/XNU                   | Apple A7–A9X                |
| **iOS 8.x**                | 2014–2015       | Apple iOS               | Darwin/XNU                   | Apple A7–A8X                |
| **iOS 7.x**                | 2013–2014       | Apple iOS               | Darwin/XNU                   | Apple A7 (64-bit)           |
| **iOS 6.x**                | 2012–2013       | Apple iOS               | Darwin/XNU                   | Apple A6/A6X                |
| **iOS 5.x**                | 2011–2012       | Apple iOS               | Darwin/XNU                   | Apple A5/A5X                |
| **iOS 4.x**                | 2010–2011       | Apple iOS               | Darwin/XNU                   | Apple A4                    |
| **iPhone OS 3.2**          | 2010            | Apple iOS               | Darwin/XNU                   | Apple A4 (iPad)             |
| **iPhone OS 3.1**          | 2009–2010       | Apple iOS               | Darwin/XNU                   | Samsung A8                  |
| **iPhone OS 3.0**          | 2009            | Apple iOS               | Darwin/XNU                   | Samsung A8                  |
| **iPhone OS 2.2**          | 2008–2009       | Apple iOS               | Darwin/XNU                   | Samsung 1176                |
| **iPhone OS 2.1**          | 2008            | Apple iOS               | Darwin/XNU                   | Samsung 1176                |
| **iPhone OS 2.0**          | 2008            | Apple iOS               | Darwin/XNU                   | Samsung 1176                |
| **iPhone OS 1.1**          | 2007–2008       | Apple iOS               | Darwin/XNU                   | Samsung 1176                |
| **iPhone OS 1.0**          | 2007            | Apple iOS               | Darwin/XNU                   | Samsung 1176                |

---

## 2. Android (Google / OEM)

Covers all Android versions from the latest (2026) to the original Android 1.x (2008) in descending chronological order.

> [!NOTE]
> **Android Version Gaps:**
> There are no Android versions between Android 1.1 (Bender) and Android 1.5 (Cupcake). Google skipped versions 1.2, 1.3, and 1.4, proceeding directly from 1.1 to 1.5 when introducing the standard confectionery-themed dessert naming scheme.

| Canonical OS Version Label | Release Year(s) | Operating System Family | Underlying Platform & Kernel | Hardware / Silicon Baseline |
| :------------------------- | :-------------- | :---------------------- | :--------------------------- | :-------------------------- |
| **Android 17.0**           | 2026            | Android                 | AOSP/Linux                   | Next-gen GPU                |
| **Android 16.0**           | 2025            | Android                 | AOSP/Linux                   | Adreno 8xx+, G9             |
| **Android 15.0**           | 2024–2025       | Android                 | AOSP/Linux                   | Adreno 8xx, G925            |
| **Android 14.0**           | 2023–2024       | Android                 | AOSP/Linux                   | Adreno 7xx, G720            |
| **Android 13.0**           | 2022–2023       | Android                 | AOSP/Linux                   | Adreno 7xx, G715            |
| **Android 12L**            | 2022            | Android                 | AOSP/Linux                   | Same as Android 12.0        |
| **Android 12.0**           | 2021–2022       | Android                 | AOSP/Linux                   | Adreno 66x, G710            |
| **Android 11.0**           | 2020–2021       | Android                 | AOSP/Linux                   | Adreno 6xx, G78             |
| **Android 10.0**           | 2019–2020       | Android                 | AOSP/Linux                   | Adreno 6xx, G77             |
| **Android 9.0**            | 2018–2019       | Android                 | AOSP/Linux                   | Adreno 6xx, G76             |
| **Android 8.1**            | 2017–2018       | Android                 | AOSP/Linux                   | Adreno 5xx, G71/72          |
| **Android 8.0**            | 2017            | Android                 | AOSP/Linux                   | Adreno 5xx, G71/72          |
| **Android 7.1**            | 2016–2017       | Android                 | AOSP/Linux                   | Adreno 5xx, G71/72          |
| **Android 7.0**            | 2016            | Android                 | AOSP/Linux                   | Adreno 5xx, G71/72          |
| **Android 6.0**            | 2015–2016       | Android                 | AOSP/Linux                   | Adreno 430 (SD810)          |
| **Android 5.1**            | 2015            | Android                 | AOSP/Linux                   | Adreno 4xx, T7xx            |
| **Android 5.0**            | 2014–2015       | Android                 | AOSP/Linux                   | Adreno 4xx, T7xx            |
| **Android 4.4**            | 2013–2014       | Android                 | AOSP/Linux                   | Adreno 3xx, T6xx            |
| **Android 4.3**            | 2013            | Android                 | AOSP/Linux                   | Adreno 3xx, T6xx            |
| **Android 4.2**            | 2012–2013       | Android                 | AOSP/Linux                   | Adreno 2xx, M400            |
| **Android 4.1**            | 2012            | Android                 | AOSP/Linux                   | Adreno 2xx, M400            |
| **Android 4.0**            | 2011–2012       | Android                 | AOSP/Linux                   | Adreno 2xx, M400            |
| **Android 3.2**            | 2011–2012       | Android                 | AOSP/Linux                   | NVIDIA Tegra 2              |
| **Android 3.1**            | 2011            | Android                 | AOSP/Linux                   | NVIDIA Tegra 2              |
| **Android 3.0**            | 2011            | Android                 | AOSP/Linux                   | NVIDIA Tegra 2              |
| **Android 2.3**            | 2010–2011       | Android                 | AOSP/Linux                   | Adreno 2xx, SGX             |
| **Android 2.2**            | 2010            | Android                 | AOSP/Linux                   | Adreno 2xx, SGX             |
| **Android 2.1**            | 2010            | Android                 | AOSP/Linux                   | Adreno 2xx, SGX             |
| **Android 2.0**            | 2009            | Android                 | AOSP/Linux                   | Adreno 2xx, SGX             |
| **Android 1.6**            | 2009            | Android                 | AOSP/Linux                   | Adreno 130                  |
| **Android 1.5**            | 2009            | Android                 | AOSP/Linux                   | Adreno 130                  |
| **Android 1.1**            | 2009            | Android                 | AOSP/Linux                   | Adreno 130                  |
| **Android 1.0**            | 2008–2009       | Android                 | AOSP/Linux                   | Adreno 130                  |

---

## 3. Custom Operating Systems & Android Forks (Smartphone-Relevant Only)

These operating systems were developed by smartphone manufacturers as custom alternatives or forks of the Android Open Source Project (AOSP) to power their respective mobile devices.

### 3.1 HarmonyOS (Huawei)

Launched by **Huawei** in 2019 following US trade restrictions that blacklisted the company and barred them from using licensed Google Mobile Services (GMS) and the Google Play Store on future devices. Rather than merely creating a cosmetic theme, Huawei developed HarmonyOS to establish a complete, self-sustaining operating system platform. Designed from the ground up for the "Super Device" era, it aims to seamlessly unite smartphones, tablets, smart screens, wearables, and Internet of Things (IoT) appliances. Versions 2.0 through 4.0 maintained a hybrid kernel with Android (AOSP) code compatibility to ease app migration. However, **HarmonyOS 5.0 NEXT** marked a total architectural break, dropping all legacy AOSP code and Linux dependencies entirely in favor of Huawei's high-efficiency, native **HongMeng Microkernel** for maximum system fluidness, context-switching speed, and robust security.

| Canonical OS Version Label | Release Year(s) | Operating System Family | Underlying Platform & Kernel | Hardware / Silicon Baseline |
| :------------------------- | :-------------- | :---------------------- | :--------------------------- | :-------------------------- |
| **HarmonyOS 6.0**          | 2025–2026       | Custom                  | HongMeng Native              | HiSilicon Kirin             |
| **HarmonyOS 5.0 (NEXT)**   | 2024–2025       | Custom                  | HongMeng Native              | HiSilicon Kirin             |
| **HarmonyOS 4.0**          | 2023–2024       | Custom                  | AOSP/Linux 4.9+              | Kirin/Snapdragon            |
| **HarmonyOS 3.0**          | 2022–2023       | Custom                  | AOSP/Linux 4.9+              | Kirin/Snapdragon            |
| **HarmonyOS 2.0**          | 2021–2022       | Custom                  | AOSP/Linux 4.9+              | Kirin/Snapdragon            |
| **HarmonyOS 1.0**          | 2019–2020       | Custom                  | LiteOS/Linux                 | HiSilicon Honghu            |

### 3.2 HyperOS (Xiaomi)

Introduced by **Xiaomi** in 2023 to replace their long-standing MIUI User Interface (UI) skin. Rather than just updating the visual design, Xiaomi engineered HyperOS to completely unify their massive and diverse product ecosystem—encompassing smartphones, smart home appliances, wearables, and smart electric vehicles (such as the Xiaomi SU7)—under a single consolidated kernel layer. HyperOS achieves this by merging highly-optimized Android/Linux system frameworks with Xiaomi's proprietary Vela software platform at the kernel level (collectively named the **HyperCore** kernel) and coordinating it using an advanced cross-device interconnectivity framework called **HyperConnect**.

| Canonical OS Version Label | Release Year(s) | Operating System Family | Underlying Platform & Kernel | Hardware / Silicon Baseline |
| :------------------------- | :-------------- | :---------------------- | :--------------------------- | :-------------------------- |
| **HyperOS 3.0**            | 2025–2026       | Custom                  | HyperCore/Linux              | Qualcomm/MediaTek           |
| **HyperOS 2.0**            | 2024–2025       | Custom                  | HyperCore/Linux              | Qualcomm/MediaTek           |
| **HyperOS 1.0**            | 2023–2024       | Custom                  | HyperCore/Linux              | Qualcomm/MediaTek           |

---

## 4. Windows Phone & Windows Mobile Platforms (Smartphone-Only)

This section covers Microsoft's dedicated smartphone-specific operating systems. These operating systems were designed strictly to run on mobile smartphones (primarily the Nokia Lumia series, but also early smartphones from Samsung, HTC, and LG). This lineage ended in January 2020 when Windows 10 Mobile reached its final End of Life (EOL) and Microsoft officially withdrew from the smartphone OS market. This database includes these historical platforms in descending chronological order to ensure complete lookups of classic mobile hardware.

> [!NOTE]
> **Windows Mobile Versioning & Gaps:**
> - **Windows OS Versioning Gaps Explained:**
>   - **Gaps between 6.1 and 6.5**: Versions 6.2, 6.3, and 6.4 do not exist; Windows Mobile 6.5 was an interim touch-optimized update released directly after 6.1.
>   - **Gaps between 7.0 and 7.5**: Versions 7.1, 7.2, 7.3, and 7.4 do not exist; Microsoft jumped directly from 7.0 to 7.5 ("Mango") for its first major update with multitasking support.
>   - **Gaps between 7.5 and 7.8**: Versions 7.6 and 7.7 do not exist; Windows Phone 7.8 was backported directly to older devices as a final visual update matching Windows Phone 8's start screen.
>   - **Skipped Version 9**: "Windows Phone 9" did not exist; Microsoft jumped directly from Windows Phone 8.1 to Windows 10 Mobile to synchronize branding and kernel alignment with desktop Windows 10.
>   - **Skipped Version 11+**: "Windows 11 Mobile" does not exist because Microsoft discontinued mobile OS development and retired the platform in January 2020 at the final end-of-life of Windows 10 Mobile.
> - **YYMM Cadence:** Windows 10 Mobile adopted Microsoft's desktop "Windows as a Service" YYMM (Year/Month) release numbering scheme based on the final compilation month, though the actual public rollout usually occurred in the following month:
>   - **1709** (Fall Creators Update): Compiled in September 2017, publicly released in October 2017 (final active mobile branch).
>   - **1703** (Creators Update): Compiled in March 2017, publicly released in April 2017.
>   - **1607** (Anniversary Update): Compiled in July 2016, publicly released in August 2016.
>   - **1511** (Initial Launch): Compiled in November 2015, publicly released in November 2015.

| Canonical OS Version Label   | Release Year(s) | Operating System Family | Underlying Platform & Kernel | Hardware / Silicon Baseline |
| :--------------------------- | :-------------- | :---------------------- | :--------------------------- | :-------------------------- |
| **Windows 10 Mobile (1709)** | 2017–2020       | Windows                 | Windows NT Mobile            | Snapdragon 820/400          |
| **Windows 10 Mobile (1703)** | 2017            | Windows                 | Windows NT Mobile            | Snapdragon 820/400          |
| **Windows 10 Mobile (1607)** | 2016–2017       | Windows                 | Windows NT Mobile            | Snapdragon 820/400          |
| **Windows 10 Mobile (1511)** | 2015–2016       | Windows                 | Windows NT Mobile            | Snapdragon 820/400          |
| **Windows Phone 8.1**        | 2014–2015       | Windows                 | Windows Phone NT             | Snapdragon 800/400          |
| **Windows Phone 8 GDR**      | 2013–2014       | Windows                 | Windows Phone NT             | Snapdragon 800/400          |
| **Windows Phone 8.0**        | 2012–2013       | Windows                 | Windows Phone NT             | Snapdragon S4               |
| **Windows Phone 7.8**        | 2013            | Windows                 | Windows CE                   | Snapdragon S2               |
| **Windows Phone 7.5**        | 2011–2012       | Windows                 | Windows CE                   | Snapdragon S2               |
| **Windows Phone 7.0**        | 2010–2011       | Windows                 | Windows CE                   | Snapdragon S1               |
| **Windows Mobile 6.5**       | 2009–2010       | Windows                 | Windows CE 5/6               | Marvell PXA/OMAP            |
| **Windows Mobile 6.1**       | 2008–2009       | Windows                 | Windows CE 5/6               | Marvell PXA/OMAP            |
| **Windows Mobile 6.0**       | 2007–2008       | Windows                 | Windows CE 5/6               | Marvell PXA/OMAP            |
| **Windows Mobile 5.0**       | 2005–2007       | Windows                 | Windows CE 5/6               | Intel XScale/OMAP           |
