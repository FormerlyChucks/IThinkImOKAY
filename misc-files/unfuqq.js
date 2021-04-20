(function() {
  const comments = document.getElementsByClassName("user-info");

  for (let x = 0; x < comments.length; x++) {
    let html = comments[x].innerHTML;
    if (html.includes("[This user has blocked you]")) {
      console.log("Match");
      comments[x].innerHTML = "[This user has blocked you (fetching...)]";
      fetch(`https://ruqqus.com/comment/${comments[x].parentNode.id.match(/(?<=comment-)\w{1,4}/)[0]}`, {credentials: 'omit'})
        .then(resp => {
          return resp.text();
        }).then((data) => {
          // dummy html
          let dummy = document.createElement('html');
          dummy.innerHTML = data;
          const revealedComment = dummy.querySelector(`#${comments[x].parentNode.id}`);
          comments[x].parentNode.innerHTML = revealedComment.innerHTML;
        })
        .catch(err => {
          comments[x].innerHTML = "[Error while fetching blocked comment]";
        });
    }
  };
})();
