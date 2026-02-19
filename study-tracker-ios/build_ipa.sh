#!/bin/bash
set -e

PROJ_DIR="$(cd "$(dirname "$0")" && pwd)"
BUILD_DIR="$PROJ_DIR/build"
ARCHIVE="$BUILD_DIR/StudyTracker.xcarchive"
PAYLOAD="$BUILD_DIR/Payload"
IPA="$BUILD_DIR/StudyTracker.ipa"

echo "📦  Building StudyTracker (unsigned, iOS 16, arm64)..."

rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

xcodebuild archive \
  -project "$PROJ_DIR/StudyTracker.xcodeproj" \
  -scheme StudyTracker \
  -configuration Release \
  -archivePath "$ARCHIVE" \
  -destination "generic/platform=iOS" \
  CODE_SIGN_IDENTITY="" \
  CODE_SIGNING_REQUIRED=NO \
  CODE_SIGNING_ALLOWED=NO \
  AD_HOC_CODE_SIGNING_ALLOWED=YES \
  ONLY_ACTIVE_ARCH=NO


if [ ! -d "$ARCHIVE/Products/Applications/StudyTracker.app" ]; then
  echo "❌  Archive failed — .app not found"
  exit 1
fi

echo "📦  Packaging into IPA..."
rm -rf "$PAYLOAD"
mkdir -p "$PAYLOAD"
cp -r "$ARCHIVE/Products/Applications/StudyTracker.app" "$PAYLOAD/"
cd "$BUILD_DIR"
zip -qr StudyTracker.ipa Payload/
rm -rf Payload

SIZE=$(du -sh "$IPA" | cut -f1)
echo ""
echo "✅  Done!"
echo "📱  IPA: $IPA  ($SIZE)"
echo ""
echo "Установка: перекинь StudyTracker.ipa на iPhone → открой в TrollStore → Install"
