// Make a slide-ready clip: H.264 MP4 at a fixed size and bitrate, upright, no
// audio track, no metadata (no GPS, no device), plus a poster JPEG from mid-clip.
// macOS only, no install beyond the Swift that ships with the command line tools.
//
//   swift deck-kit/encode-video.swift <in.mov> <out-dir> <name> [--long 640] [--kbps 300] [--max 30]
//
// --long is the long side in pixels (the short side follows the clip's shape),
// --kbps the video bitrate, --max the most seconds kept. The defaults land a
// 25-second phone clip under 1 MB, so the bundler can inline it and the deck
// plays it with no network. Prints the <video> markup the kit expects.
import AVFoundation
import AppKit

var args = Array(CommandLine.arguments.dropFirst())
func opt(_ k: String, _ d: Double) -> Double {
  if let i = args.firstIndex(of: "--" + k), i + 1 < args.count { let v = Double(args[i + 1]) ?? d; args.removeSubrange(i...i + 1); return v }
  return d
}
let longSide = opt("long", 640), kbps = opt("kbps", 300), maxSec = opt("max", 30)
guard args.count == 3 else { FileHandle.standardError.write("usage: swift deck-kit/encode-video.swift <in.mov> <out-dir> <name> [--long 640] [--kbps 300] [--max 30]\n".data(using: .utf8)!); exit(2) }
let src = URL(fileURLWithPath: args[0]), dir = URL(fileURLWithPath: args[1], isDirectory: true), name = args[2]
try? FileManager.default.createDirectory(at: dir, withIntermediateDirectories: true)
let out = dir.appendingPathComponent(name + ".mp4"), posterURL = dir.appendingPathComponent(name + "-poster.jpg")
try? FileManager.default.removeItem(at: out)

let asset = AVURLAsset(url: src)
let sema = DispatchSemaphore(value: 0)
var track: AVAssetTrack!, natural = CGSize.zero, xf = CGAffineTransform.identity, duration = CMTime.zero
Task {
  track = try! await asset.loadTracks(withMediaType: .video).first!
  natural = try! await track.load(.naturalSize); xf = try! await track.load(.preferredTransform)
  duration = try! await asset.load(.duration)
  sema.signal()
}
sema.wait()

// Upright size, then scale so the long side is --long; even numbers for H.264.
let upright = natural.applying(xf), w0 = abs(upright.width), h0 = abs(upright.height)
let k = longSide / max(w0, h0)
let W = Int((w0 * k / 2).rounded()) * 2, H = Int((h0 * k / 2).rounded()) * 2
let seconds = min(CMTimeGetSeconds(duration), maxSec)
let range = CMTimeRange(start: .zero, duration: CMTime(seconds: seconds, preferredTimescale: 600))

// A video composition applies the phone's rotation and scales in one pass.
let comp = AVMutableVideoComposition()
comp.renderSize = CGSize(width: W, height: H)
comp.frameDuration = CMTime(value: 1, timescale: 30)
let instr = AVMutableVideoCompositionInstruction(); instr.timeRange = range
let layer = AVMutableVideoCompositionLayerInstruction(assetTrack: track)
let fit = CGAffineTransform(scaleX: CGFloat(W) / w0, y: CGFloat(H) / h0)
// Move the rotated frame back to the origin before scaling.
let r = CGRect(origin: .zero, size: natural).applying(xf)
layer.setTransform(xf.concatenating(CGAffineTransform(translationX: -r.minX, y: -r.minY)).concatenating(fit), at: .zero)
instr.layerInstructions = [layer]; comp.instructions = [instr]

let reader = try! AVAssetReader(asset: asset); reader.timeRange = range
let rout = AVAssetReaderVideoCompositionOutput(videoTracks: [track], videoSettings: [kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32BGRA])
rout.videoComposition = comp; reader.add(rout)
let writer = try! AVAssetWriter(outputURL: out, fileType: .mp4)
writer.shouldOptimizeForNetworkUse = true
let win = AVAssetWriterInput(mediaType: .video, outputSettings: [
  AVVideoCodecKey: AVVideoCodecType.h264, AVVideoWidthKey: W, AVVideoHeightKey: H,
  AVVideoCompressionPropertiesKey: [AVVideoAverageBitRateKey: Int(kbps * 1000), AVVideoProfileLevelKey: AVVideoProfileLevelH264HighAutoLevel, AVVideoMaxKeyFrameIntervalKey: 60]
])
win.expectsMediaDataInRealTime = false; writer.add(win)
reader.startReading(); writer.startWriting(); writer.startSession(atSourceTime: .zero)
let q = DispatchQueue(label: "enc")
win.requestMediaDataWhenReady(on: q) {
  while win.isReadyForMoreMediaData {
    if let s = rout.copyNextSampleBuffer() { win.append(s) } else { win.markAsFinished(); writer.finishWriting { sema.signal() }; return }
  }
}
sema.wait()
guard writer.status == .completed else { FileHandle.standardError.write("encode failed: \(String(describing: writer.error))\n".data(using: .utf8)!); exit(1) }

// Poster: the frame at mid-clip, upright, same size as the video.
let gen = AVAssetImageGenerator(asset: asset); gen.appliesPreferredTrackTransform = true
gen.maximumSize = CGSize(width: W, height: H); gen.requestedTimeToleranceBefore = .zero; gen.requestedTimeToleranceAfter = .zero
var cg: CGImage?
Task { cg = try? await gen.image(at: CMTime(seconds: seconds / 2, preferredTimescale: 600)).image; sema.signal() }
sema.wait()
if let cg = cg, let jpg = NSBitmapImageRep(cgImage: cg).representation(using: .jpeg, properties: [.compressionFactor: 0.8]) { try! jpg.write(to: posterURL) }

let kb = ((try? FileManager.default.attributesOfItem(atPath: out.path)[.size] as? Int) ?? 0) / 1024
FileHandle.standardError.write("wrote \(out.path) (\(W)x\(H), \(String(format: "%.1f", seconds)) s, \(kb) KB) and \(posterURL.lastPathComponent)\n".data(using: .utf8)!)
print("<video src=\"\(name).mp4\" poster=\"\(name)-poster.jpg\" width=\"\(W)\" height=\"\(H)\" muted loop playsinline preload=\"auto\" data-play=\"auto\" aria-label=\"[TBD: what is happening, no names]\"></video>")
