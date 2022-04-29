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

function likePost(id, currentCount) {
  $(`#like-div-${id}`).hide();
  $(`#unlike-div-${id}`).show();
  $(`#likes-count-${id}`).text(() => getLikesCountString(currentCount + 1));
}

function unlikePost(id, currentCount) {
  $(`#unlike-div-${id}`).hide();
  $(`#like-div-${id}`).show();
  $(`#likes-count-${id}`).text(() => getLikesCountString(currentCount));
}
