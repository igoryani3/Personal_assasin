#!/usr/bin/env python3
"""
Generates StudyTracker.xcodeproj/project.pbxproj for the Study Tracker iOS app.
Run from the study-tracker-ios/ directory.
"""
import uuid, os

def uid():
    return uuid.uuid4().hex[:24].upper()

# ── UUIDs ────────────────────────────────────────────────────
PROJ              = uid()
MAIN_GROUP        = uid()
PRODUCTS_GROUP    = uid()
SOURCES_GROUP     = uid()

# File references
APP_REF           = uid()   # StudyTracker.app (product)
APP_MAIN_REF      = uid()
CONTENT_REF       = uid()
WEBVIEW_REF       = uid()
SETUP_REF         = uid()
SETTINGS_REF      = uid()
PLIST_REF         = uid()
ASSETS_REF        = uid()   # Assets.xcassets

# Build file entries
APP_MAIN_BF       = uid()
CONTENT_BF        = uid()
WEBVIEW_BF        = uid()
SETUP_BF          = uid()
SETTINGS_BF       = uid()
ASSETS_BF         = uid()

# Phases
SOURCES_PHASE     = uid()
FRAMEWORKS_PHASE  = uid()
RESOURCES_PHASE   = uid()

# Target / configurations
TARGET            = uid()
CFG_LIST_PROJ     = uid()
CFG_LIST_TARGET   = uid()
DEBUG_PROJ        = uid()
RELEASE_PROJ      = uid()
DEBUG_TARGET      = uid()
RELEASE_TARGET    = uid()

