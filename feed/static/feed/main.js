$(document).ready(function () {
  $("textarea").each(function () {
    this.setAttribute(
      "style",
      "height:" + this.scrollHeight + "px;overflow-y:hidden;"
    );
  });

  $("textarea.comment-create-input").on({
    "input propertychange": function () {
      $("#post-button").hide();
      if (this.value.length) {
        $("#post-button").show();
        this.style.height = "auto";
        this.style.height = this.scrollHeight + "px";
      } else {
        this.style.height = "38px";
      }
    },
  });
});

function getLikesCountString(newCount) {
  return `${newCount} ${newCount != 1 ? "likes" : "like"}`;
}

function likePost(id) {
  $(`#like-div-${id}`).hide();
  $(`#unlike-div-${id}`).show();
  $(`#likes-count-${id}`).text((_, currentContent) => {
    let currentCount = parseInt(currentContent.trim().split(" ")[0]);
    return getLikesCountString(currentCount + 1);
  });
  const xhr = new XMLHttpRequest();
  xhr.open("GET", `/like/?id=${id}`, false);
  xhr.send();
}

function unlikePost(id) {
  $(`#unlike-div-${id}`).hide();
  $(`#like-div-${id}`).show();
  $(`#likes-count-${id}`).text((_, currentContent) => {
    let currentCount = parseInt(currentContent.trim().split(" ")[0]);
    return getLikesCountString(currentCount - 1);
  });
  const xhr = new XMLHttpRequest();
  xhr.open("GET", `/unlike/?id=${id}`, false);
  xhr.send();
}

function openImagePicker() {
  const input_content = document.getElementById("id_content");

  input_content.onchange = showUploadedImage;
  input_content.click();

  function showUploadedImage() {
    const imageholder = document.getElementById("image-holder");
    const imageholderparent = document.getElementById("image-holder-parent");

    imageholder.classList.remove("image-upload-item");

    const img = document.createElement("img");
    img.src = URL.createObjectURL(this.files[0]);
    img.onload = function () {
      const aspect_ratio = img.width / img.height;
      if (aspect_ratio > 1) {
        imageholderparent.classList.add("image-holder-parent-landscape");
        imageholder.classList.add("uploaded-img-holder");
        img.width = 538;
      } else if (aspect_ratio == 1) {
        img.width = img.height = 538;
      } else if (aspect_ratio < 1) {
        imageholderparent.classList.add("image-holder-parent-portrait");
        imageholder.classList.add("uploaded-img-holder");
        img.height = 538;
      }
      imageholderparent.classList.replace("border-danger", "border-dark");
      URL.revokeObjectURL(this.src);

      const post_button = document.getElementById("proxy_submit_button");
      post_button.removeAttribute("disabled");
    };
    imageholder.replaceChild(img, imageholder.childNodes[1]);
  }
}

function submitPost() {
  const input_caption = document.getElementById("id_caption");
  const proxy_input_caption = document.getElementById("proxy_input_caption");
  const submit_button = document.getElementById("id_submit_button");

  input_caption.value = proxy_input_caption.value;
  submit_button.click();
}

function submitComment() {
  const input_text = document.getElementById("id_text");
  const proxy_input_text = document.getElementById("proxy_input_text");
  const post_button = document.getElementById("post-button");

  input_text.value = proxy_input_text.value;
  post_button.click();
}
