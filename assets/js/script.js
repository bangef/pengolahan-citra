window.addEventListener("DOMContentLoaded", () => {
	const btnLoad = document.querySelector("#btnLoad");
	btnLoad.addEventListener("click", main);
});
const buildRgb = (imageData) => {
	const rgbValues = [];
	// note that we are loopin every 4!
	// for every Red, Green, Blue and Alpha
	for (let i = 0; i < imageData.length; i += 4) {
		const rgb = {
			r: imageData[i],
			g: imageData[i + 1],
			b: imageData[i + 2],
		};

		rgbValues.push(rgb);
	}

	return rgbValues;
};
const main = () => {
	const imgFile = document.getElementById("imgfile");
	const image = new Image();
	const file = imgFile.files[0];
	const fileReader = new FileReader();

	console.log(imgFile, image, file, fileReader);
	// Whenever file & image is loaded procced to extract the information from the image
	fileReader.onload = () => {
		image.onload = () => {
			// Set the canvas size to be the same as of the uploaded image
			const canvas = document.getElementById("canvas");
			canvas.width = image.width;
			canvas.height = image.height;
			const ctx = canvas.getContext("2d");
			ctx.drawImage(image, 0, 0);

			/**
			 * getImageData returns an array full of RGBA values
			 * each pixel consists of four values: the red value of the colour, the green, the blue and the alpha
			 * (transparency). For array value consistency reasons,
			 * the alpha is not from 0 to 1 like it is in the RGBA of CSS, but from 0 to 255.
			 */
			const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
			// Convert the image data to RGB values so its much simpler
			const rgbArray = buildRgb(imageData.data);
			console.log(rgbArray);

			/**
			 * Color quantization
			 * A process that reduces the number of colors used in an image
			 * while trying to visually maintin the original image as much as possible
			 */
			// const quantColors = quantization(rgbArray, 0);

			// Create the HTML structure to show the color palette
			// buildPalette(quantColors);
		};
		image.src = fileReader.result;
	};
	fileReader.readAsDataURL(file);
};
