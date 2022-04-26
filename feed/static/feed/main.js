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
