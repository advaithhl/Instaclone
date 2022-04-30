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
  xhr.open("GET", `like/?id=${id}`, false);
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
  xhr.open("GET", `unlike/?id=${id}`, false);
  xhr.send();
}
