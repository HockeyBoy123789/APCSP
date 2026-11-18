import Foundation
import AVFoundation
import Vision
import AppKit

// Usage: ocr <video> [intervalSeconds]
let args = CommandLine.arguments
guard args.count >= 2 else {
    FileHandle.standardError.write("usage: ocr <video> [interval]\n".data(using: .utf8)!)
    exit(1)
}
let path = args[1]
let interval = args.count > 2 ? (Double(args[2]) ?? 2.0) : 2.0

let asset = AVURLAsset(url: URL(fileURLWithPath: path))
let duration = CMTimeGetSeconds(asset.duration)
let gen = AVAssetImageGenerator(asset: asset)
gen.appliesPreferredTrackTransform = true
gen.requestedTimeToleranceBefore = .zero
gen.requestedTimeToleranceAfter = .zero
if #available(macOS 13.0, *) {
    gen.maximumSize = CGSize(width: 1920, height: 1080)
}

func ocr(_ cg: CGImage) -> [String] {
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.usesLanguageCorrection = false
    req.recognitionLanguages = ["en-US"]
    let handler = VNImageRequestHandler(cgImage: cg, options: [:])
    do { try handler.perform([req]) } catch { return [] }
    let obs = req.results ?? []
    let sorted = obs.sorted { a, b in
        let ay = a.boundingBox.midY, by = b.boundingBox.midY
        if abs(ay - by) > 0.012 { return ay > by }
        return a.boundingBox.minX < b.boundingBox.minX
    }
    return sorted.compactMap { $0.topCandidates(1).first?.string }
}

var t = 0.0
while t < duration {
    let time = CMTime(seconds: t, preferredTimescale: 600)
    do {
        let cg = try gen.copyCGImage(at: time, actualTime: nil)
        let lines = ocr(cg)
        if !lines.isEmpty {
            print("=== t=\(String(format: "%.1f", t)) ===")
            for l in lines { print(l) }
        }
    } catch {
        // skip unreadable frame
    }
    t += interval
}
