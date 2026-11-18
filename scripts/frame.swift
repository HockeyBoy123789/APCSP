import Foundation
import AVFoundation
import AppKit

// Usage: frame <video> <seconds> <out.png>
let a = CommandLine.arguments
guard a.count >= 4 else { exit(1) }
let asset = AVURLAsset(url: URL(fileURLWithPath: a[1]))
let gen = AVAssetImageGenerator(asset: asset)
gen.appliesPreferredTrackTransform = true
gen.requestedTimeToleranceBefore = .zero
gen.requestedTimeToleranceAfter = .zero
let t = Double(a[2]) ?? 0
let cg = try! gen.copyCGImage(at: CMTime(seconds: t, preferredTimescale: 600), actualTime: nil)
let rep = NSBitmapImageRep(cgImage: cg)
let data = rep.representation(using: .png, properties: [:])!
try! data.write(to: URL(fileURLWithPath: a[3]))
print("wrote \(a[3]) \(cg.width)x\(cg.height)")
