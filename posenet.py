<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/posenet"></script>


const net = await posenet.load();

const net = await posenet.load();

const pose = await net.estimateSinglePose(image, {
  flipHorizontal: false
});