$(document).ready(function () {
  $("textarea").each(function () {
    this.setAttribute(
      "style",
      "height:" + this.scrollHeight + "px;overflow-y:hidden;"
    );
  });

  $("textarea.comment-create-input").on({
    "input propertychange": function () {
      $("button.post-button").hide();
      if (this.value.length) {
        $("button.post-button").show();
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

function likeOrUnlikeAJAX(action, id) {
  const xhr = new XMLHttpRequest();
  xhr.onreadystatechange = () => {
    if (xhr.readyState == 4 && xhr.status == 200) {
      update_text = JSON.parse(xhr.response).text;
      $(`#likes-count-${id}`).text(update_text);
    }
  };
  if (action == "+") {
    xhr.open("GET", `/like/?id=${id}`, false);
    xhr.send();
  } else if (action == "-") {
    xhr.open("GET", `/unlike/?id=${id}`, false);
    xhr.send();
  }
}

function likePost(id) {
  $(`#like-div-${id}`).hide();
  $(`#unlike-div-${id}`).show();
  likeOrUnlikeAJAX("+", id);
}

function unlikePost(id) {
  $(`#unlike-div-${id}`).hide();
  $(`#like-div-${id}`).show();
  likeOrUnlikeAJAX("-", id);
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
  // This code is kinda sloppy, must be fixed after the interface redesign :(
  const input_text = document.getElementById("id_text");
  const proxy_input_text1 = document.getElementById("proxy_input_text1");
  const proxy_input_text2 = document.getElementById("proxy_input_text2");
  const post_button = document.getElementsByClassName("post-button")[0];

  if (proxy_input_text1.value == "") {
    if (proxy_input_text2.value != "") {
      input_text.value = proxy_input_text2.value;
      post_button.click();
    }
  } else {
    input_text.value = proxy_input_text1.value;
    post_button.click();
  }
}