pbxproj = f"""// !$*UTF8*$!
{{
\tarchiveVersion = 1;
\tclasses = {{
\t}};
\tobjectVersion = 56;
\tobjects = {{

/* Begin PBXBuildFile section */
\t\t{APP_MAIN_BF} /* StudyTrackerApp.swift in Sources */ = {{isa = PBXBuildFile; fileRef = {APP_MAIN_REF} /* StudyTrackerApp.swift */; }};
\t\t{CONTENT_BF} /* ContentView.swift in Sources */ = {{isa = PBXBuildFile; fileRef = {CONTENT_REF} /* ContentView.swift */; }};
\t\t{WEBVIEW_BF} /* WebView.swift in Sources */ = {{isa = PBXBuildFile; fileRef = {WEBVIEW_REF} /* WebView.swift */; }};
\t\t{SETUP_BF} /* SetupView.swift in Sources */ = {{isa = PBXBuildFile; fileRef = {SETUP_REF} /* SetupView.swift */; }};
\t\t{SETTINGS_BF} /* SettingsView.swift in Sources */ = {{isa = PBXBuildFile; fileRef = {SETTINGS_REF} /* SettingsView.swift */; }};
\t\t{ASSETS_BF} /* Assets.xcassets in Resources */ = {{isa = PBXBuildFile; fileRef = {ASSETS_REF} /* Assets.xcassets */; }};
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
\t\t{APP_REF} /* StudyTracker.app */ = {{isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = StudyTracker.app; sourceTree = BUILT_PRODUCTS_DIR; }};
\t\t{APP_MAIN_REF} /* StudyTrackerApp.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = StudyTrackerApp.swift; sourceTree = "<group>"; }};
\t\t{CONTENT_REF} /* ContentView.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ContentView.swift; sourceTree = "<group>"; }};
\t\t{WEBVIEW_REF} /* WebView.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = WebView.swift; sourceTree = "<group>"; }};
\t\t{SETUP_REF} /* SetupView.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SetupView.swift; sourceTree = "<group>"; }};
\t\t{SETTINGS_REF} /* SettingsView.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SettingsView.swift; sourceTree = "<group>"; }};
\t\t{PLIST_REF} /* Info.plist */ = {{isa = PBXFileReference; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; }};
\t\t{ASSETS_REF} /* Assets.xcassets */ = {{isa = PBXFileReference; lastKnownFileType = folder.assetcatalog; path = Assets.xcassets; sourceTree = "<group>"; }};
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
\t\t{FRAMEWORKS_PHASE} /* Frameworks */ = {{
\t\t\tisa = PBXFrameworksBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t}};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
\t\t{MAIN_GROUP} = {{
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t{SOURCES_GROUP} /* StudyTracker */,
\t\t\t\t{PRODUCTS_GROUP} /* Products */,
\t\t\t);
\t\t\tsourceTree = "<group>";
\t\t}};
\t\t{PRODUCTS_GROUP} /* Products */ = {{
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t{APP_REF} /* StudyTracker.app */,
\t\t\t);
\t\t\tname = Products;
\t\t\tsourceTree = "<group>";
\t\t}};
\t\t{SOURCES_GROUP} /* StudyTracker */ = {{
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t{APP_MAIN_REF} /* StudyTrackerApp.swift */,
\t\t\t\t{CONTENT_REF} /* ContentView.swift */,
\t\t\t\t{WEBVIEW_REF} /* WebView.swift */,
\t\t\t\t{SETUP_REF} /* SetupView.swift */,
\t\t\t\t{SETTINGS_REF} /* SettingsView.swift */,
\t\t\t\t{ASSETS_REF} /* Assets.xcassets */,
\t\t\t\t{PLIST_REF} /* Info.plist */,
\t\t\t);
\t\t\tpath = StudyTracker;
\t\t\tsourceTree = "<group>";
\t\t}};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
\t\t{TARGET} /* StudyTracker */ = {{
\t\t\tisa = PBXNativeTarget;
\t\t\tbuildConfigurationList = {CFG_LIST_TARGET} /* Build configuration list for PBXNativeTarget "StudyTracker" */;
\t\t\tbuildPhases = (
\t\t\t\t{SOURCES_PHASE} /* Sources */,
\t\t\t\t{FRAMEWORKS_PHASE} /* Frameworks */,
\t\t\t\t{RESOURCES_PHASE} /* Resources */,
\t\t\t);
\t\t\tbuildRules = (
\t\t\t);
\t\t\tdependencies = (
\t\t\t);
\t\t\tname = StudyTracker;
\t\t\tproductName = StudyTracker;
\t\t\tproductReference = {APP_REF} /* StudyTracker.app */;
\t\t\tproductType = "com.apple.product-type.application";
\t\t}};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
\t\t{PROJ} /* Project object */ = {{
\t\t\tisa = PBXProject;
\t\t\tattributes = {{
\t\t\t\tBuildIndependentTargetsInParallel = 1;
\t\t\t\tLastSwiftUpdateCheck = 1600;
\t\t\t\tLastUpgradeCheck = 1600;
\t\t\t\tTargetAttributes = {{
\t\t\t\t\t{TARGET} = {{
\t\t\t\t\t\tCreatedOnToolsVersion = 16.0;
\t\t\t\t\t}};
\t\t\t\t}};
\t\t\t}};
\t\t\tbuildConfigurationList = {CFG_LIST_PROJ} /* Build configuration list for PBXProject "StudyTracker" */;
\t\t\tcompatibilityVersion = "Xcode 14.0";
\t\t\tdevelopmentRegion = en;
\t\t\thasScannedForEncodings = 0;
\t\t\tknownRegions = (
\t\t\t\ten,
\t\t\t\tBase,
\t\t\t);
\t\t\tmainGroup = {MAIN_GROUP};
\t\t\tproductRefGroup = {PRODUCTS_GROUP} /* Products */;
\t\t\tprojectDirPath = "";
\t\t\tprojectRoot = "";
\t\t\ttargets = (
\t\t\t\t{TARGET} /* StudyTracker */,
\t\t\t);
\t\t}};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
\t\t{RESOURCES_PHASE} /* Resources */ = {{
\t\t\tisa = PBXResourcesBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
\t\t\t\t{ASSETS_BF} /* Assets.xcassets in Resources */,
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t}};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
\t\t{SOURCES_PHASE} /* Sources */ = {{
\t\t\tisa = PBXSourcesBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
\t\t\t\t{APP_MAIN_BF} /* StudyTrackerApp.swift in Sources */,
\t\t\t\t{CONTENT_BF} /* ContentView.swift in Sources */,
\t\t\t\t{WEBVIEW_BF} /* WebView.swift in Sources */,
\t\t\t\t{SETUP_BF} /* SetupView.swift in Sources */,
\t\t\t\t{SETTINGS_BF} /* SettingsView.swift in Sources */,
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t}};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
\t\t{DEBUG_PROJ} /* Debug */ = {{
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {{
\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;
\t\t\t\tCLANG_ANALYZER_NONNULL = YES;
\t\t\t\tCLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
\t\t\t\tCLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
\t\t\t\tCLANG_ENABLE_MODULES = YES;
\t\t\t\tCLANG_ENABLE_OBJC_ARC = YES;
\t\t\t\tCLANG_ENABLE_OBJC_WEAK = YES;
\t\t\t\tCOPY_PHASE_STRIP = NO;
\t\t\t\tDEBUG_INFORMATION_FORMAT = dwarf;
\t\t\t\tENABLE_STRICT_OBJC_MSGSEND = YES;
\t\t\t\tENABLE_TESTABILITY = YES;
\t\t\t\tGCC_C_LANGUAGE_STANDARD = gnu17;
\t\t\t\tGCC_DYNAMIC_NO_PIC = NO;
\t\t\t\tGCC_NO_COMMON_BLOCKS = YES;
\t\t\t\tGCC_OPTIMIZATION_LEVEL = 0;
\t\t\t\tGCC_PREPROCESSOR_DEFINITIONS = (
\t\t\t\t\t"DEBUG=1",
\t\t\t\t\t"$(inherited)",
\t\t\t\t);
\t\t\t\tMTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
\t\t\t\tMTL_FAST_MATH = YES;
\t\t\t\tONLY_ACTIVE_ARCH = YES;
\t\t\t\tSDKROOT = iphoneos;
\t\t\t\tSWIFT_ACTIVE_COMPILATION_CONDITIONS = DEBUG;
\t\t\t\tSWIFT_OPTIMIZATION_LEVEL = "-Onone";
\t\t\t}};
\t\t\tname = Debug;
\t\t}};
\t\t{RELEASE_PROJ} /* Release */ = {{
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {{
\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;
\t\t\t\tCLANG_ANALYZER_NONNULL = YES;
\t\t\t\tCLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
\t\t\t\tCLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
\t\t\t\tCLANG_ENABLE_MODULES = YES;
\t\t\t\tCLANG_ENABLE_OBJC_ARC = YES;
\t\t\t\tCLANG_ENABLE_OBJC_WEAK = YES;
\t\t\t\tCOPY_PHASE_STRIP = NO;
\t\t\t\tDEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
\t\t\t\tENABLE_NS_ASSERTIONS = NO;
\t\t\t\tENABLE_STRICT_OBJC_MSGSEND = YES;
\t\t\t\tGCC_C_LANGUAGE_STANDARD = gnu17;
\t\t\t\tGCC_NO_COMMON_BLOCKS = YES;
\t\t\t\tMTL_ENABLE_DEBUG_INFO = NO;
\t\t\t\tMTL_FAST_MATH = YES;
\t\t\t\tSDKROOT = iphoneos;
\t\t\t\tSWIFT_COMPILATION_MODE = wholemodule;
\t\t\t\tSWIFT_OPTIMIZATION_LEVEL = "-O";
\t\t\t\tVALIDATE_PRODUCT = YES;
\t\t\t}};
\t\t\tname = Release;
\t\t}};
\t\t{DEBUG_TARGET} /* Debug */ = {{
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {{
\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
\t\t\t\tASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
\t\t\t\tCODE_SIGN_IDENTITY = "";
\t\t\t\tCODE_SIGN_STYLE = Manual;
\t\t\t\tCODE_SIGNING_ALLOWED = NO;
\t\t\t\tCODE_SIGNING_REQUIRED = NO;
\t\t\t\tCURRENT_PROJECT_VERSION = 1;
\t\t\t\tDEVELOPMENT_ASSET_PATHS = "";
\t\t\t\tDEVELOPMENT_TEAM = "";
\t\t\t\tENABLE_PREVIEWS = YES;
\t\t\t\tGENERATE_INFOPLIST_FILE = NO;
\t\t\t\tINFOPLIST_FILE = StudyTracker/Info.plist;
\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 16.0;
\t\t\t\tLD_RUNPATH_SEARCH_PATHS = (
\t\t\t\t\t"$(inherited)",
\t\t\t\t\t"@executable_path/Frameworks",
\t\t\t\t);
\t\t\t\tMARKETING_VERSION = 1.0;
\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.studytracker.app;
\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";
\t\t\t\tSUPPORTED_PLATFORMS = iphoneos;
\t\t\t\tSWIFT_EMIT_LOC_STRINGS = YES;
\t\t\t\tSWIFT_VERSION = 5.0;
\t\t\t\tTARGETED_DEVICE_FAMILY = "1,2";
\t\t\t}};
\t\t\tname = Debug;
\t\t}};
\t\t{RELEASE_TARGET} /* Release */ = {{
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {{
\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
\t\t\t\tASSTCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
\t\t\t\tCODE_SIGN_IDENTITY = "";
\t\t\t\tCODE_SIGN_STYLE = Manual;
\t\t\t\tCODE_SIGNING_ALLOWED = NO;
\t\t\t\tCODE_SIGNING_REQUIRED = NO;
\t\t\t\tCURRENT_PROJECT_VERSION = 1;
\t\t\t\tDEVELOPMENT_ASSET_PATHS = "";
\t\t\t\tDEVELOPMENT_TEAM = "";
\t\t\t\tENABLE_PREVIEWS = YES;
\t\t\t\tGENERATE_INFOPLIST_FILE = NO;
\t\t\t\tINFOPLIST_FILE = StudyTracker/Info.plist;
\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 16.0;
\t\t\t\tLD_RUNPATH_SEARCH_PATHS = (
\t\t\t\t\t"$(inherited)",
\t\t\t\t\t"@executable_path/Frameworks",
\t\t\t\t);
\t\t\t\tMARKETING_VERSION = 1.0;
\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.studytracker.app;
\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";
\t\t\t\tSUPPORTED_PLATFORMS = iphoneos;
\t\t\t\tSWIFT_EMIT_LOC_STRINGS = YES;
\t\t\t\tSWIFT_VERSION = 5.0;
\t\t\t\tTARGETED_DEVICE_FAMILY = "1,2";
\t\t\t}};
\t\t\tname = Release;
\t\t}};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
\t\t{CFG_LIST_PROJ} /* Build configuration list for PBXProject "StudyTracker" */ = {{
\t\t\tisa = XCConfigurationList;
\t\t\tbuildConfigurations = (
\t\t\t\t{DEBUG_PROJ} /* Debug */,
\t\t\t\t{RELEASE_PROJ} /* Release */,
\t\t\t);
\t\t\tdefaultConfigurationIsVisible = 0;
\t\t\tdefaultConfigurationName = Release;
\t\t}};
\t\t{CFG_LIST_TARGET} /* Build configuration list for PBXNativeTarget "StudyTracker" */ = {{
\t\t\tisa = XCConfigurationList;
\t\t\tbuildConfigurations = (
\t\t\t\t{DEBUG_TARGET} /* Debug */,
\t\t\t\t{RELEASE_TARGET} /* Release */,
\t\t\t);
\t\t\tdefaultConfigurationIsVisible = 0;
\t\t\tdefaultConfigurationName = Release;
\t\t}};
/* End XCConfigurationList section */

\t}};
\trootObject = {PROJ} /* Project object */;
}}
"""

os.makedirs("StudyTracker.xcodeproj", exist_ok=True)
with open("StudyTracker.xcodeproj/project.pbxproj", "w") as f:
    f.write(pbxproj)

print("✅  Generated StudyTracker.xcodeproj/project.pbxproj")
